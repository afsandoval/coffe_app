from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.rule import Rule
from rich import box

console = Console()

def mostrar_menu():
    # ── Encabezado de bienvenida ──────────────────────────────
    console.print()
    console.print(Panel(
        ":coffee: [bold white]Bienvenido a la Cafetería ADSO[/bold white] :coffee:\n"
        "[dim]El mejor café de todo el programa[/dim]",
        border_style="bold green",
        padding=(1, 6),
    ))

    # ── Tabla de opciones del menú principal ─────────────────
    tabla = Table(
        box=box.ROUNDED,
        border_style="green",
        header_style="bold white on dark_green",
        show_header=True,
        padding=(0, 2),
    )
    tabla.add_column("Opción", justify="center", width=8)
    tabla.add_column("Acción",  justify="left",   min_width=24)

    tabla.add_row("[bold yellow]1[/bold yellow]", ":cup_with_straw: Pedir Café")
    tabla.add_row("[bold yellow]2[/bold yellow]", ":clipboard:       Ver Historial de Pedidos")
    tabla.add_row("[bold red]3[/bold red]",        ":door:            Salir")

    console.print(tabla)
    console.print()