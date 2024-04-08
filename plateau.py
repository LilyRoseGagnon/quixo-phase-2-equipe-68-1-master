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
        for coordonnée in position:
            if coordonnée < 1 or coordonnée > 5:
                raise QuixoError(
                    'QuixoError: Les positions x et y doivent être entre 1 et 5 inclusivement.')

        x = position[0]
        y = position[1]

        return self.plateau[y][x]

    def __setitem__(self, position, valeur):
        """Modifie la valeur à la position donnée

        Args:
            position (tuple[int, int]): La position (x, y) du pion sur le plateau.
            value (str): La valeur à insérer à la position donnée, soit "X", "O" ou " ".

        Raises:
            QuixoError: Les positions x et y doivent être entre 1 et 5 inclusivement.
            QuixoError: La valeur donnée doit être "X", "O" ou " ".
        """
        for coordonnée in position:
            if coordonnée < 1 or coordonnée > 5:
                raise QuixoError(
                    'QuixoError: Les positions x et y doivent être entre 1 et 5 inclusivement.')

        if valeur not in ('X', 'O', ' '):
            raise QuixoError('QuixoError: La valeur donnée doit être "X", "O" ou " ".')

        x = position[0]
        y = position[1]

        del self.plateau[y][x]

        liste_modifier = self.plateau[y]
        liste_modifier = liste_modifier.insert(x, valeur)

        del self.plateau[y]

        self.plateau.insert(y, liste_modifier)

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
            liste_vide = [' ', ' ', ' ', ' ', ' ']
            plateau_vide = [liste_vide, liste_vide, liste_vide, liste_vide, liste_vide]
            return plateau_vide

        if len(plateau) != 5:
            raise QuixoError(
                'QuixoError: Le plateau doit être une liste de 5 listes de 5 éléments.')

        for liste in plateau:
            if len(liste) != 5:
                raise QuixoError(
                    'QuixoError: Le plateau doit être une liste de 5 listes de 5 éléments.')

            for case in liste:
                if case not in ('X', 'O', ' '):
                    raise QuixoError(
                        'QuixoError: Les éléments du plateau doivent être "X", "O" ou " ".')

        return plateau


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
        if direction not in ('haut', 'bas', 'gauche', 'droite'):
            raise QuixoError(
                'QuixoError: La direction doit être "haut", "bas", "gauche" ou "droite".')

        if pion not in ('X', 'O'):
            raise QuixoError('QuixoError: Le pion à insérer doit être "X" ou "O".')

        if direction == 'bas':
            Plateau.insertion_par_le_bas(self.plateau, pion, origine)

        if direction == 'haut':
            Plateau.insertion_par_le_haut(self.plateau, pion, origine)

        if direction == 'gauche':
            Plateau.insertion_par_la_gauche(self.plateau, pion, origine)

        if direction == 'droite':
            Plateau.insertion_par_la_droite(self.plateau, pion, origine)

    def insertion_par_le_bas(self, pion, origine):
        """Insère un pion dans le plateau en direction du bas

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du pion à insérer.
        """
        ligne = origine[1]
        y = origine[1]

        plateau_inversé = self.plateau[::-1]
        indices = [4, 3, 2, 1, 0]

        for indice, liste in enumerate(plateau_inversé):
            if indice == indices[ligne-1]:
                break

            position = (origine[0], y)
            y += 1
            Plateau.__setitem__(self.plateau, position, pion)

            nouveau_pion = Plateau.état_plateau()
            pion = Plateau.__getitem__(nouveau_pion, position)


    def insertion_par_le_haut(self, pion, origine):
        """Insère un pion dans le plateau en direction du haut

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du pion à insérer.
        """
        ligne = origine[1]
        y = origine[1]

        for indice, liste in enumerate(self.plateau):
            if indice == ligne+1:
                break

            position = (origine[0], y)
            y += 1
            Plateau.__setitem__(self.plateau, position, pion)

            nouveau_pion = Plateau.état_plateau()
            pion = Plateau.__getitem__(nouveau_pion, position)

    def insertion_par_la_gauche(self, pion, origine):
        """Insère un pion dans le plateau en direction de la gauche

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du pion à insérer.
        """
        colonne = origine[0]
        x = origine[0]
        y = origine[1]

        ligne = self.plateau[y]

        for indice, case in enumerate(ligne):
            if indice == colonne+1:
                break

            position = (x, origine[1])
            x += 1
            Plateau.__setitem__(self.plateau, position, pion)

            nouveau_pion = Plateau.état_plateau()
            pion = Plateau.__getitem__(nouveau_pion, position)

    def insertion_par_la_droite(self, pion, origine):
        """Insère un pion dans le plateau en direction de la droite

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            origine (list[int]): La position [x, y] d'origine du pion à insérer.
        """
        colonne = origine[0]
        x = origine[0]
        y = origine[1]

        ligne = self.plateau[y]
        ligne_inversée = ligne[::-1]
        indices = [4, 3, 2, 1, 0]

        for indice, case in enumerate(ligne_inversée):
            if indice == indices[colonne-1]:
                break

            position = (x, origine[1])
            x += 1
            Plateau.__setitem__(self.plateau, position, pion)

            nouveau_pion = Plateau.état_plateau()
            pion = Plateau.__getitem__(nouveau_pion, position)
