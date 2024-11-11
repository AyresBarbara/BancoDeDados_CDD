import mysql.connector
cont =0
banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "turmab"
)

meucursor = banco.cursor()

while cont !=2 :
    opcao = int(input("Digite uma opção do menu: \n 1 - Pesquisar \n 2 - Inserir \n 3 - sair"))

    if opcao == 1:
        pesquisa = 'select * from alunos;'
        meucursor.execute(pesquisa)

        resultado = meucursor.fetchall()
        for x in resultado:
            print(x)


    if opcao == 2:
        nome1 = input("Digite seu nome: ")
        telefone1 = input("Digite seu telefone: ")

        sql = "INSERT INTO alunos(nome, telefone) values (%s,%s)"
        data = (nome1, telefone1)
        meucursor.execute(sql, data)
        banco.commit()

    if opcao == 3:
        meucursor.close()
        banco.close()
        print("Fim de Operação")
        break

    cont = int(input("Você deseja continuar? \n 1 - Continuar \n 2 - sair \n"))

