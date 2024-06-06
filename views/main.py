import pandas as pd
from setup_google_sheets import get_google_sheet

class PlacesToVisit:
    def __init__(self)
        
        self.sheet = get_google_sheet()
        self.places = self.load_places_from_sheet()
        
    def load_places_from_sheet(self):
        data = self.sheet.get_all