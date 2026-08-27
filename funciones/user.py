

# funcion con cantidad arbitraria de argumentos

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'juan', 'vega', location='la paz', profesion='programador')


print(user_profile)
