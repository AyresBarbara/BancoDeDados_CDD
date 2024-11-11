import requests
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "turmab"
)
meucursor2 = banco.cursor()
cep = input("Qual é o cep?")

if len(cep) == 8 :
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(link)
    print(requisicao)
    dic_requisicao = requisicao.json()

    logradouro = dic_requisicao['logradouro']
    cep = dic_requisicao['cep']
    complemento = dic_requisicao['complemento']
    print(dic_requisicao)

    sql = "INSERT INTO endereco (logradouro, cep, complemento) VALUES (%s, %s, %s)"
    data = (logradouro, cep, complemento)
    meucursor2.execute(sql, data)
    banco.commit()
    meucursor2.close()
    banco.close()
else:
    print("CEP inválido!")