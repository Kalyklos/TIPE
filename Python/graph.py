#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8

import sys
import traceback
from typing import *
from math import *

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from . import settings
from . import aeroport
from . import avion



try:
    from PySide6.QtCore import *
    from PySide6.QtWidgets import *
    from PySide6.QtGui import *
    from random import *

    Signal()
except ModuleNotFoundError as e:
    print("le module PySide6 devrait être installé pour que ce programme puisse fonctionner, lisez README.md pour plus de détails", file=stderr)
    raise e

#on identifie les aéroports par les noeuds du graphe, en les modélisant par une matrice.
nom_noeud_graph = [] #on stockera les initiales des aéroports dans une list de str.
noeud_graph = [] #matrice référençant les liaisons entre aéroports, 

NY = aeroport.Airport(9)
print(NY.nb_runway)