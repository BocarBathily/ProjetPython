t=2
while t==2:
    def alaligne():
        print()

    from random import randint
    alaligne()
    print("-------LE JUSTE PRIX-------")
    alaligne()

    num=randint(1,20)


    print("Tu as droit à 3 essaies entre 1 et 20")
    saisie=input("Saisie : ")

    def test():
        global saisie
        test=saisie.isnumeric()
        while test==False: 
            print("Erreur de saisie")
            saisie=input("Entrer un nombre : ")
            test=saisie.isnumeric()
        saisie=int(saisie)
        return saisie

    
    test()
    note=3
    i=1
    while i<3:
        if saisie<num:
            print("C'est plus")
            note=note-1
            saisie=input("Entrer un nombre : ")
            test()
        elif saisie>num:
            print("C'est moins")
            note=note-1
            saisie=input("Entrer un nombre : ")
            test()
        else :
            print(f"Win vous avez {note} points")
            alaligne()
            print("-------LE JEU EST FINI-------")
            alaligne()
            break

        i+=1
    

    
if note==1:
    p=note-1
    print(f"Echec vous avez {p} points")
    alaligne()
    print("-------LE JEU EST FINI-------")
    alaligne()

#modifier par le stagiaire pour apprendre a gérer les conflit
