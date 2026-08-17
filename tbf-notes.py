#!/usr/bin/env python3
# ============================================
#   TBF-Notes v2.5 PRO
#   by TBFPUMBA — Technology. Security. Efficiency.
# ============================================

import os
import subprocess
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from pyfiglet import Figlet

console = Console()
NOTES_DIR = os.path.expanduser("~/.tbf_notes")
os.makedirs(NOTES_DIR, exist_ok=True)

def clear():
    os.system("clear")

def show_banner():
    f = Figlet(font='slant')
    ascii_banner = f.renderText('TBF - NOTES')
    console.print(Panel(
        f"[bold magenta]{ascii_banner}[/bold magenta]"
        "[bold cyan]🔥 TBF-Notes v2.5 PRO — Terminal Fast Notes[/bold cyan]\n"
        "[bold yellow]⚡ by TBFPUMBA — Technology. Security. Efficiency.[/bold yellow]",
        border_style="cyan",
        expand=False
    ))

def show_menu():
    table = Table(title="[bold green]📂 Меню управления[/bold green]", show_header=False, expand=True)
    table.add_column("Key", style="bold yellow", width=4)
    table.add_column("Action", style="bold white")

    table.add_row("1", "📝 Создать заметку")
    table.add_row("2", "📋 Показать все заметки")
    table.add_row("3", "🔍 Поиск в заметках")
    table.add_row("4", "✏️ Редактировать заметку (nano)")
    table.add_row("5", "🗑️ Удалить заметку")
    table.add_row("6", "❌ Выход")
    
    console.print(table)
    return Prompt.ask("\n👉 [bold cyan]Выберите действие[/bold cyan]", choices=["1", "2", "3", "4", "5", "6"])

def create_note():
    console.print("\n[bold cyan]📝 Создание новой заметки[/bold cyan]")
    title = Prompt.ask("Введите название заметки").strip()
    if not title:
        console.print("[bold red]❌ Название не может быть пустым![/bold red]")
        return

    filename = os.path.join(NOTES_DIR, title.replace(" ", "_") + ".txt")
    if os.path.exists(filename):
        console.print(f"[bold red]❌ Заметка с таким названием уже существует![/bold red]")
        return

    console.print("[dim]✏️ Введите текст заметки (Ctrl+D для завершения):[/dim]")
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    console.print(f"[bold green]✅ Заметка '{title}' успешно сохранена![/bold green]")

def show_notes():
    notes = [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]
    if not notes:
        console.print("\n[bold yellow]📭 Заметок нет.[/bold yellow]")
        Prompt.ask("\n[dim]Нажмите Enter...[/dim]")
        return

    table = Table(title="[bold cyan]📋 Все заметки[/bold cyan]", expand=True)
    table.add_column("№", style="cyan", justify="center", width=4)
    table.add_column("Название", style="bold yellow")
    table.add_column("Символов", style="green", justify="right")
    table.add_column("Первые 100 символов", style="dim white")

    for i, note in enumerate(notes, 1):
        title = note.replace("_", " ").replace(".txt", "")
        filepath = os.path.join(NOTES_DIR, note)
        size = str(os.path.getsize(filepath))
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read(100).replace("\n", " ")
        table.add_row(str(i), title, size, content + "...")

    console.print(table)
    Prompt.ask("\n[dim]Нажмите Enter...[/dim]")

def search_notes():
    search_term = Prompt.ask("\n🔍 [bold cyan]Введите слово для поиска[/bold cyan]")
    found = 0

    for note in os.listdir(NOTES_DIR):
        if not note.endswith(".txt"):
            continue
        filepath = os.path.join(NOTES_DIR, note)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            if search_term.lower() in content.lower():
                title = note.replace("_", " ").replace(".txt", "")
                console.print(Panel(
                    f"[bold green]✅ Найдено в: {title}[/bold green]\n" +
                    "\n".join([line.replace(search_term, f"[bold red]{search_term}[/bold red]") 
                               for line in content.split("\n") if search_term.lower() in line.lower()]),
                    border_style="yellow"
                ))
                found += 1

    if found == 0:
        console.print("[bold yellow]❌ Ничего не найдено.[/bold yellow]")

    Prompt.ask("\n[dim]Нажмите Enter...[/dim]")

def edit_note():
    notes = [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]
    if not notes:
        console.print("\n[bold yellow]📭 Заметок нет.[/bold yellow]")
        return

    console.print("\n[bold cyan]✏️ Выберите заметку для редактирования:[/bold cyan]")
    for i, note in enumerate(notes, 1):
        console.print(f"  [bold yellow]{i}.[/bold yellow] {note.replace('_', ' ').replace('.txt', '')}")

    choice = Prompt.ask("👉 Номер", default="1")
    if choice.isdigit() and 1 <= int(choice) <= len(notes):
        subprocess.run(["nano", os.path.join(NOTES_DIR, notes[int(choice) - 1])])
        console.print("[bold green]✅ Заметка сохранена![/bold green]")
    else:
        console.print("[bold red]❌ Неверный выбор.[/bold red]")

def delete_note():
    notes = [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]
    if not notes:
        console.print("\n[bold yellow]📭 Заметок нет.[/bold yellow]")
        return

    console.print("\n[bold cyan]🗑️ Выберите заметку для удаления:[/bold cyan]")
    for i, note in enumerate(notes, 1):
        console.print(f"  [bold yellow]{i}.[/bold yellow] {note.replace('_', ' ').replace('.txt', '')}")

    choice = Prompt.ask("👉 Номер")
    if choice.isdigit() and 1 <= int(choice) <= len(notes):
        title = notes[int(choice) - 1].replace("_", " ").replace(".txt", "")
        if Confirm.ask(f"Удалить '{title}'?"):
            os.remove(os.path.join(NOTES_DIR, notes[int(choice) - 1]))
            console.print("[bold green]✅ Заметка удалена.[/bold green]")
        else:
            console.print("[bold yellow]❌ Отменено.[/bold yellow]")
    else:
        console.print("[bold red]❌ Неверный выбор.[/bold red]")

def main():
    while True:
        clear()
        show_banner()
        choice = show_menu()
        
        if choice == "1":
            create_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            console.print("[bold green]👋 Спасибо за использование TBF-Notes![/bold green]")
            sys.exit(0)

if __name__ == "__main__":
    main()
    
