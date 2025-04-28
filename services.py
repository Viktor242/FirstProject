import tkinter as tk
from tkinter import ttk
task_listBox = ttk.Treeview


def add_task(entry, task_listBox):
 
    
    task_text = entry.get()  # Получаем текст задачи из поля ввода
    if task_text:  # Проверяем, что поле не пустое
        # Добавляем задачу в Treeview с начальным статусом "Не начата"
        task_listBox.insert("", "end", values=(task_text, "Не начата"))  
        entry.delete(0, tk.END)  # Очищаем поле ввода после добавления

def delete_task(task_listBox):

    selected_item = task_listBox.selection()  # Получаем выбранный элемент
    if selected_item:  # Если элемент выбран
        task_listBox.delete(selected_item)  # Удаляем его
