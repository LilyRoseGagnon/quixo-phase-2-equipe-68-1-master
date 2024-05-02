
from quixo import Quixo
from plateau import Plateau
from quixo_error import QuixoError


class QuixoIA(Quixo):
    def valider_diagonale(plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        
        n = 0
        m = 0
        x = 0
        y = 0
        diago_1 = [1, 1], [5, 5]
        diago_2 = [1, 5], [5, 1]
        dico = {'X': [], 'O': []}
        
        for ligne, liste in enumerate(plateau):
            if liste[ligne] == 'X':
                n += 1
            if liste[ligne] == 'O':
                x += 1
            if liste[4-ligne] == 'X':
                m += 1
            if liste[4-ligne] == 'O':
                y += 1

        if n >= nb_pions:
            dico['X'] = diago_1
        if m >= nb_pions:
            dico['X'] = diago_2
        if x >= nb_pions:
            dico['O'] = diago_1
        if y >= nb_pions:
            dico['O'] = diago_2

        return dico

    def valider_horizontale(plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        
        dico = {'X': [], 'O': []}
        
        for ligne, liste in enumerate(plateau):
            n = 0
            x = 0
            for case in liste:
                if case == 'X':
                    n += 1
                if case == 'O':
                    x += 1
            if n >= nb_pions:
                dico['X'] += [[1, ligne+1], [5, ligne+1]]
            if x >= nb_pions:
                dico['O'] += [[1, ligne+1], [5, ligne+1]]

        return dico        

    def valider_verticale(plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        
        X_1 = 0
        X_2 = 0
        X_3 = 0
        X_4 = 0
        X_5 = 0
        O_1 = 0
        O_2 = 0
        O_3 = 0
        O_4 = 0
        O_5 = 0
        vert1 = [[1, 1], [1, 5]]
        vert2 = [[2, 1], [2, 5]]
        vert3 = [[3, 1], [3, 5]]
        vert4 = [[4, 1], [4, 5]]
        vert5 = [[5, 1], [5, 5]]
        dico = {'X': [], 'O': []}

        for liste in plateau:
            if liste[0] == 'X':
                X_1 += 1
            if liste[1] == 'X':
                X_2 += 1
            if liste[2] == 'X':
                X_3 += 1
            if liste[3] == 'X':
                X_4 += 1
            if liste[4] == 'X':
                X_5 += 1
            if liste[0] == 'O':
                O_1 += 1
            if liste[1] == 'O':
                O_2 += 1
            if liste[2] == 'O':
                O_3 += 1
            if liste[3] == 'O':
                O_4 += 1
            if liste[4] == 'O':
                O_5 += 1            

        if X_1 >= nb_pions:
            dico['X'] += vert1
        if X_2 >= nb_pions:
            dico['X'] += vert2
        if X_3 >= nb_pions:
            dico['X'] += vert3
        if X_4 >= nb_pions:
            dico['X'] += vert4
        if X_5 >= nb_pions:
            dico['X'] += vert5
        if O_1 >= nb_pions:
            dico['O'] += vert1
        if O_2 >= nb_pions:
            dico['O'] += vert2
        if O_3 >= nb_pions:
            dico['O'] += vert3
        if O_4 >= nb_pions:
            dico['O'] += vert4
        if O_5 >= nb_pions:
            dico['O'] += vert5

        return dico

    def partie_terminée(plateau):
        diago = QuixoIA.valider_diagonale(plateau)
        horiz = QuixoIA.valider_horizontale(plateau)
        vert = QuixoIA.valider_verticale(plateau)

        if diago['X'] != [] or horiz['X'] != [] or vert['X'] != []:
            return Quixo.self.joueurs[0]
        if diago['O'] != [] or horiz['O'] != [] or vert['O'] != []:
            return Quixo.self.joueurs[1]        

    def trouver_coup_gagnant(pion):
        plateau = Plateau.self.plateau
        diago = QuixoIA.valider_diagonale(plateau, 4)
        horiz = QuixoIA.valider_horizontale(plateau, 4)
        vert = QuixoIA.valider_verticale(plateau, 4)

        if diago[pion] == [] and horiz[pion] == [] and vert[pion] == []:
            raise QuixoError("Aucun coup gagnant possible.")
        
        # Trouver case manquante
        if diago[pion] != []:
            if diago[pion] == [[1, 1], [5, 5]]:
                for ligne, liste in enumerate(plateau):
                    if liste[ligne] == pion:
                        continue
                    else:
                        case = [ligne+1, ligne+1]
            if diago[pion] == [[1, 5], [5, 1]]:
                for ligne, liste in enumerate(plateau):
                    if liste[4-ligne] == pion:
                        continue
                    else:
                        case = [ligne+1, 4-ligne]

        if horiz[pion] != []:
            line = horiz[pion][0][1] - 1
            for indice, position in enumerate(plateau[line]):
                if position == pion:
                    continue
                else:
                    case = [indice+1, line+1]

        if vert[pion] != []:
            colonne = vert[pion][0][0] - 1
            for ligne, liste in enumerate(plateau):
                if liste[colonne] == pion:
                    continue
                else:
                    case = [colonne+1, ligne+1]

        #Déterminer le coup
        if case[0] == 1:
            origine = ['5', f'{case[1]}']
            direction = 'gauche'
        if case[0] == 5:
            origine = ['1', f'{case[1]}']
            direction = 'droite'
        if case[1] == 1:
            origine = [f'{case[0]}', '5']
            direction = 'haut'
        if case[1] == 5:
            origine = [f'{case[0]}', '1']
            direction == 'bas'
        
        case_haut = [case[0], case[1]-1]
        case_bas = [case[0], case[1]+1]
        case_gauche = [case[0]-1, case[1]]
        case_droite = [case[0]+1, case[1]]

        if plateau[case_haut[1]-1][case_haut[0]-1] == pion:
            origine = [f'{case_haut[0]}', '5']
            direction = 'haut'
        if plateau[case_bas[1]-1][case_bas[0]-1] == pion:
            origine = [f'{case_bas[0]}', '1']
            direction = 'bas'
        if plateau[case_gauche[1]-1][case_gauche[0]-1] == pion:
            origine = ['5', f'{case_gauche[1]}']
            direction = 'gauche'
        if plateau[case_droite[1]-1][case_droite[0]-1] == pion:
            origine = ['1', f'{case_droite[1]}']
            direction = 'droite'

        if plateau[(int(origine[1]))-1][(int(origine[0]))-1] != '':
            raise QuixoError("Aucun coup gagnant possible.")

        return origine, direction

    def trouver_coup_bloquant(pion):
        plateau = Plateau.self.plateau
        diago = QuixoIA.valider_diagonale(plateau, 4)
        horiz = QuixoIA.valider_horizontale(plateau, 4)
        vert = QuixoIA.valider_verticale(plateau, 4)

        if pion == 'X':
            pion_adv = 'O'
        if pion == 'O':
            pion_adv = 'X'

        if diago[pion_adv] == [] and horiz[pion_adv] == [] and vert[pion_adv] == []:
            raise QuixoError("Aucun coup bloquant possible.")
        
        # Trouver case manquante
        if diago[pion_adv] != []:
            if diago[pion_adv] == [[1, 1], [5, 5]]:
                for ligne, liste in enumerate(plateau):
                    if liste[ligne] == pion_adv:
                        continue
                    else:
                        case = [ligne+1, ligne+1]
            if diago[pion_adv] == [[1, 5], [5, 1]]:
                for ligne, liste in enumerate(plateau):
                    if liste[4-ligne] == pion_adv:
                        continue
                    else:
                        case = [ligne+1, 4-ligne]

        if horiz[pion_adv] != []:
            line = horiz[pion_adv][0][1] - 1
            for indice, position in enumerate(plateau[line]):
                if position == pion_adv:
                    continue
                else:
                    case = [indice+1, line+1]

        if vert[pion_adv] != []:
            colonne = vert[pion_adv][0][0] - 1
            for ligne, liste in enumerate(plateau):
                if liste[colonne] == pion_adv:
                    continue
                else:
                    case = [colonne+1, ligne+1]

        #Déterminer le coup
        if case[0] == 1:
            origine = ['5', f'{case[1]}']
            direction = 'gauche'
        if case[0] == 5:
            origine = ['1', f'{case[1]}']
            direction = 'droite'
        if case[1] == 1:
            origine = [f'{case[0]}', '5']
            direction = 'haut'
        if case[1] == 5:
            origine = [f'{case[0]}', '1']
            direction == 'bas'
        
        case_haut = [case[0], case[1]-1]
        case_bas = [case[0], case[1]+1]
        case_gauche = [case[0]-1, case[1]]
        case_droite = [case[0]+1, case[1]]

        if plateau[case_haut[1]-1][case_haut[0]-1] == pion:
            origine = [f'{case_haut[0]}', '5']
            direction = 'haut'
        if plateau[case_bas[1]-1][case_bas[0]-1] == pion:
            origine = [f'{case_bas[0]}', '1']
            direction = 'bas'
        if plateau[case_gauche[1]-1][case_gauche[0]-1] == pion:
            origine = ['5', f'{case_gauche[1]}']
            direction = 'gauche'
        if plateau[case_droite[1]-1][case_droite[0]-1] == pion:
            origine = ['1', f'{case_droite[1]}']
            direction = 'droite'

        if plateau[(int(origine[1]))-1][(int(origine[0]))-1] != '':
            raise QuixoError("Aucun coup bloquant possible.")

        return origine, direction

    def jouer_le_coup():
        pass