
def city_country(city, name, population=""):
    if population:
        full_city = f"{city}, {name} - poblacion {population}"
        return full_city.title()
    else:
        full_city = f"{city}, {name}"
        return full_city.title()
