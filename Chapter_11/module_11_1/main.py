import os
from dotenv import load_dotenv
from weather_app.weather import Weather
from weather_app.location_weather import LocationWeatherPoint
from weather_app.weather_history import WeatherHistory

load_dotenv()


def main():
    API_KEY = os.getenv('API_KEY')
    if not API_KEY:
        raise ValueError('API key not found in environment variables')

    # Example usage
    targets = ['Moscow', 'New York', 'Tokyo']
    weather_ = Weather(api_key=API_KEY)
    weather_.get_weather_report(targets)

    location = LocationWeatherPoint(api_key=API_KEY, name='Los Angeles')
    weather_history = WeatherHistory(api_key=API_KEY, location=location)

    weather_history.fetch_weather_data()
    weather_history.generate_analytics()
    weather_history.plot_data()
    weather_history.generate_pdf_report('weather_report.pdf')


if __name__ == '__main__':
    main()
