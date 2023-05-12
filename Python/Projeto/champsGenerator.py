from random import choice
import cassiopeia as cass


def champs():
    champions = cass.get_champions(region="BR")
    random_champion = choice(champions)
    return random_champion


campeao = champs()


def titleChamps():
    title = campeao.title
    return title


def nameChampion():
    nomeCampeao = campeao.name
    return nomeCampeao



