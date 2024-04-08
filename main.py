"""Jeu Quixo

Ce programme permet de joueur au jeu Quixo.
"""
from api import débuter_partie, jouer_coup, lister_parties
from quixo import Quixo, analyser_commande, formater_les_parties

# Mettre ici votre secret récupérer depuis le site de PAX
SECRET = ""


if __name__ == "__main__":
    args = analyser_commande()
    if args.parties:
        parties = lister_parties(args.idul, SECRET)
        print(formater_les_parties(parties))
    else:
        id_partie, joueurs, plateau = débuter_partie(args.idul, SECRET)
        while True:
            # Créer une instance de Quixo
            quixo = Quixo(joueurs, plateau)
            # Afficher la partie
            print(quixo)
            # Demander au joueur de choisir son prochain coup
            origine, direction = quixo.récupérer_le_coup()
            # Envoyez le coup au serveur
            id_partie, joueurs, plateau = jouer_coup(
                id_partie,
                origine,
                direction,
                args.idul,
                SECRET,
            )
