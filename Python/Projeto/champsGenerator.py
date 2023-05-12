from random import choice

import cassiopeia as cass

cass.set_riot_api_key(
    "RGAPI-e0e28fc7-d63b-436b-a8cf-8d0a97f7b2cf")  


def champs():
    champions = cass.get_champions(region="BR")
    random_champion = choice(champions)
    return random_champion.name

