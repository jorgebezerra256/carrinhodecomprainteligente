#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Funcoes import *
if __name__ == "__main__":
    print "Hello World"
    
    var = raw_input("Valor")
    print type(var[0])
    print var
    asciiss= stringToListInt(var)
    
    print type(asciiss[0])
    print asciiss
    print len(var)
    