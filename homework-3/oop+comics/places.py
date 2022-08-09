from abc import ABC, abstractmethod


class Place(ABC):
    name = 'Tatooine'

    @abstractmethod
    def get_evil(self):
        print(f'Evil from {self.name}')


class Kostroma(Place):
    name = 'Kostroma'

    def get_evil(self):
        super().get_evil()
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = [0, 22.55, 25]

    def get_evil(self):
        super().get_evil()
        print('Godzilla stands near a skyscraper')


class Asgard(Place):
    name = 'Asgard'

    def get_evil(self):
        super().get_evil()
        print('Joker is now in Marvel')
