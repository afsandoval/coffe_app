import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.rule import Rule
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich import box

console = Console()

# Catálogo de cafés: nombre, emoji, precio
CAFES = {
    "1": ("Espresso",   ":coffee:",            2500),
    "2": ("Cappuccino", ":steaming_bowl:",      5800),
    "3": ("Latte",      ":glass_of_milk:",      6200),
    "4": ("Americano",  ":droplet:",            4500),
    "5": ("Campesino",  ":ear_of_corn:",        3000),
}

def pedir_cafe():
    console.print(Rule("[bold #8B4513]Selecciona tu Café[/bold #8B4513]", style="#8B4513"))

    # ── Tabla del catálogo de bebidas ─────────────────────────
    tabla = Table(
        box=box.SIMPLE,
        header_style="bold white on #4B2C20",
        border_style="#8B4513",
        padding=(0, 2),
    )
    tabla.add_column("Opción",  justify="center", width=8)
    tabla.add_column("Bebida",  justify="left",   min_width=16)
    tabla.add_column("Precio",  justify="right",  min_width=12)

    for opcion, (nombre, emoji, precio) in CAFES.items():
        tabla.add_row(
            f"[bold yellow]{opcion}[/bold yellow]",
            f"{emoji} {nombre}",
            f"[green]${precio:,}[/green]",
        )

    console.print(tabla)

    # ── Leer opción del usuario ───────────────────────────────
    opcion = console.input("[bold yellow]▶ Opción Café:[/bold yellow] ").strip()

    if opcion in CAFES:
        nombre, emoji, precio = CAFES[opcion]

        # ── Barra de progreso: preparando el café ─────────────
        console.print()
        with Progress(
            SpinnerColumn("bouncingBall"),
            TextColumn(f"[bold #8B4513]Preparando tu {nombre}..."),
            BarColumn(bar_width=28, style="#8B4513", complete_style="green"),
            console=console,
            transient=True,          # desaparece al terminar
        ) as progress:
            tarea = progress.add_task("preparando", total=20)
            while not progress.finished:
                time.sleep(0.07)
                progress.advance(tarea)

        # ── Confirmación del pedido ───────────────────────────
        console.print(Panel(
            f":white_check_mark: [bold white]¡Pedido confirmado![/bold white]\n\n"
            f"  {emoji} [bold]{nombre}[/bold]\n"
            f"  [dim]Precio:[/dim] [bold green]${precio:,} COP[/bold green]",
            border_style="green",
            padding=(1, 4),
        ))

        # Guardar en archivo
        with open("pedidos.txt", "a") as f:
            f.write(nombre + "\n")
    else:
        console.print("[bold red]⚠  Opción no válida. Intenta de nuevo.[/bold red]")