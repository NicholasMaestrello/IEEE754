#banin
import math

def sepa(x):
    return math.modf(x)
def bint(x):
    f=""

    if x==0:
        f="0"
    else:
        while(x>0):
            f=f+str(x%2)
            x=x//2
        
    return f[::-1]

def bdec(x):
    g=""
    for i in range(32):
        x*=2
        y=int(x)
        if y==1:
            g=g+str(y)
            x=x-1
        else:
            g=g+str(y)
    return g

def hint(x):
    while len(x)<32:
        x=x+"0"
    nhex=""
    num={'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
    while len(x)%4!=0:
        x=x[::-1]
        x=x+"0"
        x=x[::-1]
    for i in range(len(x)//4):
        for j in num:
            if x[(i*4):(i+1)*4] == j:
                nhex=nhex+num[j]
    return nhex
        

def n31(x):
    while len(x) < 31:
        x=x+"0"
    return x
def sinal(x):
    if x>0:
        y=0
    else:
        y=1
    return y

#main()
numero=float(input("digite um numero: "))
if numero ==0:
    bza="00000000"
    print("numero em HEXA :",bza)
else:
    bza=str((sinal(numero)))
    if numero < 0:
        numero=numero*(-1)
    x=int(sepa(numero)[1])
    y=sepa(numero)[0]
    ultb=bdec(y)
    a=bint(x)+","+bdec(y)
    a=a.replace(",", ".")
    c=a
    c=c.split(".")
    if int(c[0])>=1:
        expo=len(c[0])-1
        g=c[0][0]+"."+c[0][1:]+c[1]
    else:
        expo=(len(c[1].split("1")[0])+1)*-1
        g=c[1][(expo*-1)-1]+"."+c[1][(expo*-1):]
    g=g.split(".")[1]
    expo=int(expo)+127
    expo=bint(expo)

    if len(expo)<8:
        auxi=expo[::-1]
        auxi=auxi+"0"
        expo=auxi[::-1]
    bza=bza+expo+g
    bza=bza[0:32]
    bza=hint(bza)
    print("numero final em HEXA:",bza)


