# --------------------------------lab2
import subprocess
import signal
import os
import psutil
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class ProcessManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Process Manager")
        self.geometry("800x600")

        # Создание главного фрейма
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Создание виджетов для отображения информации о процессах
        self.process_tree = ttk.Treeview(self.main_frame)
        self.process_tree["columns"] = ("ID", "Memory", "Threads")
        self.process_tree.heading("#0", text="Process")
        self.process_tree.heading("ID", text="ID")
        self.process_tree.heading("Memory", text="Memory")
        self.process_tree.heading("Threads", text="Threads")
        self.process_tree.pack(fill=tk.BOTH, expand=True)

        # Кнопки управления процессами
        self.create_process_button = ttk.Button(self.main_frame, text="Create Process", command=self.create_process)
        self.terminate_process_button = ttk.Button(self.main_frame, text="Terminate Process",
                                                   command=self.terminate_process)
        self.suspend_resume_thread_button = ttk.Button(self.main_frame, text="Suspend/Resume Thread",
                                                       command=self.suspend_resume_thread)
        self.change_priority_button = ttk.Button(self.main_frame, text="Change Priority", command=self.change_priority)

        self.create_process_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.terminate_process_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.suspend_resume_thread_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.change_priority_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Обновление списка процессов
        self.update_process_list()

    def update_process_list(self):
        # Очищаем список процессов
        for item in self.process_tree.get_children():
            self.process_tree.delete(item)

        # Получаем список процессов
        processes = psutil.process_iter(['pid', 'name', 'memory_info', 'num_threads'])
        for process in processes:
            memory_info = process.info.get('memory_info')
            if memory_info:
                memory = memory_info.rss
            else:
                memory = "N/A"

            if process and hasattr(process, 'info'):
                pid = process.info.get('pid', 'N/A')
            else:
                pid = 'N/A'

            if process and hasattr(process, 'info') and 'num_threads' in process.info:
                num_threads = process.info['num_threads']
            else:
                num_threads = 'N/A'

            self.process_tree.insert("", "end", text=process.info['name'],
                                     values=(pid, memory, num_threads))
        # Планируем следующее обновление списка через 1 секунду
        self.after(5000, self.update_process_list)

    def create_process(self):
        # Открытие текстового редактора на macOS
        subprocess.Popen(["open", "-a", "TextEdit"])

    def terminate_process(self):
        selected_item = self.process_tree.selection()
        if selected_item:
            pid = int(self.process_tree.item(selected_item, "values")[0])
            os.kill(pid, 9)
        else:
            messagebox.showinfo("Error", "Select a process to terminate.")

    def suspend_resume_thread(self):
        selected_item = self.process_tree.selection()
        if selected_item:
            pid = int(self.process_tree.item(selected_item, "values")[0])
            process = psutil.Process(pid)

            # Получение ID первого потока процесса
            thread_id = process.threads()[0].id

            # Проверка, приостановлен ли поток
            if process.threads()[0].is_running():
                # Если поток запущен, приостанавливаем его
                os.kill(thread_id, signal.SIGSTOP)
                messagebox.showinfo("Success", "Thread suspended.")
            else:
                # Если поток приостановлен, возобновляем его
                os.kill(thread_id, signal.SIGCONT)
                messagebox.showinfo("Success", "Thread resumed.")
        else:
            messagebox.showinfo("Error", "Select a process first.")
    def change_priority(self):
        selected_item = self.process_tree.selection()
        if selected_item:
            pid = int(self.process_tree.item(selected_item, "values")[0])

            # Установка нового приоритета (10 - это нормальный приоритет)
            os.setpriority(os.PRIO_PROCESS, pid, 20)

            messagebox.showinfo("Success", "Priority changed.")
        else:
            messagebox.showinfo("Error", "Select a process first.")


if __name__ == "__main__":
    app = ProcessManagerApp()
    app.mainloop()
