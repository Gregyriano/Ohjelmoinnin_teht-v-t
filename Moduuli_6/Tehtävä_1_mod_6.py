def say_hello_v2(username, age):
    #print("moi")
    #print(username)
    #print(f"Ikäsi: {age}")
    username = username.capitalize() # muuttaa ensimmäisen kirjaimen Isoksi
    return f"Hello {username}!, age: {age}"

#print(say_hello()) # suorittaa funktion ja tulostaa paluuarvon None
#say_hello()
print(say_hello_v2("matti", 5))
nimi = "maija"
return_value = say_hello_v2(nimi, 6)
print(return_value)
print(f"nimi muuttujan arvo: {nimi} ei muutu pääohjelmassa")