usernames = ['admin', 'juan', 'paco', 'maria', 'pedro']


if usernames:
    for username in usernames:
        if username == 'admin':
            print('hello admin, would you like to see a status report?')
        else:
            print(f'Hello {username}, thank you for login again!')
else:
    print("We need to find some users")
