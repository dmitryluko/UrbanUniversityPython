from typing import Dict, Any, Tuple
import requests


class LocationWeatherPoint:
    GEOCODING_API_URL = 'http://api.openweathermap.org/geo/1.0/direct'
    ONE_CALL_API_URL = 'https://api.openweathermap.org/data/3.0/onecall'

    def __init__(self, api_key: str, name: str = '', latitude: float = None, longitude: float = None):
        self.api_key = api_key
        self.name = name
        self.__raw_data: Dict[str, Any] = {}
        self.__lat: float = None
        self.__lon: float = None
        try:
            self.__lat, self.__lon = self._validate_and_get_location_details(name=name, latitude=latitude,
                                                                             longitude=longitude)
            self.__raw_data = self.get_weather_details()
        except ValueError as e:
            print(e)

    def _validate_and_get_location_details(self, name: str = '', latitude: float = None, longitude: float = None) -> \
            Tuple[float, float]:
        if name:
            return self._find_by_name(name)
        elif latitude is not None and longitude is not None:
            return latitude, longitude
        else:
            raise ValueError("Either 'name' or 'latitude' and 'longitude' must be provided")

    def _find_by_name(self, city_name: str) -> Tuple[float, float]:
        params = {'q': city_name, 'appid': self.api_key}
        response = requests.get(self.GEOCODING_API_URL, params=params)
        response.raise_for_status()
        results = response.json()
        if not results:
            raise ValueError('City not found')
        return results[0]['lat'], results[0]['lon']

    @property
    def lat(self) -> float:
        return self.__lat

    @property
    def lon(self) -> float:
        return self.__lon

    def get_weather_details(self) -> Dict[str, Any]:
        params = {'lat': self.lat, 'lon': self.lon, 'appid': self.api_key, 'units': 'metric'}
        response = requests.get(self.ONE_CALL_API_URL, params=params)
        response.raise_for_status()
        return response.json()

    def __str__(self) -> str:
        return f"Location(Name: {self.name}, Coordinates: {self.__lat}, {self.__lon})"

    def __repr__(self) -> str:
        return f"Location(name={self.name!r}, coordinates=({self.__lat}, {self.__lon}), api_key={'*' * len(self.api_key)})"
