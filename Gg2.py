import calendar
import tkinter as tk
from tkinter import ttk
from tkinter import font  # импортируем модуль для работы со шрифтами

class CalendarApp:
    def init(self, root):  # исправлено имя конструктора
        self.root = root
        self.root.title("Календарь")

        self.year = tk.IntVar(value=2025)
        self.month = tk.IntVar(value=5)

        self.year_label = ttk.Label(root, text="Год:")
        self.year_label.grid(row=0, column=0, padx=5, pady=5)
        self.year_entry = ttk.Entry(root, textvariable=self.year, width=6)
        self.year_entry.grid(row=0, column=1, padx=5, pady=5)

        self.month_label = ttk.Label(root, text="Месяц:")
        self.month_label.grid(row=0, column=2, padx=5, pady=5)
        self.month_entry = ttk.Entry(root, textvariable=self.month, width=3)
        self.month_entry.grid(row=0, column=3, padx=5, pady=5)

        self.show_button = ttk.Button(root, text="Показать", command=self.show_calendar)
        self.show_button.grid(row=0, column=4, padx=5, pady=5)

        # Увеличиваем шрифт для календаря
        self.calendar_font = font.Font(family="Courier New", size=16)  # моноширинный шрифт для ровного отображения

        self.calendar_text = tk.Text(root, width=30, height=10, font=self.calendar_font)
        self.calendar_text.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

    def show_calendar(self):
        year = self.year.get()
        month = self.month.get()

        try:
            year = int(year)
            month = int(month)
            if not (1 <= month <= 12):
                raise ValueError
        except ValueError:
            self.calendar_text.delete("1.0", tk.END)
            self.calendar_text.insert(tk.END, "Некорректный год или месяц")
            return

        cal = calendar.month(year, month)
        self.calendar_text.delete("1.0", tk.END)
        self.calendar_text.insert(tk.END, cal)

if name == "main":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
