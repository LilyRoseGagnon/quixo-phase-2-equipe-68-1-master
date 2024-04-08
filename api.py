"""Module d'API du jeu Quixo

Attributes:
    URL (str): Constante représentant le début de l'url du serveur de jeu.

Functions:
    * lister_parties - Récupérer la liste des parties reçus du serveur.
    * débuter_partie - Créer une nouvelle partie et retourne l'état de cette dernière.
    * récupérer_partie - Retrouver l'état d'une partie spécifique.
    * jouer_coup - Exécute un coup et retourne le nouvel état de jeu.
"""
import requests

URL = "https://pax.ulaval.ca/quixo/api/h24/"


def lister_parties(idul, secret):
    historic_parties = requests.get(URL+'parties', auth=(idul, secret))

    if historic_parties.status_code == 200:
        return historic_parties.json()['parties']

    if historic_parties.status_code == 401:
        erreur = historic_parties.json()['message']
        raise PermissionError(f'{erreur}')

    if historic_parties.status_code == 406:
        erreur = historic_parties.json()['message']
        raise RuntimeError(f'{erreur}')

    raise ConnectionError


def débuter_partie(idul, secret):
    début = requests.post(URL+'partie/', auth=(idul, secret))

    if début.status_code == 200:
        identifiant = début.json()['id']
        state = début.json()['état']['plateau']

        liste_joueurs = lister_parties(idul, secret)
        for partie in liste_joueurs:
            if identifiant == partie['id'] :
                id_joueurs = partie['joueurs']
            else:
                continue

        return identifiant, id_joueurs, state

    if début.status_code == 401:
        erreur = début.json()['message']
        raise PermissionError(f'{erreur}')

    if début.status_code == 406:
        erreur = début.json()['message']
        raise RuntimeError(f'{erreur}')

    raise ConnectionError


def récupérer_partie(id_partie, idul, secret):
    données_partie = requests.get(URL+f'partie/{id_partie}', auth=(idul, secret))

    if données_partie.status_code == 200:
        identifiant = données_partie.json()['id']
        state = données_partie.json()['état']['plateau']
        joueur_gagnant = données_partie.json()['gagnant']

        liste_joueurs = lister_parties(idul, secret)
        for partie in liste_joueurs:
            if identifiant == partie['id'] :
                id_joueurs = partie['joueurs']
            else:
                continue

        return identifiant, id_joueurs, state, joueur_gagnant

    if données_partie.status_code == 401:
        erreur = données_partie.json()['message']
        raise PermissionError(f'{erreur}')

    if données_partie.status_code == 406:
        erreur = données_partie.json()['message']
        raise RuntimeError(f'{erreur}')

    raise ConnectionError


def jouer_coup(id_partie, origine, direction, idul, secret):
    coup = requests.put(URL+'jouer', auth=(idul, secret),
                        json={
                            'id': id_partie, 
                            'origine': origine, 
                            'direction': direction})

    if coup.status_code == 200:
        if coup.json()['gagnant']:
            joueur_gagnant = coup.json()['gagnant']
            raise StopIteration(f'{joueur_gagnant}')

        identifiant = coup.json()['id']
        state = coup.json()['état']['plateau']

        liste_joueurs = lister_parties(idul, secret)
        for partie in liste_joueurs:
            if identifiant == partie['id'] :
                id_joueurs = partie['joueurs']
            else:
                continue

        return identifiant, id_joueurs, state

    if coup.status_code == 401:
        erreur = coup.json()['message']
        raise PermissionError(f'{erreur}')

    if coup.status_code == 406:
        erreur = coup.json()['message']
        raise RuntimeError(f'{erreur}')

    raise ConnectionError
