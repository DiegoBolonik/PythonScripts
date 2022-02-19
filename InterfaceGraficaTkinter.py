import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto

janela = Tk()
janela.title("Cotação atual das Moedas")
janela.geometry("400x400")

texto_orientação = Label(janela, text="Clique no botão para exibir a contação das modeas")
texto_orientação.grid(column=0, row=0, padx=30, pady=30)


botao = Button(janela, text="Buscar cotações Dólar/Euro/BTC", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text="text")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

# manter a janela visivel
janela.mainloop()
