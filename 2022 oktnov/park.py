print('1. feladat')
fileTXT = open('felajanlas.txt')
felajanlData = []
agyasLength = 0

for e in fileTXT:
    data = e.strip().split()
    if (len(data) == 3):
        felajanlData.append([int(data[0]), int(data[1]), data[2]])
    else:
        agyasLength = int(data[0])

print('2. feladat')
print(f"a felajánlások száma: {len(felajanlData)}")

print('3. feladat')
print("A bejárat mindkét oldalán ültetők:", end = " ")
for key in range(1, len(felajanlData) + 1):
    if (felajanlData[key - 1][0] > felajanlData[key - 1][1]):
        print(key, sep="", end=" ")
print()
print('4. feladat')
userInputKey = int(input('Ágyás sorszáma: '))
agyasData = []
for e in felajanlData:
    if (e[0] <= userInputKey <= e[1] or e[0] > e[1] and (e[0] <= userInputKey or e[1] >= userInputKey)):
        agyasData.append(e[2])
print(f'A felajánlók száma: {len(agyasData)}')

if (len(agyasData) > 0):
    print(f"A virágágyás színe, ha csak az első ültet: {agyasData[0]}")
    colorList = " ".join(list(set(agyasData)))
    print(f"A virágágyás színei: {colorList}")
else:
    print('Ezt az ágyást nem ültetik be.')

print('5. feladat')