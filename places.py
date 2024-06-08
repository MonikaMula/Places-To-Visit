import pandas as pd
from setup_google_sheets import get_google_sheet

class PlacesToVisit:
    REQUIRED_COLUMNS = {'Name', 'Location', 'Description', 'Category', 'Visited'}

    def __init__(self):
        print("Initializing PlacesToVisit...")
        self.sheet = get_google_sheet()
        print("Google Sheet accessed successfully.")
        self.places = self.load_places_from_sheet()

    def load_places_from_sheet(self):
        print("Loading places from sheet...")
        data = self.sheet.get_all_records()
        if not data:
            print("No data found in the sheet.")
        else:
            columns = set(data[0].keys())
            print("Columns:", columns)
            if not self.REQUIRED_COLUMNS.issubset(columns):
                missing_columns = self.REQUIRED_COLUMNS - columns
                raise ValueError(f"Missing columns in the sheet: {missing_columns}")
            print("Data loaded successfully.")
            # print("Data:", data)
        return pd.DataFrame(data)

    def add_place(self, name, location, description, category):
        self.sheet.append_row([name, location, description, category, False])
        self.places = self.load_places_from_sheet()

    def remove_place(self, name):
        cell = self.sheet.find(name)
        if cell:
            self.sheet.delete_rows(cell.row)
        self.places = self.load_places_from_sheet()

    def update_place(self, name, **kwargs):
        cell = self.sheet.find(name)
        if cell:
            for key, value in kwargs.items():
                col = self.places.columns.get_loc(key) + 1
                self.sheet.update_cell(cell.row, col, value)
        self.places = self.load_places_from_sheet()

    def list_places(self):
        return self.places

    def search_places(self, **kwargs):
        query_result = self.places
        for key, value in kwargs.items():
            query_result = query_result[query_result[key] == value]
        return query_result

    def mark_visited(self, name, visited=True):
        cell = self.sheet.find(name)
        if cell:
            self.sheet.update_cell(cell.row, 5, visited)
        self.places = self.load_places_from_sheet()


if __name__ == "__main__":
    print("Starting test...")
    manager = PlacesToVisit()
    print("Listing places...")
    print(manager.list_places())

