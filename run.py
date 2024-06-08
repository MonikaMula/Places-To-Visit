# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
import json
from google.oauth2.service_account import Credentials

# Define the scope for accessing Google Sheets and Google Drive
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

with open('creds.json') as f:
    creds_data = json.load(f)
    
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SPREADSHEET_ID = creds_data.get('spreadsheet_id')
if not SPREADSHEET_ID:
    raise ValueError("spreadsheet_id not found in creds.json")

try:
    SHEET = GSPREAD_CLIENT.open_by_key(SPREADSHEET_ID)
    PLACES_WORKSHEET = SHEET.sheet1
except gspread.SpreadsheetNotFound:
    print(f"Spreadsheet with id {SPREADSHEET_ID} not found.")
    raise

def get_google_sheet():
    return PLACES_WORKSHEET