from math import *

m1=1
m2=1
l1=1
l2=0.5
g=9.8

tita1=[-120.0, -120.69, -121.92, -122.43, -120.96, -116.25, -107.04, -92.07, -70.08, -39.81, 0.0]
tita1d=[0,-2.34,-2.16,0.54,5.76,13.5,23.76,36.54,51.84,69.66,90]
tita1dd=[-7.2,-2.14,2.92,7.98,13.04,18.1,23.16,28.22,33.28,38.34,43.4]

tita2=[15,17.1,22.8,31.2,41.4,52.5,63.6,73.8,82.2,87.9,90]
tita2d=[0,8.1,14.4,18.9,21.6,22.5,21.6,18.9,14.4,8.1,0]
tita2dd=[18,14.4,10.8,7.2,3.6,0,-3.6,-7.2,-10.8,-14.4,-18]

#print(tan(radians(45)))
def i11(i):
    s=m1*l1*l1/3
    s+=m2*l1*l1
    s+=m2*l2*l2/3
    c2=cos(radians(tita2[i]))
    s+=m2*l1*l2*c2
    return s

def i12(i):
    s=m2*l2*l2/3
    c2=cos(radians(tita2[i]))
    s+=m2*l1*l2*c2/2
    return s

def i22(i):
    return m2*l2*l2/3

def h1(i):
    s2=sin(radians(tita2[i]))
    add=tita1d[i]+0.5*tita2d[i]
    s=-m2*l1*l2*s2*tita1d[i]*add
    return s
def h2(i):
    s2=sin(radians(tita2[i]))
    s=m2*l1*l2*s2*tita1d[i]*tita1d[i]
    return s

def y1(i):
    c1=cos(radians(tita1[i]))
    s=0.5*m1*g*l1*c1
    c12=cos(radians(tita1[i]+tita2[i]))
    add=l1*c1+0.5*l2*c12
    s+=m2*g*add
    return s

def y2(i):
    c12=cos(radians(tita1[i]+tita2[i]))
    return 0.5*m2*9.8*l2*c12

print("tme : i11  i12  i22  I1  I2  h1  h2  y1  y2  r1  r2")
for i in range(0,11):
    print(i/2," : ",end='')
    print(i12(i)*tita1dd[i]+i22(i)*tita2dd[i]+h2(i)+y2(i))






