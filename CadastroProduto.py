#!/usr/bin/env python2
#encoding: UTF-8

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
from Funcoes import *

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C finaliza o sistema de leitura."
    continue_reading = False
    GPIO.cleanup()

#intervalo para gravação
inicio = 20
fim = 23
for setor in range(inicio, fim):
    continue_reading  = True
    print setor
    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()

    """
    Setores usados para gracação: 20 -> nome
    21 -> marca
    """
    print "Cadastro de produto"
    #setor de gravação no]a tag rfid

    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    #
    while continue_reading:        
            
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
            print "UID do cartão: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
            
            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
                
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)
            #setor = 20
            # Authenticate        
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, setor, key, uid)
            print "\n"
                    
            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                
                # Variable for the data to write
                if(setor == 20):        
                    var = raw_input("Digite a marca do produto!")
                if(setor == 21):        
                    var = raw_input("Digite o nome do produto!")
                if(setor == 22):        
                    var = raw_input("Digite o lote do produto")
                    inicio = 24
                    fim = 25
                if(setor == 24):        
                    var = raw_input("Digite a validade do produto")
                if(setor == 25):        
                    var = raw_input("Digite o valor do produto (R$ 00.00)!")
                produto = trataStringParaGravar(var)
                print produto
                                    
                # Write the data
                MIFAREReader.MFRC522_Write(setor, produto)
                print "\n"
                #time.sleep(1);

                print "It now looks like this:"
                # Check to see if it was written
                MIFAREReader.MFRC522_Read(setor)
                print "\n"
                                                
                # Stop
                MIFAREReader.MFRC522_StopCrypto1()

                # Make sure to stop reading for cards
                continue_reading = False
            else:
                print "Erro de Autenticação"
