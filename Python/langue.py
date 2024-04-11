#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENCE
# encoding = utf8
import json
import os
from Python.settings import *
from functools import partial

lang: dict = {}

path: str = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(path, "Langues/fr.json")  
with open(path, 'r', encoding="utf-8") as setfile:
    lang = json.load(setfile)


def get(setloc: str) -> str:
    path: list[str]=setloc.split('.')
    
    try:
        temp = lang
        for key in path:
            temp = temp[key]
        return temp
    except (KeyError):
        print("Il semblerait que cette clef n'existe pas dans le json",settings.get("affichage.langue"),"vous allez devoir la rajouter ou requérir l'assistance d'une personne compétente).")
        return lang["404"]

def reload() -> None :
    global lang
    path: str = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(path, "Langues/"+settings.get("affichage.langue")+".json")
    with open(path, 'r', encoding="utf-8") as setfile:
        lang = json.load(setfile)
        
def __lazyInternal(function : callable, setloc : str) -> None:
    function(get(setloc))

def lazyEval(function : callable, setloc : str) -> callable:
    return partial(__lazyInternal,function,setloc)