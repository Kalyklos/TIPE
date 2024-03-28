#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding=utf8

import sys
from typing import NoReturn
import importlib

import os
sys.path.append(os.path.abspath("/home/mat/Documents/MP2I/INFO/TIPE/Python/affichage"))
importlib.import_module("affichage")

def launch_app() -> NoReturn:
    sys.exit(affichage.app.exec())