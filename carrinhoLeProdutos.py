#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
from Funcoes import *

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    setor = 26
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Bem vindo ao supermercado XYZ!"
print "Precione Ctrl-C para finalizar a aplicação."

setor = 20
#cartao = []
# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading and setor != 26:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Produto detectado!"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        #print "UID da TAG rfid: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)
        

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, setor, key, uid)

        # Check if authenticated
        
        if status == MIFAREReader.MI_OK:
            cartao = MIFAREReader.MFRC522_Read(setor)            
            print "\nMarca do produto:"                   
            
            produto = listIntToListString(cartao)
            print produto
            
            MIFAREReader.MFRC522_StopCrypto1()

            print setor
            setor = setor + 1
            
        else:
            print setor
            setor = setor + 1            
            print "Erro de Autenticação!"

        if setor == 26:
            setor = 20
            continue
