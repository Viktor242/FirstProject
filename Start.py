import tkinter as tk
from tkinter import ttk, messagebox
from services import TaskManager

class TaskApp:
    STATUS_OPTIONS = ["Не начата", "В процессе", "Выполнено", "Просрочено"]

    def __init__(self, root):
        self.root = root
        self.root.title("Управление задачами")
        self.root.geometry("500x600")
        self.manager = TaskManager()
        self.create_widgets()
        self.refresh_tasks()

    def create_widgets(self):
        tk.Label(self.root, text="Пропиши задачу", font=("Arial", 14)).pack(pady=20)
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=10, ipadx=100)
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Добавить задачу", command=self.add_task).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Удалить задачу", command=self.delete_task).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Изменить статус", command=self.change_status).pack(side=tk.LEFT, padx=5)
        self.status_var = tk.StringVar()
        self.status_combobox = ttk.Combobox(self.root, textvariable=self.status_var, values=self.STATUS_OPTIONS, state="readonly")
        self.status_combobox.pack(pady=5)
        self.status_combobox.set("Выбрать статус")
        self.tree = ttk.Treeview(self.root, columns=("Task", "Status"), show="headings")
        self.tree.heading("Task", text="Текущие задачи")
        self.tree.heading("Status", text="Статус")
        self.tree.column("Task", width=250)
        self.tree.column("Status", width=120)
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)
        style = ttk.Style()
        style.configure("Treeview.Heading", foreground="blue")

    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            messagebox.showwarning("Ошибка", "Задача не может быть пустой!")
            return
        self.manager.add_task(text)
        self.entry.delete(0, tk.END)
        self.refresh_tasks()

    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Ошибка", "Выберите задачу для удаления!")
            return
        if messagebox.askyesno("Подтверждение", "Удалить выбранную задачу?"):
            index = self.tree.index(selected[0])
            self.manager.delete_task(index)
            self.refresh_tasks()

    def change_status(self):
        selected = self.tree.selection()
        new_status = self.status_var.get()
        if not selected:
            messagebox.showwarning("Ошибка", "Выберите задачу для изменения статуса!")
            return
        if new_status not in self.STATUS_OPTIONS:
            messagebox.showwarning("Ошибка", "Выберите корректный статус!")
            return
        index = self.tree.index(selected[0])
        self.manager.change_status(index, new_status)
        self.refresh_tasks()

    def refresh_tasks(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for task in self.manager.get_tasks():
            self.tree.insert("", "end", values=(task.text, task.status))

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()