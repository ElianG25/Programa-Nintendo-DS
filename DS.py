pan = 0
comp = 0
bat = 0
resp = 0
resc = 0
resb = 0
res = 0

pan = int(input("Cuantas pantallas tiene?:"))
if (pan < 2):
    input ("No tiene suficientes pantallas para armar su Nintendo DS")
else:
    resp = pan / 2
comp = int(input("Cuantos componentes electronicos tiene?:"))
bat = int(input("Cuantas celdas de baterias tiene?:"))

if (pan < 2):
    print ("No tiene suficientes pantallas para armar su Nintendo DS")
else:
    resp = pan / 2

if (comp < 3):
    print ("No tiene suficientes componentes electronicos para armar su Nintendo DS")
else:
    resc = comp / 3

if (bat < 8):
    print ("No tiene suficientes celdas de baterias para armar su Nintendo DS")
else:
    resb = pan / 8

if (resp < resc) or (resp < resb):
    res = resp

elif (resc < resp) or (resc < resb):
    res = resc

elif (resb < resc) or (resb < resc):
    res = resc

print ("Usted puede armar",int(res),"Nintendo(s) DS con lo que tiene")

if int(res) % 2 == 0:
    print("Su resultado es par")
else:
    print("Su resultado NO es par")
