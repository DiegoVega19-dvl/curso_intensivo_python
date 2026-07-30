favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'eduardo': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for nombre, lenguaje in favorite_languages.items():
    print(f'el lenguaje favorito de {nombre.title()}')
    for lenguage in lenguaje:
        print(lenguage)


person = {
    'first_name': 'juan',
    'last_name': 'vega',
    'city': 'La Paz'
}

print('la persona se llama', person['first_name'])
print('se apellida', person['last_name'])
print('y vive en', person['city'])


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f'key:{key}')
    print(f'value:{value}')
