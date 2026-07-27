'''alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# para remover una clave-valor de un diccionario (permanente)

del alien_0['points']

print(alien_0)'''

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print('...')

print(f'el numero total de aliens creados son: {len(aliens)}')
