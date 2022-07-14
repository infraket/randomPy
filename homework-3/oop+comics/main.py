from heroes import Superman, SuperHero, News, JeanGrey, Deadpool
from places import Kostroma, Tokyo, Asgard
from random import choice


def save_the_place(hero: SuperHero, place=None):
    if place:
        place = place

    else:
        city = [Kostroma(), Tokyo(), Asgard()]
        place = choice(city)

    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    News.create_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Tokyo())
    print('-' * 20)
    save_the_place(JeanGrey())
    print('-' * 20)
    save_the_place(Deadpool())
    print('-' * 20)
    save_the_place(SuperHero('WonderWomen', True))
