from pprint import pprint
import requests
from typing import Dict, Any


class Location:
    BASE_URL = "https://api.tomorrow.io/v4/locations?"

    def __init__(self, **kwargs):
        self.api_key = kwargs.get('api_key', None)
        try:
            self.__raw_data = self._validate_and_get_location_details(**kwargs)
        except ValueError as e:
            print(e)
            self.__raw_data = {}

    def _validate_and_get_location_details(self, **kwargs) -> Dict[str, Any]:
        if 'name' in kwargs:
            return self._find_by_name(kwargs['name'])
        elif 'latitude' in kwargs and 'longitude' in kwargs:
            return self._find_by_coordinates(kwargs['latitude'], kwargs['longitude'])
        else:
            raise ValueError("Either 'name' or 'latitude' and 'longitude' must be provided")

    def _find_by_name(self, _name_to_search: str) -> Dict[str, Any]:
        params = {
            'name': _name_to_search,
            'apikey': self.api_key
        }
        response = requests.get(self.BASE_URL + '/', params=params)
        response.raise_for_status()
        return response.json()

    def _find_by_coordinates(self, _lat: float, _lon: float) -> Dict[str, Any]:
        params = {
            'lat': _lat,
            'lon': _lon,
            'apikey': self.api_key
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()


# Example usage
def main():
    api_key = '2BvHDotVS5UZNsYGl6NuNvOZPkOnyvPo'
    location = Location(api_key=api_key, name='Moscow')
    pprint(location.__dict__)


# Run the example
if __name__ == "__main__":
    main()
