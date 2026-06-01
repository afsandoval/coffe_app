from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box

console = Console()

def ver_historial():
    console.print(Rule("[bold #4B2C20]Historial de Pedidos[/bold #4B2C20]", style="#8B4513"))

    # Emojis asociados a cada café para la tabla
    EMOJIS = {
        "Espresso":   ":coffee:",
        "Cappuccino": ":steaming_bowl:",
        "Latte":      ":glass_of_milk:",
        "Americano":  ":droplet:",
        "Campesino":  ":ear_of_corn:",
    }

    try:
        with open("pedidos.txt", "r") as f:
            pedidos = [linea.strip() for linea in f.readlines() if linea.strip()]

        if not pedidos:
            console.print(Panel(
                ":information: [yellow]Aún no hay ningún pedido registrado.[/yellow]",
                border_style="yellow",
                padding=(0, 3),
            ))
            return

        # ── Tabla de historial ────────────────────────────────
        tabla = Table(
            title=f":clipboard: [bold]{len(pedidos)} pedido(s) registrado(s)[/bold]",
            box=box.ROUNDED,
            border_style="#8B4513",
            header_style="bold white on #4B2C20",
            show_lines=True,
            padding=(0, 2),
        )
        tabla.add_column("#",       justify="center", width=5)
        tabla.add_column("Bebida",  justify="left",   min_width=18)

        for i, pedido in enumerate(pedidos, start=1):
            emoji = EMOJIS.get(pedido, ":coffee:")
            fila_estilo = "on grey11" if i % 2 == 0 else ""
            tabla.add_row(
                f"[dim]{i}[/dim]",
                f"{emoji} {pedido}",
                style=fila_estilo,
            )

        console.print(tabla)

    except FileNotFoundError:
        console.print(Panel(
            ":warning: [bold red]No existe historial de pedidos todavía.[/bold red]\n"
            "[dim]Haz tu primer pedido y aparecerá aquí.[/dim]",
            border_style="red",
            padding=(0, 3),
        ))