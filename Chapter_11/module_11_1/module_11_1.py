from pprint import pprint
import requests
from typing import Dict, Any, Tuple


class Location:
    GEOCODING_API_URL = "http://api.openweathermap.org/geo/1.0/direct"
    ONE_CALL_API_URL = "https://api.openweathermap.org/data/3.0/onecall"

    def __init__(self, **kwargs):
        self.api_key = kwargs.get('api_key', None)
        self.__coordinates = {}
        self.__raw_data = {}
        try:
            self.__coordinates = self._validate_and_get_location_details(**kwargs)
            self.__raw_data = self._get_weather_details(**self.__coordinates)
        except ValueError as e:
            print(e)
            self.__raw_data = {}

    def _validate_and_get_location_details(self, **kwargs) -> Dict[str, float]:
        if 'name' in kwargs:
            return self._find_by_name(kwargs['name'])
        elif 'latitude' in kwargs and 'longitude' in kwargs:
            return {'lat': kwargs['latitude'], 'lon': kwargs['longitude']}
        else:
            raise ValueError("Either 'name' or 'latitude' and 'longitude' must be provided")

    def _find_by_name(self, city_name: str) -> Dict[str, float]:
        params = {
            'q': city_name,
            'appid': self.api_key
        }
        response = requests.get(self.GEOCODING_API_URL, params=params)
        response.raise_for_status()
        results = response.json()
        if not results:
            raise ValueError("City not found")
        return {'lat': results[0]['lat'], 'lon': results[0]['lon']}

    def _get_weather_details(self, **coordinates) -> Dict[str, Any]:
        params = {
            'lat': coordinates['lat'],
            'lon': coordinates['lon'],
            'appid': self.api_key
        }
        response = requests.get(self.ONE_CALL_API_URL, params=params)
        response.raise_for_status()
        return response.json()


# Example usage
def main():
    api_key = '088762ed0e87d25d2afadf68da481fe2'
    location = Location(api_key=api_key, name='Moscow')
    pprint(location.__dict__)


# Run the example
if __name__ == "__main__":
    main()
