# Importing the modules
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

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

# Each row is a separate list
header = sheet.get("A1:I1")
body = sheet.get("A2:I6")

# print(header)
# print(body)

# Calling another Google sheet
file = gspread.authorize(creds)
workbook2 = file.open("TMS - Timetable Sub")

sheet2 = workbook2.get_worksheet(0)
sheet2.clear()

sheet2.update('A1:I1', header)
sheet2.update('A2:I6', body)

# sheet2.update(value=[header], range_name="Header")
# sheet2.update(value=[body], range_name="Body")

header2 = sheet2.get("A1:I1")
body2 = sheet2.get("A2:I6")

# print(header2)
# print(body2)

fh = open("Checkbox_State.json", "r")
teacher_state = json.load(fh)

ateacher = []
for k in teacher_state:
    avalues = (teacher_state[k])
    if avalues == 'Absent':
        ateacher.append(k)

print(ateacher)

fn = open("Subject.json", "r")
subjects = json.load(fn)

sub = []
for i in subjects:
    for o in ateacher:
        if i == o:
            sub.append(subjects[i])

print(sub)

# remove the subs from gsheetsub and add random sub
