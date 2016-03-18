#!/usr/bin/env python
# -*- coding: utf8 -*-

#converte uma lista de string para lista de inteiro
def stringToListInt(string):
    listInt = []
    for c in string:
        listInt.append(ord(c))
    return listInt

#converte uma lista de inteiros para uma string
def listIntToListString(numero):
    listChar = []        
    for i in numero:        
        if i == 0:            
            break            
        listChar.append(chr(i))
        
    return ''.join(listChar)

#recebe uma string converte para numeros e monta uma lista de 16 bytes para retorno
def trataStringParaGravar(string):            
    stringGravar = stringToListInt(string)            
    tam = len(string)
    if tam < 16:
        for x in range(tam,16):
            stringGravar.append(0)
    else:
        stringGravar[0:16]
    return stringGravar
