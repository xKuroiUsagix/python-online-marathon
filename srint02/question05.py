import re


def max_population(data: list) -> tuple:
    max_pop, max_city = 0, ''
    pattern = r'([a-z]+\_[a-z]+|\d{5})'
    for line in data[1:]:
        city_population = re.findall(pattern, line)
        if int(city_population[1]) > max_pop:
            max_pop = int(city_population[1])
            max_city = city_population[0]

    return max_city, max_pop