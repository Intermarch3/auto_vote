from requests import post, get
from time import sleep
from random import randint

def menu():
    print("\n\n\nBienvenue sur le programme d'auto vote by *Intermarch3* !!!\n")
    nb_vote = int(input("Combien de vote voulez vous créer ?\n>>> "))
    random_delay = input("Voulez vous un delaie aléatoir entre la création de deux vote ? (oui/non)\n>>> ")
    if (random_delay == "oui"):
        max_delay = int(input("Quel est le delay maximum que vous autorisée ? (en seconde)\n>>> "))
        min_delay = int(input("Quel est le delay minimum que vous autorisée ? (en seconde)\n>>> "))
        return nb_vote, random_delay, max_delay, min_delay
    elif (random_delay == "non"):
        delay = int(input("Combien de delaie voulez vous entre la création de deux vote ? (en seconde)\n>>> "))
        return nb_vote, random_delay, delay


def main(nb_vote, random, delay=0, max=0, min=0):
    vote = 0
    payload = {'api_key': 'apikey_from_scraperapi_here', 'url':'https://karaoke.fribourg-centre.com/wp-admin/admin-ajax.php', 'keep_headers': 'true', 'country_code': 'fr'}
    payload_website = {'api_key': 'apikey_from_scraperapi_here', 'url':'https://karaoke.fribourg-centre.com/karaoke/votez-pour-marouchka-au-karaoke-challenge/'}
    data = {'action': 'save', 'id': '976'}
    headers = {
        'sec-fetch-site': 'smae-origin',
        'accept-language': 'fr-FR',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    while vote < nb_vote:
        if (random == "oui"):
            website = get('http://api.scraperapi.com', params=payload_website)
            print("Demande du site web : ", website)
            r = post('http://api.scraperapi.com', params=payload, data=data, headers=headers)
            vote = vote + 1
            print("Vote numéro ", vote, " : ", r)
            time = randint(min, max)
            print("Attente de ", time, " secondes ...\n")
            sleep(time)
        elif (random == "non"):
            website = get('http://api.scraperapi.com', params=payload_website)
            print("Demande du site web : ", website)
            r = post('http://api.scraperapi.com', params=payload, data=data, headers=headers )
            vote = vote + 1
            print("Vote numéro ", vote, " : ", r, "\n")
            sleep(delay)

if __name__ == '__main__':
    settings = menu()
    if (settings[1] == "oui"):
        main(nb_vote=settings[0], random=settings[1], max=settings[2], min=settings[3])
    elif (settings[1] == "non"):
        main(nb_vote=settings[0], random=settings[1], delay=settings[2])
