#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    print "Hello World"
    
    var = raw_input("Valor")
    print "ascii"
    print var
    asciiss= []
    for c in var:
        asciiss.append(ord(c))

    print asciiss
    asciiss = raw_input("inteiro")
    print "Caractere"
    char = []
    for i in asciiss:
        char.append(chr(i))
    print char
    print type(char)
