import logging
import matplotlib.pyplot as plt
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Constants
PLOT_FIG_SIZE = (10, 6)


class DataPlotter:
    def __init__(self, date_for_years: pd.DataFrame):
        self.date_for_years = date_for_years

    def plot_data(self) -> None:
        """Plot data for weather history."""
        if self.date_for_years is None or self.date_for_years.empty:
            logging.warning('No data available to plot.')
            return
        try:
            plt.figure(figsize=PLOT_FIG_SIZE)
            self._plot_column('main.temp', 'Temperature (°C)')
            self._plot_column('wind.speed', 'Wind Speed (m/s)')
            self._plot_column('main.humidity', 'Humidity (%)')
            plt.xlabel('Date')
            plt.ylabel('Values')
            plt.title('All-Year Temperature, Wind Speed, and Humidity (Metric Units)')
            plt.legend()
            plt.grid(True)
            plt.show()
            logging.info('Plot generated successfully.')
        except Exception as e:
            logging.error(f'Error occurred while plotting data: {e}')

    def _plot_column(self, column: str, label: str) -> None:
        """Helper method to plot a single column."""
        if column in self.date_for_years.columns:
            plt.plot(self.date_for_years.index, self.date_for_years[column], label=label)
        else:
            logging.warning(f"'{column}' column is missing in the data.")
