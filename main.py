from os import system
from platform import system as platform
import sys
from pathlib import Path


file = Path(__file__).resolve()
parent, top = file.parent, file.parents[1]
sys.path.append(str(top))


if platform() == "Windows":
    effacer = 'cls'
else:
    effacer = 'clear'

system(effacer)

sys.path.append(str(Path(__file__).resolve().parents[1]))



#------------------------------------------#fonctions#------------------------------------------#



def menu():
    system(effacer)
    choix = None
    liste_menu = ['continuer','nouvelle partie','options','aide','tutorial','conseil','quitter']
    while choix not in liste_menu:
        choix =  input('''
                 
        Bien venue sur ..........
          que voulais vous faire
                 
    [continuer    [nouvelle partie]
                                                 
    [options       [aide]
                  
    [tutorial]      [conseil]
                 
    [quitter
    
    [''')
        if choix not in liste_menu:
            system(effacer)
            print('  veuiller saissir une option qui existe')
    return choix


def continuer(sauv1,sauv2,sauv3):
    system(effacer)
    fichier_sauv = None
    while fichier_sauv != sauv1 or fichier_sauv != sauv2 or fichier_sauv != sauv3 or fichier_sauv == None:
        fichier_sauv = input(f'''
                             
    [continuer]
                          
    quelle sauvegarde voulais vous charger
                         
    [1 - { sauv1 }]
    [2 - { sauv2 }]
    [3 - { sauv3 }]

    [retour]
                         
    [''')
        if fichier_sauv == 'retour':
            __main__()
        if fichier_sauv != sauv1 or fichier_sauv != sauv2 or fichier_sauv != sauv3:
            system(effacer)
            print("cette sauvegarde n'existe pas veuiller saissir une option qui existe ou de cree une nouvelle sauvegarde  ")
            print(fichier_sauv)
            print(sauv1 , sauv2 , sauv3)
    return fichier_sauv



#------------------------------------------#main#------------------------------------------#


def  __main__():
    sauv1 = 'pomme'
    sauv2 = None
    sauv3 = None
    quoi_faire = menu()
    if quoi_faire == 'continuer':
        fichier_run = continuer(sauv1,sauv2,sauv3)
        
            



__main__()