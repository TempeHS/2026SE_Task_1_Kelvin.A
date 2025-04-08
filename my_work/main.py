import csv
import sys

user = input('Enter a num: 1. Login, 2. Register, 3. Quit: ')

logins = []
detail = []
with open('details.csv') as details:
    reader = csv.DictReader(details)
    for row in reader:
        logins.append({'user': row['user'], 'password': row['password']})

if user == '1':
    details = input("what is your user and password? ")





elif user == '2':

elif user == '3':

else:








