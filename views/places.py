import pandas as pd
from setup_google_sheets import get_google_sheet

class PlacesToVisit:
    def __init__(self):
        
        self.sheet = get_google_sheet()
        self.places = self.load_places_from_sheet()
        
    def load_places_from_sheet(self):
        data = self.sheet.get_all_records()
        return pd.DataFrame(data)
    
    def add_place(self, name,location, description, category):
        self.sheet.append_row([name, location, description, category, False])
        self.places = self.load_places_from_sheet()
        
    def remove_place(self, name):
        cell = self.sheet.find(name)
        if cell:
            self.sheet.delate_row(cell.row)
        self.places = self.load_places_from_sheet()
        
    def update_places(self, name, **kwargs):
        cell = self.sheet.find(name)
        if cell:
            for key, value in kwargs.items():
                col = self.places.columns.get_loc(key) +1
                self.sheet.update_cell(cell.row, col, value)
        self.places = self.load_places_from_sheet()
        
    def list_places(self):
        return self.places
    
    def search_places(self, **kwargs):
        query_request = self.places
        for key, value in kwargs.items():
            query_result = query_result[query_result[key] == value]
        return query_result
    
    def mark_visited(self, name, visited=True):
        cell = self.sheet.find(name)
        if cell:
            self.sheet.update_cell(cell.row, 5, visited)
        self.places = self.load_places_from_sheet()