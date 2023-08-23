## immigration_data.py

import requests
from typing import Dict

class ImmigrationData:
    """Class to fetch and provide New Zealand immigration data for the AI agent."""

    def __init__(self, url: str = "https://api.immigration.govt.nz"):
        """Initializes the ImmigrationData class with the URL of the data source."""
        self.url = url

    def get_data(self) -> Dict[str, str]:
        """Fetches the immigration data from the data source and returns it as a dictionary."""
        response = requests.get(self.url)
        data = response.json()
        return data

    def update_data(self) -> None:
        """Updates the immigration data by fetching the latest data from the data source."""
        self.data = self.get_data()
