app_run = True

while app_run == True:
    tuuma = float(input("Anna tuuma: "))
    if tuuma >= 0:
        sent = tuuma * 2.54
        print(f"Tuumat sentimetreina: {sent:0.2f}")
    else:
        print("Väärä syöte.")
        app_run = False