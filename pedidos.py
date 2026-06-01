def pedir_cafe():
    print("\n Elige el Café que prefieras: ")
    print("1. Espresso")
    print("2. Cappucino")
    print("3. Latte")
    print("4. Americano")
    print("5. Campesino")

    opcion = input("Opcion Café: ")

    cafes = {
        "1": "Espresso",
        "2": "Cappucino",
        "3": "Latte",
        "4": "Americano",
        "5": "Campesino"
    }

    if opcion in cafes.keys():
        cafe_elegido = cafes[opcion]
        print(f"Has pedido un {cafe_elegido}")

        with open("pedidos.txt", "a") as file:
            file.write(cafe_elegido + "\n")
    else:
        print("Opcion no valida")