#  Code sous liscence GPL3+. Plus de détail a <https://www.gnu.org/licenses/> ou dans le fichier LICENCE
# encoding = utf8

import sys
import os
import json
from sys import *
from math import *
from functools import *
# import des différentes librairies non-standard avec debug en cas de librairie manquante
try:
    from PySide6.QtCore import *
    from PySide6.QtWidgets import *
    from PySide6.QtGui import *
    Signal()
except ModuleNotFoundError as e:
    print("le module PySide6 devrait être installé pour que ce programme puisse fonctionner, lisez README.md pour plus de détails", file=stderr)
    raise e

from Python.settings import *
import Python.langue as langue
app: QApplication = QApplication(sys.argv)

class Main_window(QMainWindow):
    """Cette classe définit la fenêtre principale du programme, à partir d'un QWidget."""
    changeLangSignal : Signal = Signal()
    
    def __init__(self) -> None:
        super().__init__()
        self.setFocusPolicy(Qt.ClickFocus)
        self.affichage_controles: bool = True

        self.setWindowTitle(langue.get("title"))        
        #style

        self.change_theme()
        self.layout: QLayout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addSpacing(10)

        # Création des actions utiliseables dans les menus
        self.attach_detachAction: QAction = QAction(langue.get("menu.display.detach"), self)
        self.attach_detachAction.triggered.connect(self.attach_detach_controles)
        self.changeLangSignal.connect(self.attach_detach_texte)
        self.langAction: list(QAction) = []
        for speak in (("Français","fr")):
            self.langAction.append(QAction(speak[0], self))
            self.langAction[-1].triggered.connect(partial(self.change_lang,speak[1]))
        
        self.themeAction: list(QAction) = []
        for theme in ("light","dark","system"):
            self.themeAction.append(QAction(langue.get("menu.settings.theme."+theme), self))
            self.changeLangSignal.connect(langue.lazyEval(self.themeAction[-1].setText,"menu.settings.theme."+theme))
            self.themeAction[-1].triggered.connect(partial(self.change_theme,theme))

        self.licenseAction: QAction = QAction(langue.get("menu.help.license"), self)
        self.changeLangSignal.connect(langue.lazyEval(self.licenseAction.setText,"menu.help.license"))
        self.licenseAction.triggered.connect(self.affich_licence)

        # Création des menus
        self.menuBar: QWidget = QMenuBar(self)
        self.menuBar.setFixedWidth(self.size().width())

        self.affichageMenu: QMenu = QMenu(langue.get("menu.display.title"), self.menuBar)
        self.changeLangSignal.connect(langue.lazyEval(self.affichageMenu.setTitle,"menu.display.title"))
        self.menuBar.addMenu(self.affichageMenu)
        self.affichageMenu.addAction(self.attach_detachAction)
        
        self.configMenu : QMenu = QMenu(langue.get("menu.settings.title"), self.menuBar)
        self.changeLangSignal.connect(langue.lazyEval(self.configMenu.setTitle,"menu.settings.title"))
        self.menuBar.addMenu(self.configMenu)
        self.langMenu : QMenu = QMenu(langue.get("menu.settings.speak"), self.configMenu)
        self.changeLangSignal.connect(langue.lazyEval(self.langMenu.setTitle,"menu.settings.speak"))
        self.configMenu.addMenu(self.langMenu)
        self.langMenu.addActions(self.langAction)
        self.themeMenu : QMenu = QMenu(langue.get("menu.settings.theme.title"), self.configMenu)
        self.changeLangSignal.connect(langue.lazyEval(self.themeMenu.setTitle,"menu.settings.theme.title"))
        self.configMenu.addMenu(self.themeMenu)
        self.themeMenu.addActions(self.themeAction)

        self.helpMenu: QMenu = QMenu(langue.get("menu.help.title"), self.menuBar)
        self.changeLangSignal.connect(langue.lazyEval(self.helpMenu.setTitle,"menu.help.title"))
        self.menuBar.addMenu(self.helpMenu)
        self.helpMenu.addAction(self.licenseAction)
        
         # Fenètre détacheable de controle
        self.affichage_controles: bool = True
        self.controles = Controles()
        self.layout.addWidget(self.controles)
        self.controles.setFixedHeight(self.controles.minimumSizeHint().height())
        self.changeLangSignal.connect(langue.lazyEval(self.controles.boutton1.setText,"control.simple_add.title"))
        self.changeLangSignal.connect(langue.lazyEval(self.controles.boutt_show_aj_air.setText,"control.add_settings.title"))

    def closeEvent(self, event) -> None:
        """Permet de fermer toutes les fenêtres lors de la fermeture de la fenêtre principale, et de terminer le programme"""
        app.exit(0)

    def attach_detach_controles(self) -> None: 
        """Permet d'afficher les controles dans une fenètre séparée de la principale."""
        if self.affichage_controles:
            self.controles.hide()
            controles_graphiques.show()
            self.attach_detachAction.setText(langue.get("menu.display.attach"))
            self.affichage_controles = False

        else:
            self.controles.show()
            controles_graphiques.hide()
            self.attach_detachAction.setText(langue.get("menu.display.detach"))
            self.affichage_controles = True
    
    def attach_detach_texte(self):
        if self.affichage_controles:
            self.attach_detachAction.setText(langue.get("menu.display.detach"))
        else :
            self.attach_detachAction.setText(langue.get("menu.display.attach"))
    def change_lang(self, lang):
        settings.set("affichage.langue",lang)
        settings.save()
        langue.reload()
        self.changeLangSignal.emit()
        
    def change_theme(self, theme=None):
        style = ""
        if theme!=None:
            settings.set("affichage.theme",theme)
            settings.save()
        if settings.get("affichage.theme")=="dark":
            style = """
            background-color: #262626;
            color: #FFFFFF;
            """
        elif settings.get("affichage.theme")=="light":
            style = """
            background-color: #DADADA;
            color: #000000;
            """
        elif settings.get("affichage.theme")=="system":
            style = """
            background-color: #05C1FF;
            color: #FA9901;
            """
        self.setStyleSheet(style)
        controles_graphiques.setStyleSheet(style)
        Controles.fenetre_ajoute.setStyleSheet(style)

    def affich_licence(self) -> None:
        """Cette fonction permet d'afficher la licence du projet"""
        self.fenetre_license: QWidget = QScrollArea()
        self.fenetre_license.setWindowTitle(langue.get("file.license"))
        try:
            path: str = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(path, langue.get("file.license"))
            with open(path, encoding="utf-8") as file:
                self.licenseTextlabel: QWidget = QLabel(file.read())
        except:
            print("The requested licence file was not found at", path, file=stderr)
            self.licenseTextlabel: QWidget = QLabel("Ficher manquant ou chemin cassé.")
        self.fenetre_license.setWidget(self.licenseTextlabel)
        self.fenetre_license.show()

