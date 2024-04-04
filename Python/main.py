#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding=utf8

import sys
import os
from typing import NoReturn
import importlib
import affichage

def launch_app() -> NoReturn:
    sys.exit(affichage.app.exec())