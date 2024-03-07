#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding=utf8

import sys
from typing import NoReturn

import affichage as aff

def launch_app() -> NoReturn:
    sys.exit(aff.app.exec())