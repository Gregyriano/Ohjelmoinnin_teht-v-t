

kuut = ("kevät", "kesä", "syksy", "talvi")

number = int(input("Anna kuukauden numero (1-12): "))

if number in range(1,3):
    print(kuut[0])
elif number in range(4,6):
    print(kuut[1])
elif number in range(7,9):
    print(kuut[2])
else:
    print(kuut[3])

