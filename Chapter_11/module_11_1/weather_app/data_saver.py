import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Constants
CSV_INDEX = False


class DataSaver:
    @staticmethod
    def save_to_csv(df: pd.DataFrame, filename: str) -> None:
        """Save a DataFrame to a CSV file."""
        try:
            df.to_csv(filename, index=CSV_INDEX)
            logging.info(f'Data saved to {filename}.')
        except Exception as e:
            logging.error(f'Failed to save data to CSV: {e}')
