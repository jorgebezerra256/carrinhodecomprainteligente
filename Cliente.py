#!/usr/bin/env python
# -*- coding: utf8 -*-

#http://wiki.python.org.br/SocketBasico
#https://www.passeidireto.com/arquivo/6120307/programa-cliente-echo-usando-tcp---python
"""
Cliente ECHO utilizando TCP

Para criar um cliente, é necessário:
    criar um socket
    conectar ao servidor
    enviar e receber dados

Rodrigo Borges de Oliveira
Eliezer Marques da Silva Neto
"""

#utilizar sockets para comunicação
import socket

#endereço local 192.168.11.51
host = '192.168.11.51'
#porta de acesso
porta = 9856

#socket(socket_family, socket_type), o construtor cria um novo socket.  AF_INET - IPv4, SOCK_STREAM - TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#conecta o socket ao endereço e porta

s.connect((host,porta))
#utiliza input() para entrada de dados do teclado
msg = raw_input("Digite a mensagem: ")

#enquanto o usuário não digitar "f"
while msg != "f":
    #envia a mensagem em bytes, utilizando o socket. Encode() é utilizado para converter de string para bytes
    s.send(msg.encode())
    #recebe os dados pelo socket e armazena em dados(buffer). Neste caso, de tamanho 1024 bytes
    dados = s.recv(1024)
    #decode() é utilizado para converter bytes em string
    print("Dados recebidos: " + dados.decode())
    #utiliza input() para entrada de dados do teclado
    msg = raw_input("Digite a mensagem: ")
print("Conexão encerrada!")
#fecha o socket s
s.close() 