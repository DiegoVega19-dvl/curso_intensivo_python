
def city_country(city, country):
    country_city = f'"{city}, {country}"'
    return country_city.title()


print(city_country("la paz", "mexico"))
print(city_country("hermosillo", "mexico"))
print(city_country("bogota", "colombia"))


def make_album(artist_name, album_title, number_songs=None):
    artist = {'name': artist_name,
              'album': album_title, 'number_songs': number_songs}
    return artist


print(make_album("michael jackson", "bad"))
print(make_album("michael jackson", "xscape", 10))
print(make_album("michael jackson", "invencible", 10))
