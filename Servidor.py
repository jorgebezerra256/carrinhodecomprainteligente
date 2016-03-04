#!/usr/bin/env python
# -*- coding: utf8 -*-


#https://www.passeidireto.com/arquivo/6120307/programa-cliente-echo-usando-tcp---python
#utilizar sockets para comunicação
import socket

#endereço local
host = ''
#porta de acesso
porta = 9856 

#socket(socket_family, socket_type), o construtor cria um novo socket. AF_INET - IPv4, SOCK_STREAM - TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#direciona o socket para o host e a porta
s.bind((host,porta))
#começa a escutar por conexões TCP, neste caso coloca apenas uma conexão na fila de espera.
s.listen(1)

print("Aguardando conexão com o cliente...")
#Aceita a conexão, cliente é um novo socket e end é o endereço do cliente

#str() converte os dados no parâmetro, em string
#print("Conectado ao cliente: " + str(end))

while True:    
    cliente, end = s.accept()
    print("Conectado ao cliente: " + str(end))
    #armazena os dados de entrada em dados(buffer). Neste caso, de tamanho 1024 bytes
    dados = cliente.recv(1024)
    #Se não existirem dados para capturar, sai do while.
    if not dados:
        break
        #decode() é utilizado para converter bytes em string
    print("Mensagem recebida: " + dados.decode())
    #envia os dados pelo socket cliente
    cliente.send(dados)
    print("Dados enviados!")
print("Cliente se desconectou!")
#fecha o socket cliente
cliente.close()