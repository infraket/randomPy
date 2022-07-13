from abc import abstractmethod

from antagonistfinder import AntagonistFinder


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def evil(self, place):
        self.finder.get_evil(place)

    @abstractmethod
    def attack(self):
        pass

    def ultimate(self):
        pass


class Gun:

    @staticmethod
    def fire_a_gun():
        print('PIU PIU')


class Laser:
    @staticmethod
    def incinerate_with_lasers():
        print('Wzzzuuuup!')


class Kick:
    @staticmethod
    def roundhouse_kick():
        print('Bump')


class News:
    name = 'Hot News'

    @staticmethod
    def create_news(self, place):
        place_name = getattr(place, 'name', 'place')
        print(f'{self.name} saved the {place_name}!')


class JeanGrey(SuperHero, Gun):
    def __init__(self):
        super(JeanGrey, self).__init__('JeanGrey', True)

    def attack(self):
        self.fire_a_gun()


class Deadpool(SuperHero, Kick):
    def __init__(self):
        super(Deadpool, self).__init__('Deadpool', True)

    def attack(self):
        self.roundhouse_kick()


class Kryptoman(SuperHero, Laser):
    def attack(self):
        self.incinerate_with_lasers()

    def ultimate(self):
        if self.name == 'Clark Kent':
            self.incinerate_with_lasers()

    def evil(self, place):
        self.finder.get_evil(place)


class Superman(Kryptoman):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        return 'Kick'
