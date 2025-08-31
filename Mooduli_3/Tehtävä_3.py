sukupuoli = input("Kirjoita sukupuoli: ")
hemogarv = float(input("Kirjoita sinun hemoglobiiniarvo: "))

if (sukupuoli == "mies" and 134 <= hemogarv <= 195):
    print("Sinulla on normaali hemoglobiiniarvo")

elif (sukupuoli == "nainen" and 117 <= hemogarv <= 175):
    print("Sinulla on normaali hemoglobiiniarvo")

elif (sukupuoli == "mies" and hemogarv < 134):
    print("Sinulla on alhainen hemoglobiiniarvi")

elif (sukupuoli == "mies" and hemogarv > 195):
    print("Sinulla on korkea hemoglobiiniarvo")

elif (sukupuoli == "nainen" and hemogarv < 117):
    print("Sinulla on alhainen hemoglobiiniarvi")

elif (sukupuoli == "nainen" and hemogarv > 175):
    print("Sinulla on korkea hemoglobiiniarvo")
else:
    print("Väärä syöte")