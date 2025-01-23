#!/usr/bin/env python3

from socket import *

TCP_IP = 'localhost'
TCP_PORT = 5010
BUFFER_SIZE = 4096
#dica = input("digite uma dica simples:").lower()
palavra = input("Digite a palavra secreta: ").lower()
letras_secretas = ['_' for letra in palavra]
errou = False
# criamos um socket para se comunicar
# AF_INET = IPv4
# SOCK_STREAM = TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
# associamos o socket a uma dupla (endereço, porta)
serverSocket.bind((TCP_IP, TCP_PORT))

# precisamos habilitar o socket TCP a ser um servidor e ouvir novas conexões
serverSocket.listen()

# aqui o programa trava e fica esperando uma nova conexão para ser aceita
# o accept() retorna uma conexao por onde os pacotes serão enviados
conexao, endereco = serverSocket.accept()
print('Endereço e porta conectado:', endereco)

# vamos enviar os dados de volta, fazendo um eco
#serverSocket.send(str.encode(dica))
conexao.send(str(letras_secretas).encode())

while True:

    # recv retorna os dados em bytes
    # não precisamos do endereço, pois a conexão já está estabelecida
    # além disso, já temos o endereço no accept() acima
    dados = conexao.recv(BUFFER_SIZE)

    # um pacote vazio significa que a conexão foi encerrada
    if not dados:
        break

    print("Dados recebidos:", dados.decode())

    # Armazena as letras na variável chute e transforma elas em strings 
    chute = dados.decode()
    # Verifica se a letra chutada está no meio da palavra
    if(chute in palavra):
        index = 0
        
        # Procura a letra na palavra
        for letra in palavra:

            # ALtera a letra da palavra
            if (chute == letra):
                letras_secretas[index] = letra
            index += 1
            errou = False
            
    else:
        errou = True
        
    print(letras_secretas)
    
     

    # vamos enviar os dados de volta, fazendo um eco
    conexao.send(str(letras_secretas).encode())
    conexao.send(str(errou).encode())
    #conexao.send(str(dica).encode())
# fechar a conexão para liberar recursos do sistema
conexao.close()
