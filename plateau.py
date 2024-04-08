"""Module Plateau

Classes:
    * Plateau - Classe principale du plateau de jeu Quixo.
"""
from copy import deepcopy

from quixo_error import QuixoError


class Plateau:
    def __init__(self, plateau=None):
        self.plateau = self.construire_plateau(deepcopy(plateau))


    def état_plateau(self):
        return deepcopy(self.plateau)

    def __str__(self):
        grille = '   -------------------' + '\n'
        interligne = '  |---|---|---|---|---|'
        conclusion = '--|---|---|---|---|---\n' + '  | 1   2   3   4   5\n'

        for indice, row in enumerate(self.plateau):
            indice = indice + 1
            ligne = f'{indice}'
            for index, case in enumerate(row):
                ligne += ' | ' + row[index]
            ligne += ' |'

            if indice == 1:
                grille += ligne + '\n'

        else:
            grille += interligne + '\n' + ligne + '\n'

        return grille + conclusion

    def __getitem__(self, position):
        """Retourne la valeur à la position donnée

        Args:
            position (tuple[int, int]): La position (x, y) du pion sur le plateau.

        Returns:
            str: La valeur à la position donnée, soit "X", "O" ou " ".

        Raises:
            QuixoError: Les positions x et y doivent être entre 1 et 5 inclusivement.
        """
        pass

    def __setitem__(self, position, valeur):
        """Modifie la valeur à la position donnée

        Args:
            position (tuple[int, int]): La position (x, y) du pion sur le plateau.
            value (str): La valeur à insérer à la position donnée, soit "X", "O" ou " ".

        Raises:
            QuixoError: Les positions x et y doivent être entre 1 et 5 inclusivement.
            QuixoError: La valeur donnée doit être "X", "O" ou " ".
        """
        pass

    def construire_plateau(self, plateau):
        """Construit un plateau de jeu

        Si un plateau est fourni, il est retourné tel quel.
        Sinon, si la valeur est None, un plateau vide de 5x5 est retourné.

        Args:
            plateau (list[list[str]] | None): La représentation du plateau
                tel que retourné par le serveur de jeu ou la valeur None.

        Returns:
            list[list[str]]: La représentation du plateau
                tel que retourné par le serveur de jeu.

        Raises:
            QuixoError: Le plateau doit être une liste de 5 listes de 5 éléments.
            QuixoError: Les éléments du plateau doivent être "X", "O" ou " ".
        """
        if plateau is None:
            return Plateau.__str__(plateau)
        
        if len(plateau) != 5:
            raise QuixoError('QuixoError: Le plateau doit être une liste de 5 listes de 5 éléments.')
        
        for liste in plateau:
            if len(liste) != 5:
                raise QuixoError('QuixoError: Le plateau doit être une liste de 5 listes de 5 éléments.')
            
            for case in liste:
                if case != 'X' and case != 'O' and case != ' ':
                    raise QuixoError('QuixoError: Les éléments du plateau doivent être "X", "O" ou " ".')
        
        return Plateau.__str__(plateau)


    def insertion(self, pion, origine, direction):
        """Insère un pion dans le plateau

        Cette méthode appelle la méthode d'insertion appropriée selon la direction donnée.

        À noter que la validation des positions sont faites dans
        les méthodes __setitem__ et __getitem__. Vous devez donc en faire usage dans
        les diverses méthodes d'insertion pour vous assurez que les positions sont valides.

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du pion à insérer.
            direction (str): La direction de l'insertion, soit "haut", "bas", "gauche" ou "droite".

        Raises:
            QuixoError: La direction doit être "haut", "bas", "gauche" ou "droite".
            QuixoError: Le pion à insérer doit être "X" ou "O".
        """
        pass

    def insertion_par_le_bas(self, pion, origine):
        """Insère un pion dans le plateau en direction du bas

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du pion à insérer.
        """
        pass

    def insertion_par_le_haut(self, pion, origine):
        """Insère un pion dans le plateau en direction du haut

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du pion à insérer.
        """
        pass

    def insertion_par_la_gauche(self, pion, origine):
        """Insère un pion dans le plateau en direction de la gauche

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du pion à insérer.
        """
        pass

    def insertion_par_la_droite(self, pion, origine):
        """Insère un pion dans le plateau en direction de la droite

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du pion à insérer.
        """
        pass
