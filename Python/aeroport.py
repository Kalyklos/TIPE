# référencement de différents aéroports (sommets du graphe) représenté par des classes




class Airport:
    """Classe régissant les aéroports (noeuds)"""
    def __init__(self, nb_runway):
        self.nb_runway = nb_runway
        self.f_runway = self.nb_runway
    def is_free (self):
        """Vérifie si une piste est libre.

        Returns:
            bool: True s'il reste une piste de libre, False sinon.
        """
        if self.f_runway > 0:
            return True
        return False
    def take_runway(self):
        """Réserve une piste.
        """
        self.f_runway -= 1
    def free_runway(self):
        """Libère une piste réservé.
        """
        self.f_runway +=1
