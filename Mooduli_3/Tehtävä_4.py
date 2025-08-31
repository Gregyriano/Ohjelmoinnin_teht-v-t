lukuvuosi = float(input("Anna lukuvuosi: "))

if (lukuvuosi % 4 == 0):
    print("Tämä vuosi on karkainen.")
elif (lukuvusi % 100 == 0 and lukuvuosi % 400 == 0 ):
    print("Tämä vuosi on karkainen.")
else:
    print("Tämä vuosi ei ole karkainen.")
