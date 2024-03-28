#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding=utf8

import sys
import os
from typing import NoReturn
import importlib

try:
    from affichage import *
except ModuleNotFoundError as e:
    print("Problème avec l'affichage.", file=stderr)
    raise e

def launch_app() -> NoReturn:
    sys.exit(app.exec())