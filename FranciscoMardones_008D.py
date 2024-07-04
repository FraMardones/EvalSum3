import csv
import time
import random
import os
try:
    with open ("pedidos.csv","x",newline="") as pedidos1:
        escritorpedidos = csv.writer(pedidos1)
        escritorpedidos.writerow([
            ["Nro.pedido","Cliente","Direccion","Sector","Saco 5kg","Saco 10kg","Saco 20kg"]
                                  ])
except FileExistsError:
    pass

try:
    with open ("pedidosSB.csv", "x", newline="") as sector1:
        escritorsbtxt = csv.writer(sector1)
        escritorsbtxt.writerow([
            ["Nro.pedido","Cliente","Direccion","Sector","Saco 5kg","Saco 10kg","Saco 20kg"]
                                ])
except FileExistsError:
    pass
try:
    with open ("pedidosCT.csv", "x", newline="") as sector2:
        escritorsCTtxt = csv.writer(sector2)
        escritorsCTtxt.writerow([
            ["Nro.pedido","Cliente","Direccion","Sector","Saco 5kg","Saco 10kg","Saco 20kg"]
                                ])
except FileExistsError:
    pass

try:
    with open ("pedidosBU.csv", "x", newline="") as sector3:
        escritorCTtxt = csv.writer(sector3)
        escritorCTtxt.writerow([
            ["Nro.pedido","Cliente","Direccion","Sector","Saco 5kg","Saco 10kg","Saco 20kg"]
                                ])
except FileExistsError:
        pass


def registropedidos():
    os.system("cls")
    saco5kg = 0
    saco10kg = 0
    saco20kg = 0
    cantidad = 0
    sector = 0
    numeropedido = random.randint(1,1000)
    cliente = input("Ingrese su nombre y apellido: ")
    direccion = input("Ingrese su direccion: ")
    while True:   
        sector = int(input("Ingrese su sector\n1.San Bernardo\n2.Calera de Tango\n3.Buin\nSeleccione: "))
        if sector == 1:
            sector = "San Bernardo"
            break
        elif sector == 2:
            sector = "Calera de Tango"
            break
        elif sector == 3:
            sector = "Buin"
            break
        else:
            print("Ingrese una opcion valida")
    otromas = 0
    while otromas != 2:        
        comida = int(input("¿Que sacos quiere?\n1.Saco 5kg\n2.Saco 10kg\n3.Saco 20kg\n"))
        if comida == 1:
            cantidad = int(input("Cuantos sacos quiere?\n"))
            saco5kg += cantidad
            otromas = int(input("¿Quiere otro tipo de comida? 1(si)/2(no)\nElija: "))
        elif comida == 2:
            cantidad = int(input("Cuantos sacos quiere?\n"))
            saco10kg += cantidad
            otromas = int(input("¿Quiere otro tipo de comida? 1(si)/2(no)\nElija: "))
        elif comida == 3:
            cantidad = int(input("Cuantos sacos quiere?\n"))
            saco20kg += cantidad
            otromas = int(input("¿Quiere otro tipo de comida? 1(si)/2(no)\nElija: "))
        else:
            print("Debe ingresar un numero entero positivo")
    with open ("pedidos.csv","a",newline="") as pedidos1:
        escritorpedidos = csv.writer(pedidos1)
        escritorpedidos.writerows([
            [numeropedido,cliente,direccion,sector,saco5kg,saco10kg,saco20kg]
        ])
    if sector == 1:
        with open ("pedidosSB.csv","a",newline="") as sector1:
            escritorpedidos = csv.writer(sector1)
            escritorpedidos.writerows([
            [numeropedido,cliente,direccion,sector,saco5kg,saco10kg,saco20kg] 
            ])   
    elif sector == 2:
        with open ("pedidosCT.csv","a",newline="") as sector2:
            escritorCTtxt = csv.writer(sector2)
            escritorCTtxt.writerows([
            [numeropedido,cliente,direccion,sector,saco5kg,saco10kg,saco20kg] 
            ])   
    elif sector == 3:
        with open ("pedidosBU.csv","a",newline="") as sector3:
            escritorCTtxt = csv.writer(sector3)
            escritorCTtxt.writerows([
            [numeropedido,cliente,direccion,sector,saco5kg,saco10kg,saco20kg] 
            ])   

    print("Ha sido registrado con exito")

def listado():
    time.sleep(1)
    print("Cargando...")
    with open ("pedidos.csv", "r",newline="") as pedidos:
        lectorpedidos = csv.reader(pedidos)
        for i in lectorpedidos:
            print(*i)
        

def hojaDeRuta():
    os.system("cls")
    ruta = int(input("Que ruta quiere ver?\n1.San Bernardo\n2.Calera de Tango\n3.Buin\nSeleccione: "))
    if ruta == 1:
        print("Cargando...")
        time.sleep(1)
        with open ("pedidosSB.txt", "r",newline="") as sector1:
            lectorSBtxt = csv.reader(sector1)
            for i in lectorSBtxt:
                print(*i)
                time.sleep(1)
    elif ruta == 2:
        print("Cargando...")
        time.sleep(1)
        with open ("pedidosCT.txt", "r",newline="") as sector2:
            lectorCTtxt = csv.reader(sector2)
            for i in lectorCTtxt:
                print(*i)
                time.sleep(1)
    elif ruta == 3:
        print("Cargando...")
        time.sleep(1)
        with open ("pedidosBU.txt", "r",newline="") as sector3:
            lectorBUtxt = csv.reader(sector3)
            for i in lectorBUtxt:
                print(*i)

def menu():
    while True:    
        opc = int(input("Bienvenido a CatPremium!!\n-------------------\nElija una opcion porfavor\n1.Registrar pedido\n2.Listar todos los pedidos\n3.Imprimir hoja de ruta\n4.Salir del programa\n-----------------\nSeleccione: "))
        if opc == 1:
            registropedidos()
        elif opc == 2:
            listado()
        elif opc == 3:
            hojaDeRuta()
        elif opc == 4:
            print("Nos vemos!!")
            break
        else:
            print("Elija una opcion valida")
            time.sleep(2)
            os.system("cls")
menu()
