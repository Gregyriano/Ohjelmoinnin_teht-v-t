nums = []

n = input("Syötä numero tai lopeta painamalla Enter:")

while n != "":
    print(n)
    nums.append(int(n))
    n = input("Syötä numero tai lopeta painamalla Enter:")

def parluk(list):
    nums_par = []
    for i in list:
        if i % 2 == 0:
            nums_par.append(i)
        else:
            print(i)
    return nums_par
print(nums)
print(parluk(nums))


