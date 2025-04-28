import tkinter as tk
from tkinter import ttk
from services import add_task, delete_task


# Создание главного окна
root = tk.Tk()
root.title("Управление задачами")
root.geometry("500x600")

# Метка для ввода задачи
text1 = tk.Label(root, text="Пропиши задачу", font=("Arial", 14)).pack(pady=20)

# Поле ввода задачи
entry = tk.Entry(root, width=30)
entry.pack(pady=25, ipadx=100)

# Кнопка добавления задачи
button1 = tk.Button(root, text="Добавить задачу", command=lambda: add_task(entry, task_listBox))
button1.place(x=50, y=150)

# Кнопка удаления задачи
button2 = tk.Button(root, text="Удалить задачу", command=lambda: delete_task(task_listBox))
button2.place(x=200, y=150)

# Таблица для отображения задач
task_listBox = ttk.Treeview(root, columns=("Task1", "Status"), show="headings")
task_listBox.column("Task1", width=200)
task_listBox.heading("Task1", text="Текущие задачи")
# Добавляем столбец для статуса
task_listBox.column("Status", width=100)
task_listBox.heading("Status", text="Статус")
task_listBox.place(x=100, y=250)

# Стилизация таблицы
style = ttk.Style()
style.configure("Treeview.Heading", foreground="blue")

# Создаем выпадающий список для изменения статуса
status_options = ["В процессе", "Выполнено", "Просрочено"]
status_var = tk.StringVar()
status_combobox = ttk.Combobox(root, textvariable=status_var, values=status_options, state="readonly")
status_combobox.place(x=310, y=200)
status_combobox.set("Выбрать статус")

# Функция для изменения статуса выбранной задачи
def change_status():
    selected_item = task_listBox.selection()
    if selected_item:
        task_listBox.set(selected_item, column="Status", value=status_var.get())

# Кнопка для применения изменения статуса
change_status_button = tk.Button(root, text="Изменить статус", command=change_status)
change_status_button.place(x=350, y=150)

# Запуск основного цикла приложения
root.mainloop()