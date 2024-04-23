from rich import box
from rich.table import Table


def create_table():

    table = Table(
        show_header=True,
        header_style="bold",
        title="Network Devices",
        title_style="bold",
        box=box.SIMPLE_HEAD,
        caption="Press [bold]'R'[/bold] to refresh the table",
        safe_box=True,
        padding=(0, 2),
        collapse_padding=True,
        pad_edge=True,
        style="blue",
        title_justify="left",
    )
    table.add_column("Ping", justify="center")
    table.add_column(
        "IPv4 Adress",
        width=12,
        style="bold",
    )
    table.add_column("MAC Address", justify="left", style="dim")
    table.add_column("Hostname", justify="left")
    table.add_column("Vendor", justify="left")
    return table
