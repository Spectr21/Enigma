p1 = p2 = p3 = -1
r1=r2=r3 = -1
result = ''
alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
while min(p1,p2,p3) < 0 or max(p1,p2,p3) > 25:
    p1 = int(input("Insert position of first rotor: "))
    p2 = int(input("Insert position of second rotor: "))
    p3 = int(input("Insert position of third rotor: "))
while min(r1,r2,r3) < 0 or max(r1,r2,r3) > 25:
    r1 = int(input("Insert position of first ring: "))
    r2 = int(input("Insert position of second ring: "))
    r3 = int(input("Insert position of third ring: "))
n2 = 15
n3 = 10
rtr1 = list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
rtr2 = list('AJDKSIRUXBLHWTMCQGZNPYFVOE')
rtr3 = list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
p = (rtr1.index('A') - 1 + r1) % 26
for i in range(len(rtr3)):
    rtr1[i] = alph[((alph.index(rtr1[i])) - 1 + r1)%26]
while rtr1[p] != alph[r1 - 1]:
    rtr1 = rtr1[-1:] + rtr1[:-1]
p = (rtr2.index('A') - 1 + r2) % 26
for i in range(len(rtr3)):
    rtr2[i] = alph[((alph.index(rtr2[i])) - 1 + r2)%26]
while rtr1[p] != alph[r2 - 1]:
    rtr1 = rtr1[-1:] + rtr1[:-1]
p = (rtr3.index('A') + r3 - 1) % 26
for i in range(len(rtr3)):
    rtr3[i] = alph[((alph.index(rtr3[i])) + r3 - 1)%26]
while rtr3[p] != alph[r3 - 1]:
    rtr3 = rtr3[-1:] + rtr3[:-1]
#print(*alph)
#print(*rtr1)
#print(*rtr2)
#print(*rtr3)'''
refl_ukw_a = list('EJMZALYXVBWFCRQUONTSPIKHGD')
print("Your text: ")
string = input()
string = string.upper()
words = string.split()

def encode(letter):
    global p1, p2, p3, rtr1, rtr2, rtr3
    ln = alph.index(letter)
    p3 = (p3 + 1) % 26
    if p3 == n2:
        p2 = (p2 + 1) % 26
    if p2 == n3:
        p3 = (p3 + 1) % 26
    ln = alph.index(rtr3[(p3 + ln) % 26])
    ln = alph.index(rtr2[(ln + (p2 - p3)) % 26])
    ln = alph.index(rtr1[(ln + (p1 - p2)) % 26])
    ln = alph.index(refl_ukw_a[(ln - p1) % 26])
    ln = rtr1.index(alph[(ln + p1) % 26])
    ln = rtr2.index(alph[(ln - (p1 - p2)) % 26])
    ln = rtr3.index(alph[(ln - (p2 - p3)) % 26])
    return alph[(ln - p3) % 26]

for w in words:
    for l in w:
        result += encode(l)
    result += ' '
print(result)

