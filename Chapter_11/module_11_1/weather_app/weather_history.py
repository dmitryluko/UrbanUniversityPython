import pandas as pd
import requests
import matplotlib.pyplot as plt
import logging
from typing import Optional, Dict, Tuple
from fpdf import FPDF
from .location_weather import LocationWeatherPoint

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
API_URL_TEMPLATE = 'https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&appid={apikey}'
CSV_INDEX = False
PLOT_FIG_SIZE = (10, 6)


class WeatherHistory:
    def __init__(self, api_key: str, location: Optional[LocationWeatherPoint] = None):
        self.api_key: str = api_key
        self.location: Optional[LocationWeatherPoint] = location
        self.daily_mean: pd.DataFrame = pd.DataFrame()
        self.monthly_mean: pd.DataFrame = pd.DataFrame()
        self.yearly_mean: pd.DataFrame = pd.DataFrame()
        self._raw_data: pd.DataFrame = pd.DataFrame()
        self.date_for_years: Optional[pd.DataFrame] = None

    def fetch_weather_data(self) -> None:
        """Fetch weather data from the API and process it."""
        if not self.api_key or not self.location:
            logging.error('API key or location not set.')
            return
        response = requests.get(
            API_URL_TEMPLATE.format(lat=self.location.lat, lon=self.location.lon, apikey=self.api_key)
        )
        if response.status_code == 200:
            data = response.json()
            self._raw_data = self.process_weather_data(data)
        else:
            logging.error(f'Failed to fetch data: {response.status_code} {response.reason}')

    @staticmethod
    def process_weather_data(data: Dict) -> pd.DataFrame:
        """Process raw weather data to a pandas DataFrame with datetime index."""
        logging.info('Processing weather data...')
        if not data or 'list' not in data:
            logging.warning('No data provided or "list" key is missing in the data.')
            return pd.DataFrame()

        try:
            weather_records = data['list']
            df = pd.json_normalize(weather_records)
            date_column = 'dt'
            if date_column in df.columns:
                df['date'] = pd.to_datetime(df[date_column], unit='s')
                df.set_index('date', inplace=True)
                logging.info('Date column converted to datetime and set as index.')
            else:
                logging.warning(f"'{date_column}' column is missing in the data.")
            return df
        except Exception as e:
            logging.error(f'An error occurred during processing: {e}')
            return pd.DataFrame()

    def save_data_to_csv(self, filename: str) -> None:
        """Save the raw data to a CSV file."""
        self._save_dataframe_to_csv(self._raw_data, filename)

    @staticmethod
    def _save_dataframe_to_csv(df: pd.DataFrame, filename: str) -> None:
        """Save a DataFrame to a CSV file."""
        try:
            df.to_csv(filename, index=CSV_INDEX)
            logging.info(f'Data saved to {filename}.')
        except Exception as e:
            logging.error(f'Failed to save data to CSV: {e}')

    def _years_by_date(self, given_date: pd.Timestamp) -> pd.DataFrame:
        """
        Returns all data for the given date in all available years.
        Args:
            given_date (pd.Timestamp): The date provided as a Pandas Timestamp.
        Returns:
            pd.DataFrame: Data for the given date across all available years.
        """
        if self._raw_data.empty:
            logging.warning('No data available to filter.')
            return pd.DataFrame()

        try:
            # Extract the month and day from the given_date
            month = given_date.month
            day = given_date.day
            # Extract the month and day from the data
            self._raw_data['month'] = self._raw_data.index.month
            self._raw_data['day'] = self._raw_data.index.day
            # Filter the DataFrame to match the given month and day
            date_filtered_data = self._raw_data[
                (self._raw_data['month'] == month) &
                (self._raw_data['day'] == day)
                ]
            # Drop the temporary month and day columns
            date_filtered_data = date_filtered_data.drop(columns=['month', 'day'])
            if date_filtered_data.empty:
                logging.warning(f'No data found for the given date: {given_date.strftime("%m-%d")}.')
            return date_filtered_data
        except Exception as e:
            logging.error(f'An error occurred while filtering data for given date {given_date.strftime("%m-%d")}: {e}')
            return pd.DataFrame()

    def generate_analytics(self) -> None:
        """Generate analytics data like daily, monthly, and yearly means."""
        logging.info('Generating analytics...')
        if self._raw_data.empty:
            logging.warning('No data to generate analytics.')
            return
        self.date_for_years = self._years_by_date(pd.to_datetime('today'))
        logging.info('Analytics generated.')

    @staticmethod
    def _get_mean_series(df: pd.DataFrame, freq: str) -> pd.DataFrame:
        """Compute mean values for specific frequency."""
        if 'main.temp' not in df.columns:
            logging.warning("'main.temp' column is missing in the data.")
            return pd.DataFrame()
        try:
            mean_series = df.resample(freq)['main.temp'].mean()
            logging.info(f'Mean series computed with frequency "{freq}".')
            return mean_series
        except KeyError as e:
            logging.error(f'Column missing for resampling: {e}')
            return pd.DataFrame()
        except Exception as e:
            logging.error(f'An error occurred during resampling: {e}')
            return pd.DataFrame()

    def _plot_date_for_years_stats(self) -> None:
        """Plot temperature, wind speed, and humidity statistics for specific dates across years."""
        if self.date_for_years is None or self.date_for_years.empty:
            logging.warning('No data available to plot.')
            return
        try:
            plt.figure(figsize=PLOT_FIG_SIZE)
            # Plot temperature (°C)
            if 'main.temp' in self.date_for_years.columns:
                plt.plot(self.date_for_years.index, self.date_for_years['main.temp'], label='Temperature (°C)')
            else:
                logging.warning("'main.temp' column is missing in the data.")
            # Plot wind speed (m/s)
            if 'wind.speed' in self.date_for_years.columns:
                plt.plot(self.date_for_years.index, self.date_for_years['wind.speed'], label='Wind Speed (m/s)')
            else:
                logging.warning("'wind.speed' column is missing in the data.")
            # Plot humidity (%)
            if 'main.humidity' in self.date_for_years.columns:
                plt.plot(self.date_for_years.index, self.date_for_years['main.humidity'], label='Humidity (%)')
            else:
                logging.warning("'main.humidity' column is missing in the data.")
            # Setting plot aesthetics
            plt.xlabel('Date')
            plt.ylabel('Values')
            plt.title('All-Year Temperature, Wind Speed, and Humidity (Metric Units)')
            plt.legend()
            plt.grid(True)
            plt.show()
            logging.info('Plot generated successfully.')
        except Exception as e:
            logging.error(f'An error occurred while plotting data: {e}')

    def plot_data(self) -> None:
        """Plot data for weather history."""
        plt.figure(figsize=PLOT_FIG_SIZE)
        self._plot_date_for_years_stats()

    def generate_pdf_report(self, filename: str) -> None:
        """Generate a PDF report."""
        pdf = FPDF()
        self._initialize_pdf(pdf, f'Weather History Report for {self.location}')
        plt.figure(figsize=PLOT_FIG_SIZE)
        logging.warning('PDF report generation is not implemented yet.')

    @staticmethod
    def _initialize_pdf(pdf: FPDF, title: str) -> None:
        """Initialize the PDF document."""
        pdf.add_page()
        pdf.set_font('Arial', size=12)
        pdf.cell(200, 10, txt=title, ln=True, align='C')
        pdf.set_font('Arial', size=10)
        pdf.multi_cell(0, 10, txt='This report contains weather history analytics for the past 30 years.')
