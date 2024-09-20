import aiohttp
import asyncio
from typing import Dict, Any


class Location:
    BASE_URL = "https://api.tomorrow.io/v4/locations?"

    def __init__(self, **kwargs):
        self.api_key = kwargs.get('api_key', None)
        try:
            self.__raw_data = asyncio.run(self._validate_and_get_location_details(**kwargs))
        except ValueError as e:
            print(e)
            self.__raw_data = {}


    async def _validate_and_get_location_details(self, **kwargs) -> Dict[str, Any]:
        if 'name' in kwargs:
            return await self._find_by_name(kwargs['name'])
        elif 'latitude' in kwargs and 'longitude' in kwargs:
            return await self._find_by_coordinates(kwargs['latitude'], kwargs['longitude'])
        else:
            raise ValueError("Either 'name' or 'latitude' and 'longitude' must be provided")

    async def _find_by_name(self, _name_to_search: str) -> Dict[str, Any]:
        params = {
            'name': _name_to_search,
            'apikey': self.api_key
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL, params=params) as response:
                response.raise_for_status()
                return await response.json()

    async def _find_by_coordinates(self, _lat: float, _lon: float) -> Dict[str, Any]:
        params = {
            'lat': _lat,
            'lon': _lon,
            'apikey': self.api_key
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL, params=params) as response:
                response.raise_for_status()
                return await response.json()


# Example usage
async def main():
    api_key = '2BvHDotVS5UZNsYGl6NuNvOZPkOnyvPo'
    location = Location(api_key, 'Moscow')

    # Finding by name
    try:
        location_details = await location._validate_and_get_location_details(name="Boston")
        print(location_details)
    except ValueError as e:
        print(e)
    except aiohttp.ClientResponseError as e:
        print(e)

    # Finding by coordinates
    try:
        location_details = await location._validate_and_get_location_details(latitude=42.3601, longitude=-71.0589)
        print(location_details)
    except ValueError as e:
        print(e)
    except aiohttp.ClientResponseError as e:
        print(e)


# Run the example
if __name__ == "__main__":
    asyncio.run(main())
