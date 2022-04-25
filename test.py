from random import randint

prix=0
prix=randint(1,100)
i=1
print("Tu as droit à 5 essaies entre 1 et 100")
saisie=input("Entrer un nombre : ")

def test():
    global saisie
    v=True
    v=saisie.isnumeric()
    while v==False: 
        print("Erreur de saisie")
        saisie=input("Entrer un nombre : ")
        v=saisie.isnumeric()
    saisie=int(saisie)
    return saisie

    
test()
print(saisie)
note=5

while i<=4:
    
    if saisie<prix:
        print("C'est plus")
        note=note-1
        saisie=input("Entrer un nombre : ")
        test()
    elif saisie>prix:
        print("C'est moins")
        note=note-1
        saisie=input("Entrer un nombre : ")
        test()
    else :
        print(f"Win vous avez {note} points")
        break
    
    i=i+1
    
if note==1:
    p=note-1
    print(f"Echec vous avez {p} points")