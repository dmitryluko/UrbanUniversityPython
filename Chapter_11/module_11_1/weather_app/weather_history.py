import pandas as pd
import requests
import matplotlib.pyplot as plt
import logging
from typing import Optional, Dict

from fpdf import FPDF
from .location_weather import LocationWeatherPoint

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

API_URL_TEMPLATE = 'https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&appid={apikey}'
CSV_INDEX = False
PLOT_FIG_SIZE = (10, 6)


class WeatherHistory:
    def __init__(self, api_key: str, location: Optional[LocationWeatherPoint] = None):
        self.api_key = api_key
        self.location = location

        self.daily_mean: pd.Series = pd.Series()
        self.monthly_mean: pd.Series = pd.Series()
        self.yearly_mean: pd.Series = pd.Series()
        # self.month_by_year: pd.DataFrame = pd.DataFrame()
        # self.year_by_month: pd.DataFrame = pd.DataFrame()
        # self.year_by_day: pd.DataFrame = pd.DataFrame()
        # self.day_by_year: pd.DataFrame = pd.DataFrame()

        self._raw_data: pd.DataFrame = pd.DataFrame()

    def fetch_weather_data(self):
        if not self.api_key or not self.location:
            logging.error('API key or location not set.')
            return
        response = requests.get(
            API_URL_TEMPLATE.format(lat=self.location.lat, lon=self.location.lon, apikey=self.api_key))
        if response.status_code == 200:
            data = response.json()
            self._raw_data = self.process_weather_data(data)
        else:
            logging.error(f'Failed to fetch data: {response.status_code} {response.reason}')

    @staticmethod
    def process_weather_data(data: Dict) -> pd.DataFrame:
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
        self._save_dataframe_to_csv(self._raw_data, filename)

    @staticmethod
    def _save_dataframe_to_csv(df: pd.DataFrame, filename: str) -> None:
        try:
            df.to_csv(filename, index=CSV_INDEX)
            logging.info(f'Data saved to {filename}.')
        except Exception as e:
            logging.error(f'Failed to save data to CSV: {e}')

    def generate_analytics(self):
        logging.info('Generating analytics...')
        if self._raw_data.empty:
            logging.warning('No data to generate analytics.')
            return
        self.daily_mean = self._get_mean_series(self._raw_data, 'D')
        self.monthly_mean = self._get_mean_series(self._raw_data, 'ME')
        self.yearly_mean = self._get_mean_series(self._raw_data, 'YE')
        logging.info('Analytics generated.')

    @staticmethod
    def _get_mean_series(df: pd.DataFrame, freq: str) -> pd.Series:

        if 'main.temp' not in df.columns:
            logging.warning("'main.temp' column is missing in the data.")
            return pd.Series()

        try:
            mean_series = df.resample(freq)['main.temp'].mean()
            logging.info(f'Mean series computed with frequency "{freq}".')
            return mean_series
        except KeyError as e:
            logging.error(f'Column missing for resampling: {e}')
            return pd.Series()
        except Exception as e:
            logging.error(f'An error occurred during resampling: {e}')
            return pd.Series()

    def plot_data(self):
        plt.figure(figsize=PLOT_FIG_SIZE)
        self._plot_series(self.daily_mean, 'Daily Mean Temperature')
        self._plot_series(self.monthly_mean, 'Monthly Mean Temperature')
        self._plot_series(self.yearly_mean, 'Yearly Mean Temperature')
        plt.xlabel('Date')
        plt.ylabel('Temperature')
        plt.title(f'Temperature Trends Over 30 Years in {self.location}')
        plt.legend()
        plt.show()

    @staticmethod
    def _plot_series(series: pd.Series, label: str):
        if not series.empty:
            plt.plot(series.index, series.values, label=label)
            logging.info(f"Plotting '{label}'...")
        else:
            logging.warning(f"No data available for '{label}'.")

    def generate_pdf_report(self, filename: str):
        pdf = FPDF()
        self._initialize_pdf(pdf, f'Weather History Report for {self.location}')
        plt.figure(figsize=PLOT_FIG_SIZE)
        self._plot_series(self.yearly_mean, 'Yearly Mean Temperature')
        plt.xlabel('Date')
        plt.ylabel('Temperature')
        plt.title('Yearly Temperature Trends')
        plt.legend()
        plt.savefig('temp_plot.png')
        pdf.image('temp_plot.png', x=10, y=50, w=190)
        pdf.output(filename)
        logging.info(f'PDF report generated: {filename}')

    @staticmethod
    def _initialize_pdf(pdf: FPDF, title: str):
        pdf.add_page()
        pdf.set_font('Arial', size=12)
        pdf.cell(200, 10, txt=title, ln=True, align='C')
        pdf.set_font('Arial', size=10)
        pdf.multi_cell(0, 10, txt='This report contains weather history analytics for the past 30 years.')
