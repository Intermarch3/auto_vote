from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from time import sleep
from random import randint
import sys

driver = webdriver.Chrome(executable_path="chromedriver.exe")

dev = False

def menu():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nBienvenue sur le programme d'auto vote fait par un dieu !!!\n")
    proxy = input("Quelle site de proxy utiliser ?\n1 : CroxyProxy (environ 5 vote max )\t2 : proxysite (max 35 votes)\n>>> ")
    if (dev == True):
        nb_vote = 3
        random_delay = "non"
        delay = 5
        print("Dev mode activé : nb vote 3; pas de delai random; delay de 5s")
        return nb_vote, random_delay, proxy, delay
    else:
        nb_vote = int(input("Combien de vote voulez vous créer ?\n>>> "))
        random_delay = input("Voulez vous un delaie aléatoir entre la création de deux vote ? (oui/non)\n>>> ")
        if (random_delay == "oui"):
            max_delay = int(input("Quel est le delay maximum que vous autorisée ? (en seconde)\n>>> "))
            min_delay = int(input("Quel est le delay minimum que vous autorisée ? (en seconde)\n>>> "))
            return nb_vote, random_delay, proxy, max_delay, min_delay
        elif(random_delay == "non"):
            delay = int(input("Combien de delaie voulez vous entre la création de deux vote ? (en seconde)\n>>> "))
            return nb_vote, random_delay, proxy, delay


def random_delay(min, max):
    return randint(min, max)


def vote_function_croxy(nb_vote, delay):
    vote = 0

    while vote != int(nb_vote):
        try:
            driver.get("https://www.croxyproxy.com/_fr/")
            sleep(2.5)
            driver.find_element_by_id("url").send_keys("https://karaoke.fribourg-centre.com/karaoke/votez-pour-marouchka-au-karaoke-challenge/", Keys.RETURN)
            print("\nAttente chargement de la page . . .\n")
            sleep(5)
            vote_btn = driver.find_element_by_class_name("vote")
            vote_btn.click()
            vote = vote + 1 
            print("\nVote N° ", vote, " réalisée !!!\n")
            print("\nDelai de ", delay, " seconde\n")
            sleep(delay)
        except NoSuchElementException:
            print("\nErreur : Vote N° ", vote + 1, " non-réalisée car le boutton n'est pas disponible\n")
    sys.exit()




def vote_function_proxysite(nb_vote, delay): # max 35 vote
    vote = 0
    for i in range(0, nb_vote):
        driver.get("https://www.proxysite.com/fr/")
        sleep(1)
        server_ls = ["us1", "us2", "us3", "us4", "us5", "us6", "us7", "us8", "us9", "us10", "us11", "us12", "us13", "us14", "us15", "us16", "us17", "eu1", "eu2", "eu3", "eu4", "eu5", "eu6", "eu7", "eu8", "eu9", "eu10", "eu11", "eu12", "eu13", "eu14", "eu15", "eu16", "eu17", "eu18"]
        select = Select(driver.find_element_by_name('server-option'))
        try:
            select.select_by_value(server_ls[i])
        except NoSuchElementException:
            print("Erreur : serveur ", server_ls[i], " introuvable !!!")
            continue
        print("\nSelection du serveur ", server_ls[i])
        try:
            driver.find_element_by_name("d").send_keys("https://karaoke.fribourg-centre.com/karaoke/votez-pour-marouchka-au-karaoke-challenge/", Keys.RETURN)
            print("\nAttente chargement de la page . . .\n")
            # sleep(5)
            vote_btn = driver.find_element_by_class_name("vote")
            vote_btn.click()
            vote = vote + 1 
            print("\nVote N° ", vote, " réalisée !!!\n")
            print("\nDelai de ", delay, " seconde\n")
            sleep(delay)
        except NoSuchElementException:
            print("\nErreur : Vote N° ", vote + 1, " non-réalisée car le boutton n'est pas disponible\n")
    sys.exit()




if __name__ == '__main__':
    sleep(2)
    set = menu()
    if (set[2] == "1"):
        if (set[1] == "oui"):
            print("Démarage . . .\n")
            vote_function_croxy(set[0], random_delay(set[4], set[3]))
        elif (set[1] == "non"):
            print("Démarage . . .\n")
            vote_function_croxy(set[0], set[3])
    elif (set[2] == "2"):
        if (set[1] == "oui"):
            print("Démarage . . .\n")
            vote_function_proxysite(set[0], random_delay(set[4], set[3]))
        elif (set[1] == "non"):
            print("Démarage . . .\n")
            vote_function_proxysite(set[0], set[3])



