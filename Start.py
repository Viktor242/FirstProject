# Импорт библиотек
import tkinter as tk
from tkinter import ttk
from services import add_task, delete_task, mark_task_1, mark_task_2, mark_task_3
from tkcalendar import Calendar

# Создание главного окна
root = tk.Tk()
root.title("Управление задачами-Канбан")
root.geometry("800x600")

# Метка для ввода задачи
text1 = tk.Label(root, text="Пропиши задачу", font=("Arial", 14)).pack(pady=20)

# Поле ввода задачи
entry = tk.Entry(root, width=30)
entry.pack(pady=25, ipadx=100)

# Кнопка добавления задачи
button1 = tk.Button(root, text="Добавить задачу", font=("Arial", 10), command=lambda: add_task(entry, task_listBox))
button1.place(x=210, y=150)

# Кнопка удаления задачи
button2 = tk.Button(root, text="Удалить задачу", font=("Arial", 10), command=lambda: delete_task(task_listBox))
button2.place(x=500, y=150)

# Кнопки изменения статуса задач (примечание: все названы mark_button_1)
mark_button_1 = tk.Button(root, text="Отметить задачу в процессе", command=lambda: mark_task_1(task_listBox))
mark_button_1.place(x=100, y=500)

mark_button_1 = tk.Button(root, text="Отметить задачу выполненной", command=lambda: mark_task_2(task_listBox))
mark_button_1.place(x=280, y=500)

mark_button_1 = tk.Button(root, text="Отметить задачу просроченной", command=lambda: mark_task_3(task_listBox))
mark_button_1.place(x=500, y=500)

# Таблица для отображения задач
task_listBox = ttk.Treeview(root, columns=("Task1"), show="headings")
task_listBox.column("Task1", width=400)
task_listBox.heading("Task1", text="Текущие задачи")
task_listBox.place(x=200, y=250)

# Функция и кнопка для отображения календаря
def show_calendar():
    top = tk.Toplevel(root)
    top.title("Календарь")
    cal = Calendar(top, selectmode='day', year=2023, month=11, day=1)
    cal.pack(pady=20)
    close_btn = tk.Button(top, text="Закрыть", command=top.destroy)
    close_btn.pack(pady=10)

show_button = tk.Button(root, text="Показать календарь", command=show_calendar)
show_button.place(x=50, y=50)

# Запуск основного цикла приложения
root.mainloop()