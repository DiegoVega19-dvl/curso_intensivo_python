unconfirmed_users = ['juan', 'ana', 'pedro']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"confirmado usario: {current_user}")
    confirmed_users.append(current_user)


print("los siguientes usuarios han sido confirmados: ")
for users in confirmed_users:
    print(users.title())
