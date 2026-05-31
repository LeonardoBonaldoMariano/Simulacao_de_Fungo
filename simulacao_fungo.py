#30/05 - Leo
#Tradução do pseudocodigo para python;
#ajuste nos calculos das taxas;
#colocar consumo como porcetagem

#LIBRARYS
import time
import os

#VARIÁVEIS INICIAIS
quantidade_de_individuos = 1
temperatura = 10
nutrientes = 9999999999999999
umidade = 55
hora = 0
dia = 0
adaptacao = 0.1

umidade = 55
#ADAPTAÇÃO AO LONGO DO TEMPO
while quantidade_de_individuos > 0 :  
    os.system('cls')
    if dia < 2 :
        adaptacao = 0.1
    else :
        if adaptacao_em_porcentagem < 100 :
            if hora % 23 ==  0 :
                adaptacao = (1 + (dia / 100))
                adaptacao_em_porcentagem = adaptacao * 100
        else :
            adaptacao_em_porcentagem = 100

#PASSAGEM DO TEMPO
    if hora == 24 :
        hora = (hora * 0) 
        dia = (dia + 1)

#UMIDADE AO LONGO DO TEMPO
    if hora < 6 or hora > 18 :
            variacao_de_umidade = (umidade - 55) * 0.3 
            umidade = (umidade - variacao_de_umidade)
    else :
            variacao_de_umidade = (95 - umidade) * 0.3
            umidade = (umidade + variacao_de_umidade)

#TEMPERATURA AO LONGO DO TEMPO
    if hora < 6 or hora > 18 :
            variacao_de_temperatura = (temperatura - 14) * 0.3
            temperatura = (temperatura - variacao_de_temperatura)
    else :
            variacao_de_temperatura = (26 - temperatura) * 0.3
            temperatura = (temperatura + variacao_de_temperatura)

#NUTRIENTES AO LONGO DO TEMPO
    if nutrientes > quantidade_de_individuos :
        consumo_nutricional = (quantidade_de_individuos)
        nutrientes = (nutrientes - consumo_nutricional)
        consumo_nutricional_em_porcentagem = (consumo_nutricional / nutrientes) * 100
        nutrientes_em_porcentagem = (nutrientes / 9999999999999999) * 100
    else :
        nutrientes = 0
        consumo_nutricional_em_porcentagem = 0
        nutrientes_em_porcentagem = 0


#INDIVIDUOS AO LONGO DO TEMPO
    if nutrientes > 0 :
        taxa_de_crescimento = (((temperatura) * (consumo_nutricional / 1000) * (umidade /55) * (adaptacao)))
        quantidade_de_individuos = (quantidade_de_individuos + taxa_de_crescimento)
    else :
        taxa_de_crescimento = (-1 * ((temperatura) * (consumo_nutricional / 10000) * (umidade /55) * (adaptacao)))
        quantidade_de_individuos = (quantidade_de_individuos + taxa_de_crescimento)
    
    if quantidade_de_individuos < (-1 * taxa_de_crescimento) :
        quantidade_de_individuos = 0

    print(f"QUANTIDADE DE INDIVÍDUOS: {quantidade_de_individuos:.0f}")
    print(f"TEMPERATURA: {temperatura:.0f}°C")
    print(f"NUTRIENTES DISPONÍVEIS: {nutrientes_em_porcentagem:.1f}%")
    print(f"CONSUMO NUTRICIONAL: {consumo_nutricional_em_porcentagem:.1f}%")
    print(f"UMIDADE: {umidade:.1f}%")
    print(f"ADAPTAÇÃO: {adaptacao_em_porcentagem:.1f}%")
    print(f"Dia {dia} ; Hora {hora}")
#espera 1 segundo
    time.sleep(0.05)
    hora = (hora + 1)