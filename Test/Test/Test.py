aa = "javascript"
print(aa[2:6:2])



a= False
b=7
c=200

if a or c==200:
    print("K",end=",")
elif c and not b:
    print("B",end=",")
else:
    print("D",end="")

names1 = ["python","php","C++","Javascript"]
names2 = names1
names3 = names1[:]

names2[0]="java"
names3[1]="C#"

print(names1,names2,names3)

sum =0
for l in (names1,names2,names3):
    if l [3]=="java":
        sum+=1
    if l[2]=="C#":
        sum+=10
    if l[2]=="C++":
        sum+=23
print(sum)

cumle = input("cumle:")

b = cumle.split()

for i in b:
    if i[0]=="a" and i[-1]=="m":
        print(i)
    else:
        print("bele soz yoxdur")
print(a)

