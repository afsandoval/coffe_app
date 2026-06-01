from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion del Menú: ")

        if opcion == "1":
            pedir_cafe()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("\n Muchas gracias por haner tomado nuestros Cafés ")
            break
        else:
            print("Opcion invalida")


# Ejecuta el flujo principal el Archivo llamado main.py
if __name__ == "__main__":
    main()