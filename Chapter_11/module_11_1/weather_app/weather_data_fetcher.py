import logging
import pandas as pd
import requests
from typing import Optional, Dict
from .location_weather import LocationWeatherPoint

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Constants
API_URL_TEMPLATE = 'https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&units=metric&appid={apikey}'


class WeatherDataFetcher:
    def __init__(self, api_key: str, location: Optional[LocationWeatherPoint]):
        self.api_key = api_key
        self.location = location

    def fetch_weather_data(self) -> pd.DataFrame:
        """Fetch weather data from the API and return as DataFrame."""
        if not self.api_key or not self.location:
            logging.error('API key or location not set.')
            return pd.DataFrame()
        response = requests.get(
            API_URL_TEMPLATE.format(lat=self.location.lat, lon=self.location.lon, apikey=self.api_key)
        )
        if response.status_code == 200:
            data = response.json()
            return self._process_weather_data(data)
        else:
            logging.error(f'Failed to fetch data: {response.status_code} {response.reason}')
            return pd.DataFrame()

    @staticmethod
    def _process_weather_data(data: Dict) -> pd.DataFrame:
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
