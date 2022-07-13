from places import Kostroma, Tokyo,Asgard
from abc import ABC, abstractmethod


class Place(ABC):

    @abstractmethod
    def get_evil(self, place):
        print(f'Evil from {place.name}')


class AntagonistFinder(Place):
    def get_evil(self, place):
        super().get_evil(place)

    @staticmethod
    def get_antagonist(place):

        if isinstance(place, Kostroma):

            place.get_orcs()
        elif isinstance(place, Tokyo):

            place.get_godzilla()
        elif isinstance(place, Asgard):

            place.get_joker()


