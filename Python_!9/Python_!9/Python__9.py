a = int(input("Reqem yazin:"))
b= 0

for i in range(0,a):
    if i%7==0:
        b=i*i
print(b)

cumle = input("Cumle yazin:")

sozler = cumle.split()

dord_herfli = []
for l in sozler:
    if len(l)==4:
        dord_herfli.append(l)
print( dord_herfli )