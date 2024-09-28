from typing import Dict, Any, Tuple
from typing import List

from fpdf import FPDF
from rich.console import Console
from rich.table import Table
from datetime import datetime
from dotenv import load_dotenv
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

load_dotenv()


class LocationWeatherPoint:
    GEOCODING_API_URL = "http://api.openweathermap.org/geo/1.0/direct"
    ONE_CALL_API_URL = "https://api.openweathermap.org/data/3.0/onecall"

    def __init__(self, **kwargs):
        self.api_key = kwargs.get('api_key', None)
        self.__raw_data = {}
        self.name = kwargs.get('name', '')
        self.__lat = None
        self.__lon = None

        try:
            self.__lat, self.__lon = self._validate_and_get_location_details(**kwargs)
            self.__raw_data = self.get_weather_details()
        except ValueError as e:
            print(e)
            self.__raw_data = {}

    def _validate_and_get_location_details(self, **kwargs) -> Tuple[float, float]:
        if 'name' in kwargs:
            return self._find_by_name(kwargs['name'])
        elif 'latitude' in kwargs and 'longitude' in kwargs:
            return kwargs['latitude'], kwargs['longitude']
        else:
            raise ValueError("Either 'name' or 'latitude' and 'longitude' must be provided")

    def _find_by_name(self, city_name: str) -> Tuple[float, float]:
        params = {
            'q': city_name,
            'appid': self.api_key,
        }
        response = requests.get(self.GEOCODING_API_URL, params=params)
        response.raise_for_status()
        results = response.json()
        if not results:
            raise ValueError("City not found")
        return results[0]['lat'], results[0]['lon']

    @property
    def lat(self):
        return self.__lat

    @property
    def lon(self):
        return self.__lon

    def get_weather_details(self) -> Dict[str, Any]:
        params = {
            'lat': self.lat,
            'lon': self.lon,
            'appid': self.api_key,
            'units': 'metric'  # Specify metric units
        }
        response = requests.get(self.ONE_CALL_API_URL, params=params)
        response.raise_for_status()
        return response.json()

    def __str__(self):
        return f"Location(Name: {self.name}, Coordinates: {self.__lat}, {self.__lon})"

    def __repr__(self):
        return f"Location(name={self.name!r}, coordinates=({self.__lat}, {self.__lon}), api_key={'*' * len(self.api_key)})"


class Weather:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.console = Console()

    def get_weather_report(self, targets: List[str]):
        for target in targets:
            location = LocationWeatherPoint(api_key=self.api_key, name=target)
            weather_data = location.get_weather_details()
            self.console.print(f"[bold yellow]Weather for {target}[/bold yellow]")
            self._print_current_weather(weather_data)
            self._print_three_day_forecast(weather_data)

    def _print_current_weather(self, data: Dict[str, Any]):
        current = data.get('current', {})
        table = Table(title="[cyan]Current Weather[/cyan]")
        table.add_column("Description")
        table.add_column("Temperature (°C)")
        table.add_column("Humidity (%)")
        table.add_column("Wind Speed (m/s)")
        table.add_row(
            f"[blue]{current.get('weather', [{}])[0].get('description', 'N/A')}[/blue]",
            f"[red]{current.get('temp', 'N/A')}[/red]",
            f"[green]{current.get('humidity', 'N/A')}[/green]",
            f"[magenta]{current.get('wind_speed', 'N/A')}[/magenta]"
        )
        self.console.print(table)

    def _print_three_day_forecast(self, data: Dict[str, Any]):
        daily = data.get('daily', [])
        table = Table(title="[cyan]3-Day Forecast[/cyan]")
        table.add_column("Date")
        table.add_column("Description")
        table.add_column("Max Temp (°C)")
        table.add_column("Min Temp (°C)")
        for day in daily[:3]:
            date = datetime.fromtimestamp(day.get('dt', 0)).strftime('%Y-%m-%d')
            table.add_row(
                f"[yellow]{date}[/yellow]",
                f"[blue]{day.get('weather', [{}])[0].get('description', 'N/A')}[/blue]",
                f"[red]{day.get('temp', {}).get('max', 'N/A')}[/red]",
                f"[green]{day.get('temp', {}).get('min', 'N/A')}[/green]"
            )
        self.console.print(table)

    def __str__(self):
        return f"Weather(API Key: {'*' * len(self.api_key)})"

    def __repr__(self):
        return f"Weather(api_key={'*' * len(self.api_key)})"


