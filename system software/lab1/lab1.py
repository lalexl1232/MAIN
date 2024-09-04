import os
import psutil
import matplotlib.pyplot as plt
import platform
import getpass

def get_system_info():
    # Получение информации о процессоре
    cpu_info = platform.processor()
    cpu_count = psutil.cpu_count(logical=False)
    cpu_architecture = platform.architecture()

    # Получение имени компьютера и пользователя
    hostname = platform.uname().node
    username = getpass.getuser()

    return cpu_info, cpu_count, cpu_architecture, hostname, username

def monitor_resources():
    cpu_percent = []
    memory_percent = []
    my_disk_usage_1 = []

    while True:
        cpu_percent.append(psutil.cpu_percent())
        memory_percent.append(psutil.virtual_memory().percent)
        my_disk_usage_1.append(psutil.disk_usage('/').percent)

        # Построение графиков
        plt.plot(cpu_percent, label='CPU')
        plt.plot(memory_percent, label='Memory')
        plt.plot(my_disk_usage_1, label='C:/')
        plt.xlabel('Time')
        plt.ylabel('Usage (%)')
        plt.title('Resource Monitor')
        plt.legend()
        plt.pause(0.5)  # Обновление графика каждую
        plt.clf()


cpu_info, cpu_count, cpu_architecture, hostname, username = get_system_info()
print(f"CPU Count: {cpu_count}")
print(f"CPU Info: {cpu_info}")
print(f"CPU Architecture: {cpu_architecture}")
print(f"Hostname: {hostname}")
print(f"Username: {username}")

monitor_resources()
