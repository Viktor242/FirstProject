import tkinter as tk

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

def mark_task_1(task_listBox):
   
    selected_item = task_listBox.selection()  # Получаем выбранный элемент
    if selected_item:
        # Обновляем статус задачи (первое значение остается прежним, второе меняется)
        task_listBox.item(selected_item, values=(task_listBox.item(selected_item)['values'][0], "В процессе"))
        # Настраиваем тег для желтого фона
        task_listBox.tag_configure("inprogress", background="yellow")
        # Применяем тег к выбранному элементу
        task_listBox.item(selected_item, tags=("inprogress",))

def mark_task_2(task_listBox):
    
    selected_item = task_listBox.selection()
    if selected_item:
        # Обновляем статус задачи на "Выполнено"
        task_listBox.item(selected_item, values=(task_listBox.item(selected_item)['values'][0], "Выполнено"))
        # Настраиваем тег для светло-зеленого фона
        task_listBox.tag_configure("completed", background="lightgreen")
        # Применяем тег к выбранному элементу
        task_listBox.item(selected_item, tags=("completed",))

def mark_task_3(task_listBox):
   
    selected_item = task_listBox.selection()
    if selected_item:
        # Обновляем статус задачи на "Просрочено"
        task_listBox.item(selected_item, values=(task_listBox.item(selected_item)['values'][0], "Просрочено"))
        # Настраиваем тег для красного фона
        task_listBox.tag_configure("completed", background="red")
        # Применяем тег к выбранному элементу
        task_listBox.item(selected_item, tags=("completed",))