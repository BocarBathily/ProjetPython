
from random import randint
t=2

while t==2:

    def alaligne():
        print()

    
    alaligne()
    print("-------LE JUSTE PRIX-------")
    alaligne()

    num=randint(1,20)
    print("Tu as droit à 3 essaies entre 1 et 20")
    saisie=input("Essaie : ")

    def test():
        global saisie
        test=saisie.isnumeric()
        while test==False: 
            saisie=input("T'es con ou quoi, j'ai dit un nombre merde! : ")
            test=saisie.isnumeric()
            saisie=int(saisie)
            return saisie

    

    test()
    note=3
    i=1
    

    while i<3:
        saisie=int(saisie)
        if (saisie)<(num):
            print("C'est plus")
            note=note-1
            saisie=input("Réessaie : ")
            test()
        elif (saisie)>(num):
            print("C'est moins")
            note=note-1
            saisie=input("Réessaie : ")
            test()
        else :
            print(f"Tu l'asfais mec, t'es le meilleur. T'as {note} points")
            alaligne()
            print("-------LE JEU EST FINI-------")
            alaligne()
            break
    
        i=i+1
    

    if note==1:
        p=note-1
        print(f"T'es un looser, tu m'as fais perdre mon temps. T'as eu {p} point ")
        alaligne()
        print("-------LE JEU EST FINI-------")
        alaligne()

