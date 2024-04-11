#  Code sous licence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8

# référencement de différents aéroports (sommets du graphe) représenté par des classes

import sys
import traceback
from typing import *
from math import *
from numpy import *

from settings import *

class Airport:
    # to do : ajout des poids entres différents sommets.
    """Classe régissant les aéroports (noeuds)"""
    def __init__(self, nb_runway, id):
        self.nb_runway = nb_runway
        self.f_runway = self.nb_runway
        self.link = []
        self.id = id
        self.nb_boulangeries = 0
    def is_free (self):
        """Vérifie si une piste est libre.

        Returns:
            bool: True s'il reste une piste de libre, False sinon.
        """
        if self.f_runway > 0:
            return True
        return False
    def add_boulangerie(self) :
        self.nb_boulangeries += 1
    def take_runway(self):
        """Réserve une piste.
        """
        self.f_runway -= 1
    def free_runway(self):
        """Libère une piste réservé.
        """
        self.f_runway +=1
    def add_link (self, other_airport):
        """Rajoute un aeroport à la liste des aéroport avec une connection direct

        Args:
            other_airport (aeroport.Airport): Autre aéroport de la classe Airport du même fichier.
        """
        self.link.append(other_airport)
    def link_with (self):
        """renvoie la liste des aéroports avec une connection directe.

        Returns:
            list: liste python contenant les aéroports liés.
        """
        return self.link    