class Controles(QWidget):
    """Classe permettant de gérer et afficher les contrôles d'ajout ainsi que leurs effets.

    Args:
        QWidget (class 'Shiboken.ObjectType'): permet l'utilisation de Widgets.
    """
    """Ce QWidget permet de gérer les différents contrôles."""

    
    fenetre_ajoute: QWidget = QScrollArea()
    fenetre_ajoute.setWindowTitle(langue.get("control.add_settings.title"))
    layout_aj_air: QLayout = QGridLayout()
    fenetre_ajoute.setLayout(layout_aj_air)

    amount = QSpinBox(minimum=0, maximum=10000, value=0)
    amountl = QLabel(langue.get("control.add_settings.runway"))
    layout_aj_air.addWidget(amountl, 0,0)
    layout_aj_air.addWidget(amount,0,1)

    nb_airport = QDoubleSpinBox(minimum=1, maximum=1, value=0,decimals=0)
    airport_label = QLabel(langue.get("control.add_settings.airport"))
    for i,widget in enumerate((airport_label, nb_airport, QLabel('+-'),nb_airport)):
        layout_aj_air.addWidget(widget,1,i)
    
    nb_runway = QDoubleSpinBox(minimum=1, maximum=200, value=0,decimals=0)
    runway_label = QLabel(langue.get("control.add_settings.runway"))


    def ajouter_airport(*_) -> None:
        """Permet d'ajouter un aéroport.
        """
        #Fenetre_principale.ajouter_airport(variable)

    bouton_val_aj: QAbstractButton = QPushButton(langue.get("control.add_settings.valid"))
    layout_aj_air.addWidget(bouton_val_aj)
    bouton_val_aj.clicked.connect(ajouter_airport)

    def __init__(self) -> None:
        """Méthode constructeur, permet de créer les boutons cliquables d'ajout de sphères.
        """
        super().__init__()
        self.setWindowTitle(langue.get("control.title"))
        # layout des controles widget
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.boutton1: QAbstractButton = QPushButton(langue.get("control.simple_add.title"))
        self.boutton1.clicked.connect(Controles.ajouter_airport)
        self.layout.addWidget(self.boutton1)

        self.boutt_show_aj_air: QAbstractButton = QPushButton(langue.get("control.add_settings.title"))
        self.layout.addWidget(self.boutt_show_aj_air)
        self.boutt_show_aj_air.clicked.connect(self.fenetre_ajoute.show)


controles_graphiques: QWidget = Controles()
Fenetre_principale: QWidget = Main_window()

Fenetre_principale.changeLangSignal.connect(langue.lazyEval(controles_graphiques.bouton_val_aj.setText,"control.add_settings.valid"))
Fenetre_principale.changeLangSignal.connect(langue.lazyEval(controles_graphiques.fenetre_ajoute.setWindowTitle,"control.add_settings.title"))
for label,setloc in ((Controles.amountl,"control.add_settings.nb"),
                     (Controles.airport_label,"control.add_settings.x"),
                     (Controles.runway_label,"control.add_settings.y")):
    Fenetre_principale.changeLangSignal.connect(langue.lazyEval(label.setText,setloc))
Fenetre_principale.changeLangSignal.connect(langue.lazyEval(controles_graphiques.boutton1.setText,"control.simple_add.title"))
Fenetre_principale.changeLangSignal.connect(langue.lazyEval(controles_graphiques.boutt_show_aj_air.setText,"control.add_settings.title"))

Fenetre_principale.showMaximized()