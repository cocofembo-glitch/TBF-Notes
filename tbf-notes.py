#!/data/data/com.termux/files/usr/bin/python

import os
import subprocess
import sys

NOTES_DIR = os.path.expanduser("~/.tbf_notes")
os.makedirs(NOTES_DIR, exist_ok=True)

# Кольори (ANSI)
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"

def clear():
    os.system("clear")

def show_banner():
    print(f"""{PURPLE}{BOLD}
    ████████╗██████╗ ███████╗    ███╗   ██╗ ██████╗ ████████╗███████╗███████╗
    ╚══██╔══╝██╔══██╗██╔════╝    ████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝██╔════╝
       ██║   ██████╔╝█████╗      ██╔██╗ ██║██║   ██║   ██║   █████╗  ███████╗
       ██║   ██╔══██╗██╔══╝      ██║╚██╗██║██║   ██║   ██║   ██╔══╝  ╚════██║
       ██║   ██████╔╝██║         ██║ ╚████║╚██████╔╝   ██║   ███████╗███████║
       ╚═╝   ╚═════╝ ╚═╝         ╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝
{RESET}""")
    print(f"{CYAN}╔══════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{RESET} {BOLD}🔥 TBF-Notes v2.0{RESET}                                              {CYAN}║{RESET}")
    print(f"{CYAN}║{RESET} {BOLD}⚡ by TBFPUMBA — Technology. Security. Efficiency.{RESET}              {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════════════╝{RESET}")
    print()

def show_menu():
    print(f"{GREEN}📂 Виберіть дію:{RESET}")
    print(f"  {YELLOW}1.{RESET} 📝 Створити нотатку")
    print(f"  {YELLOW}2.{RESET} 📋 Показати всі нотатки")
    print(f"  {YELLOW}3.{RESET} 🔍 Пошук у нотатках")
    print(f"  {YELLOW}4.{RESET} ✏️ Редагувати нотатку")
    print(f"  {YELLOW}5.{RESET} 🗑️ Видалити нотатку")
    print(f"  {YELLOW}6.{RESET} ❌ Вихід")
    print()
    return input("👉 Виберіть (1-6): ")

def create_note():
    print()
    title = input("📝 Введіть назву нотатки: ")
    filename = os.path.join(NOTES_DIR, title.replace(" ", "_") + ".txt")
    
    if os.path.exists(filename):
        print(f"{RED}❌ Нотатка з такою назвою вже існує!{RESET}")
        return
    
    print(f"{GREEN}✏️ Введіть текст нотатки (Ctrl+D для завершення):{RESET}")
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    print(f"{GREEN}✅ Нотатку збережено!{RESET}")

def show_notes():
    print()
    print(f"{CYAN}📋 Всі нотатки:{RESET}")
    print("=" * 50)
    
    notes = [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]
    if not notes:
        print(f"{YELLOW}📭 Нотаток немає.{RESET}")
        input("Натисніть Enter...")
        return
    
    for i, note in enumerate(notes, 1):
        title = note.replace("_", " ").replace(".txt", "")
        size = os.path.getsize(os.path.join(NOTES_DIR, note))
        print(f"{GREEN}{i}.{RESET} {BOLD}{title}{RESET} ({size} символів)")
        with open(os.path.join(NOTES_DIR, note), "r") as f:
            content = f.read(100)
        print(f"   {BLUE}📄 Перші 100 символів:{RESET}")
        print(f"   {content}...")
        print()
    
    input("Натисніть Enter...")

def search_notes():
    print()
    search_term = input("🔍 Введіть слово для пошуку: ")
    print(f"{CYAN}🔍 Результати пошуку:{RESET}")
    print("=" * 50)
    
    found = 0
    for note in os.listdir(NOTES_DIR):
        if not note.endswith(".txt"):
            continue
        filepath = os.path.join(NOTES_DIR, note)
        with open(filepath, "r") as f:
            content = f.read()
            if search_term.lower() in content.lower():
                title = note.replace("_", " ").replace(".txt", "")
                print(f"{GREEN}✅ Знайдено в:{RESET} {BOLD}{title}{RESET}")
                for line in content.split("\n"):
                    if search_term.lower() in line.lower():
                        highlighted = line.replace(search_term, f"{RED}{search_term}{RESET}")
                        print(f"  {highlighted}")
                print()
                found += 1
    
    if found == 0:
        print(f"{YELLOW}❌ Нічого не знайдено.{RESET}")
    
    input("Натисніть Enter...")

def edit_note():
    notes = [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]
    if not notes:
        print(f"{YELLOW}📭 Нотаток немає.{RESET}")
        return
    
    print(f"{CYAN}✏️ Оберіть нотатку для редагування:{RESET}")
    for i, note in enumerate(notes, 1):
        print(f"  {i}. {note.replace('_', ' ').replace('.txt', '')}")
    
    try:
        choice = int(input("👉 Номер: ")) - 1
        if 0 <= choice < len(notes):
            subprocess.run(["nano", os.path.join(NOTES_DIR, notes[choice])])
            print(f"{GREEN}✅ Нотатку збережено!{RESET}")
        else:
            print(f"{RED}❌ Неправильний вибір.{RESET}")
    except ValueError:
        print(f"{RED}❌ Введіть число.{RESET}")

def delete_note():
    notes = [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]
    if not notes:
        print(f"{YELLOW}📭 Нотаток немає.{RESET}")
        return
    
    print(f"{CYAN}🗑️ Оберіть нотатку для видалення:{RESET}")
    for i, note in enumerate(notes, 1):
        print(f"  {i}. {note.replace('_', ' ').replace('.txt', '')}")
    
    try:
        choice = int(input("👉 Номер: ")) - 1
        if 0 <= choice < len(notes):
            title = notes[choice].replace("_", " ").replace(".txt", "")
            confirm = input(f"Видалити '{title}'? (y/n): ")
            if confirm.lower() == 'y':
                os.remove(os.path.join(NOTES_DIR, notes[choice]))
                print(f"{GREEN}✅ Нотатку видалено.{RESET}")
            else:
                print(f"{YELLOW}❌ Скасовано.{RESET}")
        else:
            print(f"{RED}❌ Неправильний вибір.{RESET}")
    except ValueError:
        print(f"{RED}❌ Введіть число.{RESET}")

def main():
    clear()
    show_banner()
    
    while True:
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
            print(f"{GREEN}👋 Дякуємо, що використовуєте TBF-Notes!{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}❌ Невірний вибір.{RESET}")

if __name__ == "__main__":
    main()
