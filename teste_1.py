#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Funcoes import *
if __name__ == "__main__":
    print "Hello World"
    produto = []
    produto.append(1)
    produto.append(1)
    produto.append(1)
    produto.append(1)
    produto.append(0)
    produto.append(0)

    print produto
    produto = listIntToListString(produto)
    print produto
    
    #var = raw_input("Valor")
    #print var
    #marca = stringToListInt(var)
    
    #print marca
    numeros = [17, 123, 87, 34, 66, 8398, 44]
    print(numeros[2])
    print(numeros[9-8])
    print(numeros[-2])
    print(numeros[len(numeros)-1])
