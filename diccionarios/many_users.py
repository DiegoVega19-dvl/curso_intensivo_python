users = {
    'juan': {
        'fisrt_name': 'juan',
        'last_name': 'vega',
        'location': 'La paz'
    },
    'perez': {
        'fisrt_name': 'sergio',
        'last_name': 'perez',
        'location': 'guadalajara'
    }
}

for user, user_info in users.items():
    print(f'usuario: {user}')
    full_name = f"{user_info['fisrt_name']} {user_info['last_name']}"
    location = user_info['location']

    print(f'\tnombre completo: {full_name}')
    print(f'\tubicacion: {location}')
