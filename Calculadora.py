import tkinter as tk
from datetime import datetime
#from dateutil.relativedelta import relativedelta as rd

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
    data_convertida = datetime.strptime(data_completa, "%d/%m/%Y %H:%M:%S")
    data_atual = datetime.now()
    
    tempo_de_vida = data_atual - data_convertida
    dias = tempo_de_vida.days
    segundos = tempo_de_vida.seconds

    tempo_vivido.config(text=f"Você viveu aproximadamente:\n{tempo_de_vida}")

    #idade = data_atual.year - data_convertida.year
    #idede = 
    if data_atual.month < data_convertida.month or data_atual.month == data_convertida.month and data_atual.day < data_convertida.day: idade = idade -1
    resultado.config(text=f"Você tem {idade} anos de Idade!!")


botao = tk.Button(janela, text="Calcular", command=calcular)
botao.pack()
data.get

adesivo3 = tk.Label(janela, text="Essa é a sua Idade:")
adesivo3.pack(pady=10)

resultado = tk.Label(janela, text="")
resultado.pack(pady=5)

tempo_vivido = tk.Label(janela, text="")
tempo_vivido.pack(pady=10)

janela.mainloop()