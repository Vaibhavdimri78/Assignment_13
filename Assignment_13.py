#1_i& 2&3
"""a = ['java','c',34,'python','sql']
print(a,type(a[1]),type(a[2]),)
print(a[-1])
#4

list = ["java","sql","c","Flutter","python"]
a = input("enter the name that you want to replace sql with")
list[1]=a
print([list])

#6
l1=["java","sql","c"]
l2 =["c","cpp","NoSql"]
l1.append(l2)
print(l1)

#7 printing index value and name 
n = int(input("number of items in list"))
l1 = ['java','c','python','sql','cpp','sql']
i=0
while(i<=n):
    print("index number =",i, l1[i])
    i+=1
#8
l1 = ['java','c','python','sql','cpp','sql']
l2 = [1,4,5,67,234,0,78]
l2.sort()
l1.sort()
print(l2,l1)
#9
a =input("Enter you city name\n")
b =input("Enter you city name\n")
c =input("Enter you city name\n")
d =input("Enter you city name\n")
e =input("Enter you city name\n")
name=[a,b,c,d,e]
name.sort()
print(name)
"""
#10
n=input("enter the number")
for i in n:
    l1=[i]
    print(l1,end='')