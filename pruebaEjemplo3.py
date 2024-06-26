def menu_principal():
    print("1) Registrar pedido")
    print("2) Listar pedidos")
    print("3) Imprimir hoja de ruta")
    print("4) Salir")


def imprimir_por_comuna(comuna_buscada):
    for pedido in l_pedidos:
        if pedido[3] == comuna_buscada:
            print(pedido)

def registrar_pedido():
    nombre = input("Ingrese nombre")
    apellido = input("Ingrese apellido")
    direccion = input("Ingrese direccion")
    comuna = input("Ingrese comuna")
    c5 = input("Ingrese cantidad balones de 5k")
    c15 = input("Ingrese cantidad balones de 15k")
    c45 = input("Ingrese cantidad balones de 45k")
    L=[nombre,apellido,direccion,comuna,c5,c15,c45]
    l_pedidos.append(L)
def imprimir_listado_general():
    for pedido in l_pedidos:
        print(pedido)

l_pedidos = [['pepe', 'papa', 'villa dulce', 'viña', '1', '2', '0'],['Juan', 'Gomez', 'Estrella polar', 'quilpue', '0', '2', '1']]

while True:
    menu_principal()
    op = input("Ingrese una opcion")

    if op =="4":
        print("Saliendo del programa")
    elif op =="1":
        registrar_pedido()
    elif op =="2":
        imprimir_listado_general()
    elif op =="3":
        comunaBuscada = input("Ingrese la comuna que desea listar")
        imprimir_por_comuna(comunaBuscada)
