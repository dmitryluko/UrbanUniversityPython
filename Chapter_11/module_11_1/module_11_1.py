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
            'units': 'metric'  # Specify metric units
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

    def get_weather_details(self) -> Dict[str, Any]:  # FIXME

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
    def __init__(self, api_key, location: LocationWeatherPoint = None):
        self.api_key = api_key
        self.location = location
        self.history_data = pd.DataFrame()

    def fetch_weather_data(self):
        """Fetch weather data for the past 30 years for the given location."""
        # Define the base URL template for the OpenWeatherMap historical data API
        url_template = "https://history.openweathermap.org/data/2.5/history/city?lat={}&lon={}&type=hour&start={}&cnt={}&appid={}"
        lat, lon = self.location

        for year in range(1994, 2024):
            start_timestamp = int(pd.Timestamp(f'{year}-01-01').timestamp())
            end_timestamp = int(pd.Timestamp(f'{year}-12-31').timestamp())
            cnt = 8760  # Approximate number of hourly data points in a year (24*365)
            url = url_template.format(lat, lon, start_timestamp, cnt, self.api_key)
            response = requests.get(url)
            if response.status_code == 200:
                yearly_data = response.json()
                if 'list' in yearly_data:
                    yearly_df = pd.DataFrame(yearly_data['list'])
                    self.history_data = pd.concat([self.history_data, yearly_df], ignore_index=True)
                else:
                    print(f"No data for year: {year}")
            else:
                print(f"Failed to fetch data for year: {year}, Status Code: {response.status_code}")

        self.history_data.to_csv(f'historical_weather_data_{self.location.name}.csv', index=False)

    def generate_analytics(self):
        """Generate useful analytics from the weather data."""
        self.history_data['datetime'] = pd.to_datetime(self.history_data['date'])
        self.history_data.set_index('datetime', inplace=True)
        self.daily_mean = self.history_data.resample('D').mean()
        self.monthly_mean = self.history_data.resample('M').mean()
        self.yearly_mean = self.history_data.resample('Y').mean()

    def plot_data(self):
        """Generate and display plots for weather data."""
        plt.figure(figsize=(10, 6))
        plt.plot(self.daily_mean['temperature'], label='Daily Mean Temperature')
        plt.plot(self.monthly_mean['temperature'], label='Monthly Mean Temperature')
        plt.plot(self.yearly_mean['temperature'], label='Yearly Mean Temperature')
        plt.xlabel('Date')
        plt.ylabel('Temperature')
        plt.title(f'Temperature Trends Over 30 Years in {self.location.name}')
        plt.legend()
        plt.show()

    def generate_pdf_report(self, filename):
        """Generate a PDF report of the analytics."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Weather History Report for {self.location.name}", ln=True, align='C')
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, txt="This report contains weather history analytics for the past 30 years.")
        plt.figure(figsize=(10, 6))
        plt.plot(self.yearly_mean['temperature'], label='Yearly Mean Temperature')
        plt.xlabel('Date')
        plt.ylabel('Temperature')
        plt.title('Yearly Temperature Trends')
        plt.legend()
        plt.savefig('temp_plot.png')
        pdf.image('temp_plot.png', x=10, y=50, w=190)
        pdf.output(filename)
        print(f"PDF report generated: {filename}")


# Update `main` function to demonstrate the Weather class usage:
def main():
    api_key = os.getenv('API_KEY')  # Get the API key from environment variables
    if not api_key:
        raise ValueError("API key not found in environment variables")

    targets = ['Moscow', 'New York', 'Tokyo']
    weather_ = Weather(api_key=api_key)
    weather_.get_weather_report(targets)

    # location = Location(name='Los Angeles')
    # weather_history = WeatherHistory(api_key, location)
    # weather_history.fetch_weather_data()
    # weather_history.generate_analytics()
    # weather_history.plot_data()
    # weather_history.generate_pdf_report('weather_report.pdf')


# Run the example
if __name__ == "__main__":
    main()
