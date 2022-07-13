from typing import Union
from heroes import Superman, SuperHero, News, JeanGrey, Deadpool
from places import Kostroma, Tokyo, Asgard


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo], news: News):
    hero.find(place)
    hero.evil(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    news.create_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), News())
    print('-' * 20)
    save_the_place(JeanGrey(), Tokyo(), News())
    print('-' * 20)
    save_the_place(Deadpool(), Kostroma(), News())
    print('-' * 20)
    save_the_place(SuperHero('WonderWomen', True), Asgard(), News())
    print('-' * 20)


