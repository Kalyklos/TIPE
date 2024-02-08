# TIPE
TIPE project of airplane flight simulation


IRL :
 - Terre modéliser par le modèle WGS84 (modelisation sphère applatie (ellipsoïde), vitesse angulaire, masse, pesanteur terrestre) (France système courant : RGF93, ex : "coo GPS" lattitude, longitude, altitude en WGS84).
 - Trajet le plus court -> Orthodromie (géométrie non euclidienne) et non Loxodromique.
 - Taxe (redevance aéronautique) -> ne pas passer sur un tout petit bout d'un pays (taxe de survol)
 - réglementation etops -> champs d'action avion (temps maximum par rapport à un endroit d'atterissage sûr) (ex : A350 etops de 350 min)
 - carburant -> coût : 1 T = 1 000 €, 5 - 8 T / h selon avion (donc -de tps = + d'argent)

Members : 
- Mathias HATEAU
- Corentin DOMENICHINI

Special Thanks to :
- Bastien DURAIN
- Idriss ABERKANE


### Windows
    - Installez [python3](https://www.python.org/downloads/windows/).
    *NB : Normalement, les header python.h et pip sont installés en meme temps.*

    - Installez le système de build python et les dépendances :

      `python.exe -m pip install --upgrade build "cython @ git+https://github.com/cython/cython" setuptools pyside6`
