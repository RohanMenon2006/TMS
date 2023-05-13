# Importing the modules
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Code to give python access to Google sheets, (mandatory)
scope = {
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
}

creds = ServiceAccountCredentials.from_json_keyfile_name("secret_key.json", scopes=scope)

# Calling the Google sheet
file = gspread.authorize(creds)
workbook = file.open("TMS - Timetable")
# Change the number to select sheets sheet1 is 0 and sheet2 is 1 and so on
sheet = workbook.get_worksheet(0)

# # Each row is a separate list
# header = sheet.get("A1:I1")
# body = sheet.get("A2:I6")

# print(header)
# print(body)

file.copy("18Qk5bzuA7JOBD8CTgwvKYRiMl_35it5AwcFG2Bi5npo", title="timcard2", copy_permissions=True)

worksheet = file.open("timcard2")
worksheet.share("my_email@google.com", perm_type='user', role='writer')