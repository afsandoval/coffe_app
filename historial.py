def ver_historial():
    try:
        print("\n Historial de Pedidos")
        
        with open("pedidos.txt", "r") as file:
            pedidos = file.readlines()
            if pedidos:
                for indice, pedido in enumerate(pedidos, start=1):  #Enumerate: indica el Indice y el contenido de una Linea
                    print(str(indice) + ". " + pedido.strip())
            else:
                print("Aun no hay ningun pedido")
    except FileNotFoundError:
        print("\n No existe Historial de Pedidos")