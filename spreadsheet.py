import gspread, pprint, scraper, settings, time
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import scraper
import time

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open(settings.SHEET).sheet1

# Print pretty looking data
pp = pprint.PrettyPrinter()
data = sheet.get_all_records()

# Add all information
sheet.insert_row(values=None, index=2)
sheet.update_cell(2, 1, time.strftime("%b %d, %Y"))
sheet.update_cell(2, 2, f'{scraper.wotd()[0]}: {scraper.wotd()[1]}')
sheet.update_cell(2, 3, scraper.qe()[0])
sheet.update_cell(2, 4, scraper.ff())
sheet.update_cell(2, 5, scraper.dp())
sheet.update_cell(2, 6, scraper.pfst()[0])
sheet.update_cell(2, 7, scraper.otd())
sheet.update_cell(2, 8, scraper.news()[0])