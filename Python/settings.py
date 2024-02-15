#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENSE
# encoding = utf8

import json
import os
from typing import *
from sys import *

settings: dict = {}
defaults: dict = {}

try:
    path: str = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(path, "../.vscode/default_settings.json")
    
    with open(path, 'r', encoding="utf-8") as setfile:
        defaults = json.load(setfile)
        
except Exception as e:
    print("no default_settings.json file, package should be réinstalled or permission checked, aborting", file=stderr)
    raise FileNotFoundError('default_settings.json')

if "--no-settings" in argv:
    print("Using only default settings")
    
else:
    path: str = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(path, "../.vscode/settings.json")
    
    try:
        with open(path, 'r', encoding="utf-8") as setfile:
            settings = json.load(setfile)
            
    except:
        print("inexistant or ill-formated settings.json file, using defaults settings only")

