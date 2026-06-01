from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

# Importar los módulos de la aplicación
from menu import mostrar_menu, console
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    # ── Pantalla de inicio ────────────────────────────────────
    console.clear()
    console.print(Panel(
        ":coffee:  [bold green]CAFETERÍA ADSO[/bold green]  :coffee:\n"
        "[dim]Sistema de Pedidos · Programa Análisis y Desarrollo de Software[/dim]",
        border_style="bold green",
        padding=(1, 8),
    ))

    while True:
        mostrar_menu()
        opcion = console.input("[bold green]▶ Selecciona una opción:[/bold green] ").strip()

        if opcion == "1":
            pedir_cafe()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            console.print()
            console.print(Rule(style="green"))
            console.print(Panel(
                ":wave: [bold white]¡Hasta pronto![/bold white]\n"
                "[dim]Gracias por visitar Cafetería ADSO :coffee:[/dim]",
                border_style="green",
                padding=(1, 6),
            ))
            break
        else:
            console.print("[bold red]⚠  Opción inválida. Elige 1, 2 o 3.[/bold red]")
            console.print()

if __name__ == "__main__":
    main()