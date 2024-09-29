from typing import List, Dict, Any
from rich.console import Console
from rich.table import Table
from datetime import datetime
from .location_weather import LocationWeatherPoint


class Weather:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.console = Console()

    def get_weather_report(self, targets: List[str]):
        for target in targets:
            location = LocationWeatherPoint(api_key=self.api_key, name=target)
            weather_data = location.get_weather_details()
            self.console.print(f'[bold yellow]Weather for {target}[/bold yellow]')
            self._print_current_weather(weather_data)
            self._print_three_day_forecast(weather_data)

    def _print_current_weather(self, data: Dict[str, Any]):
        current = data.get('current', {})
        table = Table(title='[cyan]Current Weather[/cyan]')
        table.add_column('Description')
        table.add_column('Temperature (°C)')
        table.add_column('Humidity (%)')
        table.add_column('Wind Speed (m/s)')
        table.add_row(
            f'[blue]{current.get("weather", [{}])[0].get("description", "N/A")}[/blue]',
            f'[red]{current.get("temp", "N/A")}[/red]',
            f'[green]{current.get("humidity", "N/A")}[/green]',
            f'[magenta]{current.get("wind_speed", "N/A")}[/magenta]'
        )
        self.console.print(table)

    def _print_three_day_forecast(self, data: Dict[str, Any]):
        daily = data.get('daily', [])
        table = Table(title='[cyan]3-Day Forecast[/cyan]')
        table.add_column('Date')
        table.add_column('Description')
        table.add_column('Max Temp (°C)')
        table.add_column('Min Temp (°C)')
        for day in daily[:3]:
            date = datetime.fromtimestamp(day.get('dt', 0)).strftime('%Y-%m-%d')
            table.add_row(
                f'[yellow]{date}[/yellow]',
                f'[blue]{day.get("weather", [{}])[0].get("description", "N/A")}[/blue]',
                f'[red]{day.get("temp", {}).get("max", "N/A")}[/red]',
                f'[green]{day.get("temp", {}).get("min", "N/A")}[/green]'
            )
        self.console.print(table)

    def __str__(self) -> str:
        return f"Weather(API Key: {'*' * len(self.api_key)})"

    def __repr__(self) -> str:
        return f"Weather(api_key={'*' * len(self.api_key)})"
