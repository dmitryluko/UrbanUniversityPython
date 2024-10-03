import logging
import pandas as pd
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Constants
DATE_FORMAT = "%m-%d"


class AnalyticsGenerator:
    def __init__(self, raw_data: pd.DataFrame):
        self.raw_data = raw_data
        self.date_for_years = None

    def generate_analytics(self) -> Dict[str, pd.DataFrame]:
        """Generate analytics data like daily, monthly, and yearly means."""
        logging.info('Generating analytics...')
        if self.raw_data.empty:
            logging.warning('No data to generate analytics.')
            return {}
        today = pd.to_datetime('today')
        self.date_for_years = self._years_by_date(today)
        return {
            'daily_mean': self._get_mean_series('D'),
            'monthly_mean': self._get_mean_series('ME'),
            'yearly_mean': self._get_mean_series('YE')
        }

    def _years_by_date(self, given_date: pd.Timestamp) -> pd.DataFrame:
        """Returns all data for the given date in all available years."""
        if self.raw_data.empty:
            logging.warning('No data available to filter.')
            return pd.DataFrame()
        try:
            month, day = given_date.month, given_date.day
            self.raw_data['month'], self.raw_data['day'] = self.raw_data.index.month, self.raw_data.index.day
            date_filtered_data = self.raw_data[
                (self.raw_data['month'] == month) &
                (self.raw_data['day'] == day)
                ].drop(columns=['month', 'day'])
            if date_filtered_data.empty:
                logging.warning(f'No data found for the given date: {given_date.strftime(DATE_FORMAT)}.')
            return date_filtered_data
        except Exception as e:
            logging.error(f'Error filtering data for given date {given_date.strftime(DATE_FORMAT)}: {e}')
            return pd.DataFrame()

    def _get_mean_series(self, freq: str) -> pd.DataFrame:
        """Compute mean values for specific frequency."""
        if 'main.temp' not in self.raw_data.columns:
            logging.warning("'main.temp' column is missing in the data.")
            return pd.DataFrame()
        try:
            mean_series = self.raw_data.resample(freq)['main.temp'].mean()
            logging.info(f'Mean series computed with frequency "{freq}".')
            return mean_series
        except KeyError as e:
            logging.error(f'Column missing for resampling: {e}')
            return pd.DataFrame()
        except Exception as e:
            logging.error(f'An error occurred during resampling: {e}')
            return pd.DataFrame()
