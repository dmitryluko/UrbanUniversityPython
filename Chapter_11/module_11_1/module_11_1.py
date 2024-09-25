from pprint import pprint
import requests
from typing import Dict, Any, Tuple
from typing import List
from rich.console import Console
from rich.table import Table


class Location:
    GEOCODING_API_URL = "http://api.openweathermap.org/geo/1.0/direct"
    ONE_CALL_API_URL = "https://api.openweathermap.org/data/3.0/onecall"

    def __init__(self, **kwargs):
        self.api_key = kwargs.get('api_key', None)
        self.__coordinates = {}
        self.__raw_data = {}
        try:
            self.__coordinates = self._validate_and_get_location_details(**kwargs)
            self.__raw_data = self.get_weather_details(**self.__coordinates)
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

    def get_weather_details(self, **coordinates) -> Dict[str, Any]:
        params = {
            'lat': coordinates['lat'],
            'lon': coordinates['lon'],
            'appid': self.api_key
        }
        response = requests.get(self.ONE_CALL_API_URL, params=params)
        response.raise_for_status()
        return response.json()


class Weather:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.console = Console()

    def get_weather_report(self, targets: List[str]):
        for target in targets:
            location = Location(api_key=self.api_key, name=target)
            weather_data = location.get_weather_details(**location._validate_and_get_location_details(name=target))

            self.console.print(f"[bold]Weather for {target}[/bold]")
            self._print_current_weather(weather_data)
            self._print_three_day_forecast(weather_data)

    def _print_current_weather(self, data: Dict[str, Any]):
        current = data.get('current', {})
        table = Table(title="Current Weather")

        table.add_column("Description")
        table.add_column("Temperature (°C)")
        table.add_column("Humidity (%)")
        table.add_column("Wind Speed (m/s)")

        table.add_row(
            current.get('weather', [{}])[0].get('description', 'N/A'),
            str(current.get('temp', 'N/A')),
            str(current.get('humidity', 'N/A')),
            str(current.get('wind_speed', 'N/A'))
        )

        self.console.print(table)

    def _print_three_day_forecast(self, data: Dict[str, Any]):
        daily = data.get('daily', [])
        table = Table(title="3-Day Forecast")

        table.add_column("Day")
        table.add_column("Description")
        table.add_column("Max Temp (°C)")
        table.add_column("Min Temp (°C)")

        for i, day in enumerate(daily[:3]):
            table.add_row(
                f"Day {i + 1}",
                day.get('weather', [{}])[0].get('description', 'N/A'),
                str(day.get('temp', {}).get('max', 'N/A')),
                str(day.get('temp', {}).get('min', 'N/A'))
            )

        self.console.print(table)


# Update `main` function to demonstrate the Weather class usage:
def main():
    api_key = '088762ed0e87d25d2afadf68da481fe2'
    targets = ['Moscow', 'New York', 'Tokyo']
    weather = Weather(api_key=api_key)
    weather.get_weather_report(targets)
    pass



# Run the example
if __name__ == "__main__":
    main()
