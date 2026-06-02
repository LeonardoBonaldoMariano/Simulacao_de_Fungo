#30/05 - Leo.Mariano
#Tradução do pseudocodigo para python;
#ajuste nos calculos das taxas;
#colocar consumo como porcentagem

#31/05 - Leo.Campos
#Implementação da biblioteca matplotlib
#correção na porcentagem da adaptação
#Exibição do resultado final e inicial
#Limitação de contagem de dias para o experimento 
#Resultado da simulaçao em um grafico de linhas
#Adição Tkinter para interface do programa
#adiçao de entradas na interface

#02/06 - Leo.Mariano
#Ajustes de formatação;
#Implementaçaõ de simulação em tempo real antes do gráfico;



#LIBRARYS
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


#SIMULAÇÃO/VARIÁVEIS INICIAIS
def simular():

    try:
    
        temperatura = float(entry_temperatura.get())
        umidade = float(entry_umidade.get())
        nutrientes = float(entry_nutrientes.get())
        dias_limite = int(entry_dias.get())

    except:
        messagebox.showerror(
            "Erro",
            "Preencha todos os campos corretamente."
        )
        return

    quantidade_de_individuos = 1
    hora = 0
    dia = 0


#ADAPTAÇÃO AO LONGO DO TEMPO
    adaptacao = 0.1
    adaptacao_em_porcentagem = adaptacao * 100

#ADAPTAÇÃO - HISTÓRICO PARA O GRÁFICO
    historico_dias = []
    historico_individuos = []

    while quantidade_de_individuos > 0:

        if dia < 2:
            adaptacao = 0.1
            adaptacao_em_porcentagem = adaptacao * 100
        else:
            if adaptacao_em_porcentagem < 100:
                if hora % 23 == 0:
                    adaptacao = (1 + (dia / 100))
                    adaptacao_em_porcentagem = adaptacao * 100
            else:
                adaptacao_em_porcentagem = 100

            
#PASSAGEM DO TEMPO
        if hora == 24:
            hora = 0
            dia += 1

#UMIDADE AO LONGO DO TEMPO
        if hora < 6 or hora > 18:
            variacao_de_umidade = (95 - umidade) * 0.3
            umidade += variacao_de_umidade            
        else:
            variacao_de_umidade = (umidade - 55) * 0.3
            umidade -= variacao_de_umidade

#TEMPERATURA AO LONGO DO TEMPO
        if hora < 6 or hora > 18:
            variacao_de_temperatura = (temperatura - 14) * 0.3
            temperatura -= variacao_de_temperatura
        else:
            variacao_de_temperatura = (26 - temperatura) * 0.3
            temperatura += variacao_de_temperatura
#NUTRIENTES AO LONGO DO TEMPO
        if nutrientes > quantidade_de_individuos:
            consumo_nutricional = quantidade_de_individuos
            nutrientes -= consumo_nutricional

#INDIVÍDUOS AO LONGO DO TEMPO
            taxa_de_crescimento = (temperatura * (consumo_nutricional / 1000) * (umidade / 55) * adaptacao)
            quantidade_de_individuos += taxa_de_crescimento
        else:
            taxa_de_crescimento = (-1 * temperatura * (consumo_nutricional / 10000) * (umidade / 55) * adaptacao)
            quantidade_de_individuos += taxa_de_crescimento
#SALVAR DADOS PARA O GRÁFICO
        if hora == 0:
            historico_dias.append(dia)
            historico_individuos.append(quantidade_de_individuos)

        hora += 1

#SIMULAÇÃO EM TEMPO REAL ANTES DO GRÁFICO
        resultado.config(
            text=(
                f"STATUS EM TEMPO REAL:\n"
                f"Dia: {dia} | Hora: {hora}h\n"
                f"População: {quantidade_de_individuos:.0f}\n"
                f"Temperatura: {temperatura:.1f}°C\n"
                f"Umidade: {umidade:.1f}%\n"
            )
        )
        janela.update()
        janela.after(5)  # Quanto menor o número, mais rápido corre a simulação

#LIMITE DE DIAS SIMULAÇÃO
        if dia >= dias_limite:
            break

#ESTADO FINAL
    resultado.config(
        text=(
            f"População Final: {quantidade_de_individuos:.0f}\n"
            f"Temperatura Final: {temperatura:.1f}°C\n"
            f"Umidade Final: {umidade:.1f}%\n"
            f"Adaptação: {adaptacao_em_porcentagem:.1f}%"
        )
    )
    plt.figure(figsize=(10, 5))
    plt.plot(
        historico_dias,
        historico_individuos,
        marker='o'
    )

#GRÁFICO
    plt.title("Crescimento Fungico ao Longo do Tempo")
    plt.xlabel("Dias")
    plt.ylabel("Quantidade de Indivíduos")
    plt.grid(True)
    plt.show()

#INTERFACE GRÁFICA
janela = tk.Tk()
janela.title("Simulador de Crescimento Fúngico")
janela.geometry("400x350")

tk.Label(janela, text="SIMULADOR DE CRESCIMENTO DE FUNGOS",
         font=("Arial", 11, "bold")).pack(pady=10)

tk.Label(
    janela,
    text="Temperatura Inicial"
).pack()

entry_temperatura = tk.Entry(janela)
entry_temperatura.insert(0, "10")
entry_temperatura.pack()

tk.Label(
    janela,
    text="Umidade Inicial"
).pack()

entry_umidade = tk.Entry(janela)
entry_umidade.insert(0, "55")
entry_umidade.pack()

tk.Label(
    janela,
    text="Nutrientes Iniciais"
).pack()

entry_nutrientes = tk.Entry(janela)
entry_nutrientes.insert(0, "9999999999999999")
entry_nutrientes.pack()

tk.Label(
    janela,
    text="Dias de Simulação"
).pack()

entry_dias = tk.Entry(janela)
entry_dias.insert(0, "30")
entry_dias.pack()

tk.Button(
    janela,
    text="Simular",
    command=simular
).pack(pady=10)

resultado = tk.Label(
    janela,
    text=""
)

resultado.pack()
janela.mainloop()