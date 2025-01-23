#!/usr/bin/env python3

from socket import *

TCP_IP = 'localhost'
TCP_PORT = 5010
BUFFER_SIZE = 4096
chances = 3

# Criamos um socket para se comunicar
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((TCP_IP, TCP_PORT))

# Recebe o estado inicial da palavra secreta
#dica = clientSocket.recv(BUFFER_SIZE).decode()
dados = clientSocket.recv(BUFFER_SIZE).decode()
#print("dica:", eval(dica))

print("Palavra:", eval(dados))

while True:
    
    print(f"você tem {chances}")
    chute = input("Chute uma letra: ").lower()
    
    # Envia a letra chutada 
    clientSocket.send(str.encode(chute))

    # Recebe a palavra atualizada e o status de erro
    dados = clientSocket.recv(BUFFER_SIZE).decode()
    errou = clientSocket.recv(BUFFER_SIZE).decode()
    
    # Atualiza e exibe a palavra
    print("Palavra:", eval(dados))

    #acertou/errou letra
    if errou == "True":
        print(f"Letra {chute} incorreta!")
        chances -= 1
        
    if errou == "False":
        print(f"a letra {chute} está na palavra!!")

    # Verifica se o usuário acertou a palavra completa
    acertou = '_' not in eval(dados)
    if acertou:
        print("Ganhou!!!")
        break
    if chances == 0:
             print("perdeu")
             break
        
# Fecha a conexão
clientSocket.close()
