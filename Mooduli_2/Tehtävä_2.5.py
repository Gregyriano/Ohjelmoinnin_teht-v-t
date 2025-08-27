leiviskät = input("Anna leiviskät: ")

naulat = input("Anna naulat: ")

luodit = input("Anna luodit: ")

naulojen_määrä = (float(leiviskät) * 20) + float(naulat)

luotien_määrä = (naulojen_määrä * 32) + float(luodit)

massa = float(luotien_määrä) * 13.3

kilogrammat  = massa // 1000

grammat = massa % 1000

print(f"Massa nykymittojen mukaan: {kilogrammat:.0f} kilogrammaa ja {grammat:.0f} grammaa")






