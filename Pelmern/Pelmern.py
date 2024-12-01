import tkinter as tk
from tkinter import simpledialog, messagebox
import math

# Создаем главное окно
root = tk.Tk()
root.withdraw()  # Скрыть главное окно

# Функция для ввода параметров
def get_parameters():
    params = {}

    params['daily_output'] = simpledialog.askfloat(
        "Parametr 1",
        "Sutochnaya virabotka gotovoy produkcii:"
    )
    params['shift_duration'] = simpledialog.askfloat(
        "Parametr 2",
        "Prodolzitelnost rabochey smeni:"
    )
    params['machine_productivity'] = simpledialog.askfloat(
        "Parametr 3",
        "Proizvoditelnost pelmennogo apparata:"
    )
    params['dough_percentage'] = simpledialog.askfloat(
        "Parametr 4",
        "Massovaya dolya testa(%):"
    )
    params['mixer_productivity'] = simpledialog.askfloat(
        "Parametr 5",
        "Proizvoditelnost testomesilnoy machini:"
    )
    params['kuttler_productivity'] = simpledialog.askfloat(
        "Parametr 6",
        "Proizvoditelnost kuttlera:"
    )
    return params

# Вызываем функцию для ввода
parameters = get_parameters()

#присваиваем значения
DO = parameters['daily_output']
SD = parameters['shift_duration']
MP = parameters['machine_productivity']
DP = parameters['dough_percentage']
MxP = parameters['mixer_productivity']
KP = parameters['kuttler_productivity']

# расчет значений
#Производительность технологической линии
PTP = DO/(SD*2)

#количество пельменных машин
NPM = math.ceil(max(1, PTP/MP))

# Производительность технологической линии подготовки теста
PTD = (DP*PTP)/100

#количество тестомесильных машин
NDM = math.ceil(max(1, PTD/MxP))

#Производительность технологической линии подготовки фарша
PPM = ((100 - DP)*PTP)/ 100

#количество куттеров
NKM = math.ceil(max(1, PPM/KP))


# Вывод введенных значений
print("Parametrs:")
print(f"Sutochnaya virabotka gotovoy produkcii: {parameters['daily_output']} t")
print(f"Prodolzitelnost rabochey smeni: {parameters['shift_duration']} h")
print(f"Proizvoditelnost pelmennogo apparata: {parameters['machine_productivity']} t/h")
print(f"Massovaya dolya testa(%): {parameters['dough_percentage']} %")
print(f"Proizvoditelnost testomesilnoy machini: {parameters['mixer_productivity']} t/h")
print(f"Proizvoditelnost kuttlera: {parameters['kuttler_productivity']} t/h")
print(f"Neobhodimoe kolichestvo pelmennyh apparatov: {NPM} sh")
print(f"Neobhodimoe kolichestvo testomesilnyyh machin: {NDM} sh")
print(f"Neobhodimoe kolichestvo kuttlerov: {NKM} sh")


# Функция для вывода результатов
def show_results():
    message = (
        f"Neobhodimoe kolichestvo pelmennyh apparatov: {NPM} sh\n"
        f"Neobhodimoe kolichestvo testomesilnyyh machin: {NDM} sh\n"
        f"Neobhodimoe kolichestvo kuttlerov: {NKM}sh"
    )
    messagebox.showinfo("Result", message)

# Выводим результаты в отдельном окне
show_results()
