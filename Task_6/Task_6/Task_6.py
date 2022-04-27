##Tapsiriq 1

i=0

while i<5:
     a = int(input("Reqem daxil edin:"))
     if a%2 ==0:
        print("Reqem Cutdur.")
        i=i+1
     else:
        print("Reqem tekdir.")
        i=i+1
 



print("*********")
##Tapsiriq 2

x = int(input("Reqem daxil edin:"))
y = int(input("Reqem daxil edin:"))

if x>y:
    print("Boyuk eded:",x)
else:
    print("Boyuk eded:",y)

print("*********")
##tapsiriq 3

x = int(input("Reqem daxil edin:"))
y = int(input("Reqem daxil edin:"))

cemin_yarsi = (x+y)/2
ededlerin_2misli = x*y*2

if x<y:
    x = cemin_yarsi
    print("x=",x)
    y = ededlerin_2misli
    print("y=",y)
else:
    y = cemin_yarsi
    print("y=",y)
    x = ededlerin_2misli
    print("x=",x)

print("*********")
#Tapsiriq 4

a = int(input("3 reqemli eded daxil edin: "))

sum = 0
b = a
while b > 0:
   c = b % 10
   sum += c ** 3
   b //= 10
   
if a == sum:
   print(a,"Armstronqdur")
else:
   print(a,"Armstronq deyil")

print("*********")
##Tapsiriq 5

a = input("Eded daxil edin:")

b = a[::-1]

if a==b:
    print("Eded palidromdur")
else:
    print("Eded palidrom deyil")