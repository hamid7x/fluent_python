lax_coordinates = (33.9425, -118.408056)
print(lax_coordinates)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
print(city, year, pop, chg, area)
traveler_ids = [('USA', 31195855), ('BRA', 'CE342567'), ('ESP', 'XDA20586')]
for passport in traveler_ids:
    print("%s/%s" % passport)
for country, _ in traveler_ids:
    print(country)
    