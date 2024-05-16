# TIPE
TIPE project of airplane flight simulation


IRL :
 - Terre modéliser par le modèle WGS84 (modelisation sphère applatie (ellipsoïde), vitesse angulaire, masse, pesanteur terrestre) (France système courant : RGF93, ex : "coo GPS" lattitude, longitude, altitude en WGS84).
 - Trajet le plus court -> Orthodromie (géométrie non euclidienne) et non Loxodromique.
 - Taxe (redevance aéronautique) -> ne pas passer sur un tout petit bout d'un pays (taxe de survol)
 - réglementation etops -> champs d'action avion (temps maximum par rapport à un endroit d'atterissage sûr) (ex : A350 etops de 350 min)
 - carburant -> coût : 1 T = 1 000 €, 5 - 8 T / h selon avion (donc -de tps = + d'argent)
 - nous représenterons dans le code l'infini par inf du module numpy

Members : 
- Mathias HATEAU
- Corentin DOMENICHINI

Sources :
- [insérer des sources ici de site internet + livres.]
- M. Martin (pilote d'avions Air France).

### Windows
    - Installez [python3](https://www.python.org/downloads/windows/).
    *NB : Normalement, les header python.h et pip sont installés en meme temps.*

    - Installez le système de build python et les dépendances :

      `python.exe -m pip install --upgrade build "cython @ git+https://github.com/cython/cython" setuptools pyside6`

## Licence
Ce programme et son code source sont disponibles sous les termes de la licence GNU General Public License version 3 or later (GPLV3+), 
lisez le fichier LICENSE (en anglais), sa traduction francaise dans le fichier LICENCE_FR ou référez-vous à https://www.gnu.org/licenses/ pour plus de détails.

Les textes de présentations et de documentation (tel que ce README.md) sont disponibles sous la licence [Creative Common Attribution-ShareAlike (CC-BY-SA)](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

Problème pull :
  git config pull.rebase false
  git config pull.rebase true
  git config pull.ff only
  git merge --no-ff

### Problématique
Thème 2025 :  transition, transformation, conversion

Comment organiser et optimiser la planification d'un traffic aérien ?
  Pour plusieurs avions :
    -> optimiser la moyenne des [ (temps de parcours) / (temps optimal (avion seul)) ] / (nombre d'avions)
  > Pour cela test plusieurs algorithmes
   - Dijkstra
   - Bellman-Ford (mieux)
  Départ sur une base de Bellman-Ford, recherche avec implémentation des etops. Ainsi qu'augmentation du nombre d'avions -> standby si pas possible d'avancer.
  