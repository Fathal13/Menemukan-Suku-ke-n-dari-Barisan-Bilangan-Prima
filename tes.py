print("-"*70)
print("Menemukan suku ke-n dari barisan bilangan prima.")
print("-"*70)

# Nilai input
n = int(input("Masukkan suku ke-n :"))
print("-"*70)

# Rumus jawaban
x = 1
a = 1
while x < 8:
    x += 1
    if a == n:
        print(f"Maka suku ke-{a} = {x}")
        print("-"*70)
        a += 1
    else:
        a += 1
        if x % 2 == 1:
            x += 1
    
    if a == (n+1):
        break

while True:
    if x % 2 == 0:
        x += 1
    elif x % 3 == 0:
        x += 1
    elif x % 5 == 0:
        x += 1
    elif x % 7 == 0:
        x += 1

    else :
        while True:
            if a == n:
                print(f"Maka suku ke-{a} = {x}")
                print("-"*70)
            a += 1
            x += 1
            break

    if a == (n+1):
        break