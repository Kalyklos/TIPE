import sys
import traceback
from typing import *
from math import *

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

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


