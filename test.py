def alaligne():
    print()



from random import randint
a()
print("-------LE JUSTE PRIX-------")
alaligne()

num=randint(1,80)


print("Tu as droit à 4 essaies entre 1 et 80")
saisie=input("Essaie : ")

def test():
    global saisie
    test=saisie.isnumeric()
    while test==False: 
        print("Erreur de saisie")
        saisie=input("non,c'est pas cà : ")
        test=saisie.isnumeric()
    saisie=int(saisie)
    return saisie

    
test()
note=4
i=1
while i<4:
    
    if saisie<num:
        print("C'est plus")
        note=note-1
        saisie=input("non,c'est pas cà : ")
        test()
    elif saisie>num:
        print("C'est moins")
        note=note-1
        saisie=input("non,c'est pas cà : ")
        test()
    else :
        print(f"Victoire vous avez {note} points")
        alaligne()
        print("-------LE JEU EST FINI-------")
        alaligne()
        break

    i=i+1
    

    
if note==1:
    p=note-1
    print(f"T'es un looser, t'as eu {p} point minable ")
    alaligne()
    print("-------LE JEU EST FINI-------")
    alaligne()
