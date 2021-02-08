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


print(max_population(["id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"]))