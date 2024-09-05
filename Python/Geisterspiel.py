from random import randint


print("Willkommen zum Geisterspiel")
print(" Es gibt 3 Türen, wähle eine von diesen Türen und hoffe das sich der Geist nicht dahinter befindet")
print("====================================================================================================")

Geistertuer = True
score = 0

while Geistertuer:
    geist = randint(1, 5)
    print("vor dir sind fünf Türen")
    print("wähle eine davon aus.")
    tuer = input("1, 2, 3, 4 oder 5:  ")
    tuer_nummer = int(tuer)
    if tuer_nummer == geist:
        print("Hinter der tür %s ist der GEIST", tuer_nummer)
        print("Lauf schnell weg\n")
        Geistertuer = False
    else:
        print("Der Geist ist nicht hinter der Tür")
        print("gehe eine Tür weiter.\n")
        score = score + 1

print("GAME OVER")
print("Du hast %s Punkte erreicht\n" % score)

input("drück ENTER zum schließen")