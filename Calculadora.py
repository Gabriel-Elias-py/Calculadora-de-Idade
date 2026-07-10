import tkinter as tk
from datetime import datetime

janela = tk.Tk()
janela.title("Calculadora de Idade")

adesivo = tk.Label(janela, text="Digite sua data de Nascimento")
adesivo.pack(pady=5)
data = tk.Entry(janela,)
data.pack()

adesivo2 = tk.Label(janela, text="Digite o horário do seu Nascimento")
adesivo2.pack(pady=5)
hora = tk.Entry(janela,)
hora.pack()

def calcular():
    data_de_nascimento = data.get()
    hora_de_nascimento = hora.get()
    data_completa = data_de_nascimento + " " + hora_de_nascimento
    print(data_completa)
    data_convertida = datetime.strptime(data_completa, "%d/%m/%Y %H:%M:%S")
    data_atual = datetime.now()
    timedelta = data_atual - data_convertida
    print(timedelta)

botao = tk.Button(janela, text="Calcular", command=calcular)
botao.pack()
data.get

janela.mainloop()