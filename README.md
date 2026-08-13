# 📝 TBF-Notes v2.5 PRO

<p align="center">
  <img src="https://img.shields.io/badge/License-Apache--2.0-brightgreen.svg" alt="License">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-orange.svg" alt="Platform">
  <img src="https://img.shields.io/badge/UI-Rich%20%2F%20Cyberpunk-magenta.svg" alt="UI Style">
</p>

> **Terminal-Based Fast Notes Manager** — быстрая, функциональная и удобная консольная утилита для работы с заметками прямо из терминала.

---

## ✨ Основные возможности

- 🎨 **Rich Cyberpunk UI:** Интерактивные таблицы, аккуратные панели и сочные цвета.
- 📝 **Создание и редактор:** Быстрое создание заметок или редактирование через встроенный `nano`.
- 🔍 **Полнотекстовый поиск:** Мгновенный поиск слов по всем файлам с подсветкой найденого фрагмента.
- 📋 **Предпросмотр:** Таблица со всеми заметками, их размером и первыми 100 символами текста.
- 💾 **Автосохранение:** Все файлы автоматически складываются в директорию `~/.tbf_notes/`.

---

## 🛠️ Зависимости

Интерфейс использует следующие библиотеки:
- `rich`
- `pyfiglet`

---

## 🚀 Быстрый запуск

```bash
git clone https://github.com/cocofembo-glitch/TBF-Notes.git && cd TBF-Notes && pip install -r requirements.txt && python tbf-notes.py
