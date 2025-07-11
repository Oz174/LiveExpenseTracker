import gspread
from google.oauth2.service_account import Credentials

# Define scopes and sheet name
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/drive.readonly'
]

SHEET_NAME = "Expenses and Targets"  # Replace with your actual Google Sheet name

def get_sheet_data():
    # Authenticate using credentials.json
    creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
    client = gspread.authorize(creds)

    # Open the spreadsheet and get worksheets
    sheet = client.open(SHEET_NAME)

    # Get all expense rows (skip header)
    ranges = ["Expenses!A2:C20", "Targets!A1:B2"]
    data = sheet.values_batch_get(ranges)
    expenses = data['valueRanges'][0]['values']
    targets_raw = data['valueRanges'][1]['values']

    current_remaining = float(targets_raw[0][1])
    target_remaining = float(targets_raw[1][1])

    return expenses, current_remaining, target_remaining
