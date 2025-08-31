i = 0
N = 5
käyt_tunnus = "Pipi"
salasana = "Kaka"
app_run = True

while app_run == True:
    käyt = input("kirjoita käyttäjätunnus: ")
    sal = input ("kirjoita salasana: ")
    if käyt == käyt_tunnus and sal == salasana:
        print("Tervetuloa!")
        app_run = False
    elif i == N:
        print("Pääsy evätty.")
        app_run = False
    else:
        print("Yritä uudelleen.")
        i += 1
