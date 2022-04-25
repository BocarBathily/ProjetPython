from random import randint
print()
print("-------LE JUSTE PRIX-------")
print()

num=randint(1,100)


print("Tu as droit à 5 essaies entre 1 et 100")
saisie=input("Entre un nombre : ")

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
note=5
i=1
while i<5:
    
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
        print()
        print("-------LE JEU EST FINI-------")
        print()
        break

    i+=1
    

    
if note==1:
    p=note-1
    print(f"Echec vous avez {p} points")
    print()
    print("-------LE JEU EST FINI-------")
    print()