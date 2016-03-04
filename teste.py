#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Funcoes import *
if __name__ == "__main__":
    print "Hello World"
    
    var = raw_input("Valor")
    print "ascii"
    print var
    asciiss= []
    for c in var:
        asciiss.append(ord(c))

    print asciiss
    #asciiss = raw_input("inteiro")
    #print "Caractere"
    #char = []
    #for i in asciiss:
    #    char.append(chr(i))
    #print char
    #print type(char)

    data = []
    data1 = []
    data1.append(106)
    data1.append(111)
    data1.append(114)
    data1.append(103)
    data1.append(101)
    
    for x in range(0,16):
        data.append(0x00)
    
    print data
    print type(data1)
    print data1
    dat = ListintToListString(data1)
    print dat
    #lista de caracteres para string
    tr = ''.join(dat)
    print tr
    
    dat = []
    marca = stringToListInt("Marca:")
    
    print marca