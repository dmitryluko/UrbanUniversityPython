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

    @staticmethod
    def __timestamp_to_day_month_year(ts: int) -> Tuple[int, int, int]:
        try:
            dt = pd.to_datetime(ts, unit='s')
            return dt.day, dt.month, dt.year
        except Exception as e:
            logging.error(f'Error converting timestamp to day, month, year: {e}')
            return 0, 0, 0

    def _get_date_stat_for_years(self, given_date: str) -> pd.DataFrame:
        if self._raw_data.empty:
            logging.warning('Raw data is empty. Cannot compute statistics.')
            return pd.DataFrame()

        try:
            given_date = pd.to_datetime(given_date)
        except Exception as e:
            logging.error(f'Invalid date provided: {e}')
            return pd.DataFrame()

        try:
            filtered_data = self._raw_data[
                self._raw_data.index.map(lambda x: (x.day, x.month)) == (given_date.day, given_date.month)
                ]

        except Exception as e:
            logging.error(f'An error occurred while filtering data: {e}')
            return pd.DataFrame()

        if filtered_data.empty:
            logging.warning('No data available for the given date across years.')
            return pd.DataFrame()

        logging.info(
            f'Statistics for the date {given_date.strftime("%Y-%m-%d")} across all years computed successfully.')
        return filtered_data

    def generate_analytics(self) -> None:
        logging.info('Generating analytics...')
        if self._raw_data.empty:
            logging.warning('No data to generate analytics.')
            return

        # self.daily_mean = self._get_mean_series(self._raw_data, 'D')
        # self.monthly_mean = self._get_mean_series(self._raw_data, 'M')
        # self.yearly_mean = self._get_mean_series(self._raw_data, 'Y')
        self.date_for_years = self._get_date_stat_for_years(pd.to_datetime('today').strftime('%m:%d'))
        logging.info('Analytics generated.')

    @staticmethod
    def _get_mean_series(df: pd.DataFrame, freq: str) -> pd.DataFrame:
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
        if self.date_for_years is not None and not self.date_for_years.empty:
            temperature_values = self.date_for_years['main_temp'].values
            date_index = self.date_for_years.index
            plt.plot(date_index, temperature_values,
                     label='Mean Temp for Given Date')
            plt.xlabel('Year')
            plt.ylabel('Temperature')
            plt.title('Mean Temperature for Given Date Across Years')
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            logging.warning('No data available to plot for the given date across years.')

    def plot_data(self) -> None:
        plt.figure(figsize=PLOT_FIG_SIZE)
        self._plot_date_for_years_stats()

    @staticmethod
    def _plot_series(series: pd.Series, label: str) -> None:
        if not series.empty:
            plt.plot(series.index, series.values, label=label)
            logging.info(f"Plotting '{label}'...")
        else:
            logging.warning(f'No data available for "{label}".')

    def generate_pdf_report(self, filename: str) -> None:
        pdf = FPDF()
        self._initialize_pdf(pdf, f'Weather History Report for {self.location}')
        plt.figure(figsize=PLOT_FIG_SIZE)
        # raise NotImplemented
        logging.warning('PDF report generation is not implemented yet.')

    @staticmethod
    def _initialize_pdf(pdf: FPDF, title: str) -> None:
        pdf.add_page()
        pdf.set_font('Arial', size=12)
        pdf.cell(200, 10, txt=title, ln=True, align='C')
        pdf.set_font('Arial', size=10)
        pdf.multi_cell(0, 10, txt='This report contains weather history analytics for the past 30 years.')
