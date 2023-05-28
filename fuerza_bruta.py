from string import ascii_letters, digits
from itertools import product
from time import time

caracteres = ascii_letters+ digits

def buscador (con):
    archivo = open("combinaciones.txt", "w")

    if 3<= len(con) <=4:
        for i in range(3,5):
            for comb in product (caracteres, repeat = i):
                prueba = "".join(comb)
                archivo.write(prueba + "\n")
                if prueba == con:
                    print("Tu contraseña es {}".format(prueba))
                    archivo.close()
                    break
    else:
        print ("Ingresa una contraseña que contenga de 3 a 4 caracteres")


t0 = time()
con = '9999'
buscador(con)
t1 = time()
print ("Tiempo de ejecución: {}".format(round(t1-t0, 4)))

