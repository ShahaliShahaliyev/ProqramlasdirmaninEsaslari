#Tapsiriq 1
print ("Tapsiriq 1")

a = input("reqem yaz:")
reqemler = []
kvadrat = []
for i in a:
    if i == ",":
        continue;
    else:
        reqemler.append(i)
        i = int(i)
        kvadrat.append(i**2)
print (kvadrat)

#Tapsiriq 2
print ("Tapsiriq 2")

cumle = input("Cumle yazin:")

sozler = cumle.split()

enQisaSoz = sozler[0]

for i in sozler:
    if len(i) < len(enQisaSoz):
        enQisaSoz = i

print(enQisaSoz)

#Tapsiriq 3
print ("Tapsiriq 3")
x = int(input("Reqem yaz:"))
y = int(input("Reqem yaz:"))
ededler = []

for i in range(x,y):
    if i%6==0:
        ededler.append(i)
print ( ededler )

#Tapsiriq 4
print ("Tapsiriq 4")

cumle = input("Soz yazin:")
alinanSiyahi = input("Siyahiya elave edin:")
siyahi = []
soz = []

for l in alinanSiyahi:
    siyahi.append(l)

for i in cumle:
    if siyahi.__contains__(i):
        soz.append(i)
    else:
        soz.append("-")
print ( soz )

#Tapsiriq 5
print ("Tapsiriq 5")

data = open("data.txt","r")

for i in data:
    print(i)
