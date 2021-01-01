import matplotlib.pyplot as plt


mylist=[32]
def func(a,x,b,c):
    return x*x*a+x*b+c
a = float(input("Введите постоянныq кофицент a>>"))
b = float(input("Введите постоянныq кофицент b>>"))
c = float(input("Введите постоянныq кофицент c>>"))
x = float(input("от x=>>"))
xk = float(input("до x=>>")) 
print("В каком диопазоне вывести график")
x1 = float(input("от x=>>"))
x2 = float(input("до x=>>")) 
x1z=x1
izi=str(input("Если точками то 1>>"))
if izi=="1":
    tochka=str('ro')
elif izi !=1:
    tochka=0

while x<=xk:
    y = func(a,x,b,c)
    print(x,"\t",y)
    x=x+1


i=[]
while x1!=x2:
    myglist=[88]
    myglist[0]=x1
    l=myglist
    i=i+l
    x1+=0.5
myglist[0]=x1
l=myglist
i=i+l

t=[]
while x1z<x2:
    mylist=[88]
    mylist[0]=x1z*x1z*a+b*x1z+c
    g=mylist
    t=t+g
    x1z+=0.5
myglist[0]=x1z*x1z*a+b*x1z+c
g=myglist
t=t+g
del mylist[0]
del myglist[0]
plt.title("Рисуночек")
plt.axis([-20,20,-20,20])
plt.plot(i,t,tochka)
plt.show()
plt.show()