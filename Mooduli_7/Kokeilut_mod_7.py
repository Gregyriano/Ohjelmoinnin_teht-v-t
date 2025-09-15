oppilaat = {
    'Aapeli': 25,
    'Bertta': 56,
    'Cecilia': 53,
    'Daniel': 23,
    'Emma': 25
}
print(oppilaat)

# mitä ovat tietueet / items
print(oppilaat.items())

# mitä ovat avaimet sanakirjassa
print(oppilaat.keys())

# mitä ovat arvot / values sanakirjassa
print(oppilaat.values())

for o in oppilaat:
    print(o)

print(f"Danielin ikä: {oppilaat['Daniel']}")

for o in oppilaat:
    print(f'Oppilaan nimi on {o} ja IKÄ on {oppilaat[o]}')



yhteystiedot = {
    'Aapeli': {
        'puh': '0503546585',
        'osoite': 'Linnuntie 5'
    },
    'Bertta': {
        'puh': '0406797466',
        'osoite': 'Rapakuja 7'
    },
    'Cecilia': {
        'puh': '0406797466',
        'osoite': 'Tullihaukankuja 8'
    }
}

print(yhteystiedot["Aapeli"]["osoite"])

numerot = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"}

numerot["Olga"] = "050-1011012"
numerot["Mary"] = "0401-2132139"

print (numerot)

