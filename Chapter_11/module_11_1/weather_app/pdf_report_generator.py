import matplotlib.pyplot as plt
import logging
from fpdf import FPDF
import pandas as pd

# Constants
PLOT_FIG_SIZE = (10, 6)


class PDFReportGenerator:

    @staticmethod
    def generate_pdf_report(filename: str, location: str, weather_data: pd.DataFrame) -> None:
        """Generate a PDF report based on provided weather data."""
        pdf = FPDF()
        PDFReportGenerator._initialize_pdf(pdf, f'Weather History Report for {location}')

        # Example: Analytics - average temperature
        average_temp = weather_data['Temperature'].mean()
        logging.info(f'Average temperature: {average_temp}')

        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Average Temperature: {average_temp:.2f}", ln=True)

        # Plotting temperature data
        plt.figure(figsize=PLOT_FIG_SIZE)
        plt.plot(weather_data['Date'], weather_data['Temperature'], label='Temperature')
        plt.xlabel('Date')
        plt.ylabel('Temperature')
        plt.title('Temperature Over Time')
        plt.legend()
        plt.grid(True)
        plt.savefig('temperature_plot.png')
        plt.close()

        # Adding plot to the PDF
        pdf.add_page()
        pdf.image('temperature_plot.png', x=10, y=8, w=190)

        # Output the PDF file
        pdf.output(filename)

    @staticmethod
    def _initialize_pdf(pdf: FPDF, title: str) -> None:
        """Initialize PDF with title and basic settings."""
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(200, 10, txt=title, ln=True, align='C')
