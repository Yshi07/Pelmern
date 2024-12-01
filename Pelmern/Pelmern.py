import tkinter as tk
from tkinter import simpledialog, messagebox
import math

# ������� ������� ����
root = tk.Tk()
root.withdraw()  # ������ ������� ����

# ������� ��� ����� ����������
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

# �������� ������� ��� �����
parameters = get_parameters()

#����������� ��������
DO = parameters['daily_output']
SD = parameters['shift_duration']
MP = parameters['machine_productivity']
DP = parameters['dough_percentage']
MxP = parameters['mixer_productivity']
KP = parameters['kuttler_productivity']

# ������ ��������
#������������������ ��������������� �����
PTP = DO/(SD*2)

#���������� ���������� �����
NPM = math.ceil(max(1, PTP/MP))

# ������������������ ��������������� ����� ���������� �����
PTD = (DP*PTP)/100

#���������� �������������� �����
NDM = math.ceil(max(1, PTD/MxP))

#������������������ ��������������� ����� ���������� �����
PPM = ((100 - DP)*PTP)/ 100

#���������� ��������
NKM = math.ceil(max(1, PPM/KP))


# ����� ��������� ��������
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


# ������� ��� ������ �����������
def show_results():
    message = (
        f"Neobhodimoe kolichestvo pelmennyh apparatov: {NPM} sh\n"
        f"Neobhodimoe kolichestvo testomesilnyyh machin: {NDM} sh\n"
        f"Neobhodimoe kolichestvo kuttlerov: {NKM}sh"
    )
    messagebox.showinfo("Result", message)

# ������� ���������� � ��������� ����
show_results()
