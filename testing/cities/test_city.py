from city_functions import city_country

def test_city_country():
    formatted_country = city_country('santiago', 'chile')
    assert formatted_country == 'Santiago, Chile'

def test_city_country_poulation():
    formatted_country = city_country('santiago', 'chile', 5000000)
    assert formatted_country == 'Santiago, Chile - Poblacion 5000000'