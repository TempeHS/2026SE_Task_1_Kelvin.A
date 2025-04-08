import csv
import sys

user = input('Enter a num: 1. Login, 2. Register, 3. Quit: ')

logins = []
detail = []

if user == '1':
    with open('details.csv') as details:
        reader = csv.DictReader(details)
        for row in reader:
            logins.append({'user': row['user'], 'password': row['password']})





