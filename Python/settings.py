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

def get(setloc: str) -> Any:
    path: list[str]=setloc.split('.')
    
    try:
        temp = settings
        for key in path:
            temp = temp[key]
        return temp
    
    except (KeyError, TypeError):
        try:
            temp = defaults
            for key in path:
                temp = temp[key]
            return temp
        
        except:
            print("No setting found for ", setloc, file=stderr)
            return None


def set(setloc: str, value) -> bool:
    """Définit les paramètres 'setloc' à la valeur value.

    Args:
        setloc (str): Paramètre à mettre à jour, un fichier. Permit de séparer par groupe (par exemple "group.sub.setting")
        value (any): La nouvelle valeur du paramètre, doit être représentable en json

    Returns:
        bool: if the update was sucessful
    """
    temp = settings
    path: list[str]=setloc.split('.')
    
    for key in path[:-1]:
        if type(temp) is not dict:
            print("setting path to non dict, abborting", file=stderr)
            return False
        
        if key not in temp:
            temp[key] = {}
        temp = temp[key]
        
    temp[path[-1]] = value
    
    return True


def save() -> bool:
    """Sauvegarde les changer dans settings.json

    Returns:
        bool: Si les changement on pu se faire
    """
    
    try:
        with open(path, 'w', encoding="utf-8") as setfile:
            json.dump(settings, setfile, indent=2)
            return True
        
    except Exception as e:
        print("Illegal setting for json representation or no write acess:", e, file=stderr)          
        return False