class WeatherHistory:
    def __init__(self, api_key=None, location: LocationWeatherPoint = None):
        """
        Initialize the WeatherHistory object.

        Parameters:
        api_key (str): API key for accessing weather data.
        location (LocationWeatherPoint): Object containing location details.
        """
        self.api_key = api_key
        self.location = location
        self.daily_mean = pd.DataFrame()
        self.monthly_mean = pd.DataFrame()
        self.yearly_mean = pd.DataFrame()
        self.__raw_data: pd.DataFrame = pd.DataFrame()

    def fetch_weather_data(self):
        """
        Fetch weather data from the API and process it.
        """
        if not self.api_key or not self.location:
            logging.error("API key or location not set.")
            return

        # Example URL, replace with actual API endpoint
        url = f'https://history.openweathermap.org/data/2.5/history/city?lat={self.location.lat}&lon={self.location.lon}&type=hour&appid={self.api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.__raw_data = self.process_yearly_weather_data(data)
        else:
            logging.error(f"Failed to fetch data: {response.status_code} {response.reason}")

    @staticmethod
    def process_yearly_weather_data(data) -> pd.DataFrame:
        """
        Process the yearly data into a DataFrame.
        Parameters:
        data (dict): Raw weather data that contains a list of weather records.
        Returns:
        pd.DataFrame: Processed DataFrame with datetime conversion.
        """
        logging.info('Processing yearly data...')

        if not data or 'list' not in data:
            logging.warning('No data provided or "list" key is missing in the data.')
            return pd.DataFrame()  # Return an empty DataFrame

        try:
            # Extract the list of weather records
            weather_records = data['list']

            # Create DataFrame
            df = pd.json_normalize(weather_records)

            # Define the date column
            date_column = 'dt'

            # Check if date_column exists and convert to datetime
            if date_column in df.columns:
                df['date'] = pd.to_datetime(df[date_column], unit='s')
                logging.info('Date column converted to datetime.')
            else:
                logging.warning(f"'{date_column}' column is missing in the data.")

            # Set 'date' as the index

            df.set_index('date', inplace=True)

            return df
        except Exception as e:
            logging.error(f'An error occurred during processing: {e}')
            return pd.DataFrame()  # Return an empty DataFrame in case of error

    def _save_data_to_csv(self, filename: str) -> None:
        """
        Save data to a CSV file.
        Parameters:
        df (pd.DataFrame): DataFrame to be saved.
        filename (str): Name of the file where data will be saved.
        """
        try:
            self.__raw_data.to_csv(filename, index=False)
            logging.info(f"Data saved to {filename}.")
        except Exception as e:
            logging.error(f"Failed to save data to CSV: {e}")

    def generate_analytics(self):
        """
        Generate analytics such as daily, monthly, and yearly mean temperatures.
        Parameters:
        df (pd.DataFrame): Processed DataFrame containing weather data.
        """
        logging.info("Generating analytics...")

        if self.__raw_data.empty:
            logging.warning("No data to generate analytics.")
            return

        # Resampling and calculating mean temperatures
        self.daily_mean = self.__raw_data['main.temp'].resample('D').mean()
        self.monthly_mean = self.__raw_data['main.temp'].resample('ME').mean()
        self.yearly_mean = self.__raw_data['main.temp'].resample('YE').mean()

    logging.info("Analytics generated.")

    def plot_data(self):
        """
        Plot data for visualization.
        """
        plt.figure(figsize=(10, 6))
        if not self.daily_mean.empty:
            self._plot_series(self.daily_mean, 'Daily Mean Temperature')
        if not self.monthly_mean.empty:
            self._plot_series(self.monthly_mean, 'Monthly Mean Temperature')
        if not self.yearly_mean.empty:
            self._plot_series(self.yearly_mean, 'Yearly Mean Temperature')
        plt.xlabel('Date')
        plt.ylabel('Temperature')
        plt.title(f'Temperature Trends Over 30 Years in {self.location}')
        plt.legend()
        plt.show()

    @staticmethod
    def _plot_series(df, label):

        logging.info(f"Plotting '{df.info}'...")

        if df.values is not None and len(df.values) > 0:
            logging.info(f'Plotting with label "{label}"...')
            plt.plot(df.index, df.values, label=label)
        else:
            logging.warning(f'Values not found!')

    def generate_pdf_report(self, filename):
        """
        Generate a PDF report with the weather history analytics.
        Parameters:
        filename (str): The name of the PDF file to be generated.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Weather History Report for {self.location}", ln=True, align='C')
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, txt="This report contains weather history analytics for the past 30 years.")

        plt.figure(figsize=(10, 6))
        self._plot_series(self.yearly_mean, 'Yearly Mean Temperature', 'temp')
        plt.xlabel('Date')
        plt.ylabel('Temperature')
        plt.title('Yearly Temperature Trends')
        plt.legend()
        plt.savefig('temp_plot.png')
        pdf.image('temp_plot.png', x=10, y=50, w=190)

        pdf.output(filename)
        logging.info(f"PDF report generated: {filename}")


# Update `main` function to demonstrate the Weather class usage:
def main():
    API_KEY = os.getenv('API_KEY')  # Get the API key from environment variables
    if not API_KEY:
        raise ValueError("API key not found in environment variables")

    # targets = ['Moscow', 'New York', 'Tokyo']
    # weather_ = Weather(api_key=API_KEY)
    # weather_.get_weather_report(targets)

    location = LocationWeatherPoint(api_key=API_KEY, name='Los Angeles')
    weather_history = WeatherHistory(api_key=API_KEY, location=location)
    weather_history.fetch_weather_data()
    weather_history.generate_analytics()
    weather_history.plot_data()
    # weather_history.generate_pdf_report('weather_report.pdf')


# Run the example
if __name__ == "__main__":
    main()
