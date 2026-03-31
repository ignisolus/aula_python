popA = float(input("População A: "))
taxA = float(input("Taxa A (%): ")) / 100
popB = float(input("População B: "))
taxB = float(input("Taxa B (%): ")) / 100
anos = 0
while popA < popB:
    popA += popA * taxA
    popB += popB * taxB
    anos += 1
print("Anos:", anos)