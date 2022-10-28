#!/usr/bin/env python3
import socket
import sys
class udpserveur():

    def __init__(self):# constructeur de la classe avec l'affectation des variables au serveur 
        self.port=int(sys.argv[1]) # on renseigne le port en premier argument
        self.ip="" # l'ip s'affecte automatiquement 
        self.buff = 1024
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # création du socket UDP
        self.socket.bind((self.ip, self.port)) # on lie l'ip et le port au socket 

    def repondre(self): # methode permettant au serveur d'envoyer un reponse au client
        while True: # boucle permettant au serveur de ne pas s'arreter
            data, addr = self.socket.recvfrom(self.buff) 
            print("client d'adresse " + addr[0] + " depuis port " + str(addr[1])) # affichage demandé 
            print ('ok:', data.decode("utf-8")+'')# affichage demandé
            self.socket.sendto(bytes(""+data.decode("utf-8"),'utf-8'),addr)# envoie du message de retour au client




serverTest=udpserveur(); # on creer le serveur qui va effectuer la réponse

serverTest.repondre();