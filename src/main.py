import cups
import json
import os
import mimetypes
import time
import shutil
from rich import box
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

os.system("clear")

largura = shutil.get_terminal_size().columns
reset = "\033[0m"
textc = "\033[38;5;16m"
vermelho = "\033[48;5;196m" 
amarelo  = "\033[48;5;226m"
verde    = "\033[48;5;46m" 

console = Console()

console.print("="*largura)
print(("ᕕ( ᐛ )ᕗ  ~  P R I N T E R G E I S T  ~  ᕕ( ᐛ )ᕗ").center(largura))
print(("Copyright (c) 2025 mvghasty - https://github.com/mvghasty/printergeist").center(largura))
print(("LICENSE: GNU General Public License, 2.0").center(largura))
print("="*largura)

def format_bytes(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"

conn = cups.Connection()
printers = conn.getPrinters()

printer_name = None
for name in printers:
    if "L3250" in name.upper() or "EPSON" in name.upper():
        printer_name = name
        break

if not printer_name:
    print(f"{vermelho}{textc} [	ಠ_ಠ ] - ERROR: Impressora Epson L3250 não encontrada.{reset}")
    exit(1)

file_path = input("[  π  ] - Digite o nome ou caminho do arquivo que deseja imprimir: ").strip()

if not os.path.isfile(file_path):
    error_table_input = Table(title="\n[ ಠ_ಠ ] ! ERROR ! [ ಠ_ಠ ]", box=None, title_style="bold black on red")
    error_table_input.add_column("INPUT_ERROR", justify="center", header_style="bold black on red", style="bold black on red")
    error_table_input.add_row(
        f"Arquivo '{file_path}' não encontrado.\n"
    )
    console.print(error_table_input)
    exit(1)

os.system("clear")
mime_type, _ = mimetypes.guess_type(file_path)
file_size = os.path.getsize(file_path)
file_name = os.path.basename(file_path)

is_color = not ("gray" in printer_name.lower() or "bw" in printer_name.lower())

table = Table(title=" (⌐⊙_⊙) Detalhes da Impressão", box=box.HORIZONTALS, border_style="black on yellow", title_style="bold black on yellow")
table.add_column("Arquivo", style="dark_green on yellow", header_style="bold black on yellow")
table.add_column("Tipo", justify="center", style="dark_green on yellow", header_style="bold black on yellow")
table.add_column("Tamanho", justify="right", style="dark_green on yellow", header_style="bold black on yellow")
table.add_column("Colorido", justify="center", style="dark_green on yellow", header_style="bold black on yellow")

table.add_row(
    file_name,
    mime_type or "desconhecido",
    format_bytes(file_size),
    "Sim" if is_color else "Não"
)

console.print("="*largura)
print(("CUPS REQUEST").center(largura))
print("="*largura)
console.print(table)

with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    transient=True,
) as progress:
    progress.add_task(description=f"Enviando request para a impressora {printer_name}...", total=None)
    try:
        job_id = conn.printFile(
            printer_name,
            file_path,
            "REQUEST VIA PRINTERGEIST",
            {"document-format": mime_type or "application/octet-stream"}
        )
        time.sleep(2)
    except cups.IPPError as e:
        error_table_press = Table(title="\n[ ಠ_ಠ ] ! ERROR ! [ ಠ_ಠ ]", box=None, title_style="bold black on red")
        error_table_press.add_column("REQUEST_ERROR", justify="center", header_style="bold black on red", style="bold black on red")
        error_table_press.add_row(
            f"Erro ao enviar impressão: {e}\n"
        )
        console.print(error_table_press)
        exit(1)
console.print(f"\n[bold bright_white on green][ (^‿^) ] - Impressão enviada com sucesso! Job ID: {job_id} [/bold bright_white on green]\n")
console.print("="*largura)
print(("CUPS DEBUG-LOG").center(largura))
print(("(JSON FILE FORMAT)").center(largura))
print("="*largura)
console.print(json.dumps(printers, indent=4, separators=(", ", " = ")), style="dim")
print("="*largura)
