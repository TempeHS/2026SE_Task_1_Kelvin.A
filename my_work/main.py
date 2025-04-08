import csv

## Input user for 1,2,3 options
user = input('Enter a num: 1. Login, 2. Register, 3. Quit: ')

logins = []
with open('details.csv') as details:
    reader = csv.DictReader(details)
    for row in reader:
        logins.append({'user': row['user'], 'password': row['password']})

if user == '1':
    try:
        detail = input('what is up (u,p): ')
        a = detail.split(',')
        user,password = a[0], a[1]
        simple = user,password
        if simple in logins:
            print('logged in')
        else:
            print('boo')
    except IndexError:
        print('in format of "username,password"')
        


if user == '2':
    new = input("new username and password? (A,B): ").split(',')
    user_2,password_2 = new[0], new[1]
    userS = new[0], new[1]
    print(userS)
















