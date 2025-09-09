nums = []

n = input("Syötä numero tai lopeta painamalla Enter:")

while n != "":
    print(n)
    nums.append(int(n))
    n = input("Syötä numero tai lopeta painamalla Enter:")
else:
    print(nums)

def sumcalc(list):
    u = 0
    for i in list:
        u = u + i
    return u

print(sumcalc(nums))
