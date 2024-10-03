import os

import numpy as np
import pandas as pd

from dotenv import load_dotenv

from weather_app.analytics_generator import AnalyticsGenerator
from weather_app.data_plotter import DataPlotter
from weather_app.pdf_report_generator import PDFReportGenerator
from weather_app.data_saver import DataSaver
from weather_app.weather_data_fetcher import WeatherDataFetcher
from weather_app.weather import Weather
from weather_app.location_weather import LocationWeatherPoint

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

    # Fetch weather data
    fetcher = WeatherDataFetcher(API_KEY, location)
    raw_data = fetcher.fetch_weather_data()

    # Save data to CSV
    DataSaver.save_to_csv(raw_data, 'weather_data.csv')

    # Generate analytics
    analytics_generator = AnalyticsGenerator(raw_data)
    analytics = analytics_generator.generate_analytics()

    # Plot data
    plotter = DataPlotter(analytics_generator.date_for_years)
    plotter.plot_data()

    # Generating some dummy weather data
    dates = pd.date_range(start='2023-01-01', periods=100)
    temperatures = np.random.normal(loc=20, scale=5, size=len(dates))
    weather_data = pd.DataFrame({'Date': dates, 'Temperature': temperatures})

    # Generate PDF report
    PDFReportGenerator.generate_pdf_report('weather_report.pdf', 'Sample Location', weather_data)


if __name__ == '__main__':
    main()
