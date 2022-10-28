#!/usr/bin/env python3
import socket
import sys
class udpclient():
    def __init__(self): # constructeur de la classe avec l'affectation des variables au client
        self.port=int(sys.argv[2]) # on renseigne le port en deuxième argument
        self.buff = 1024
        self.ip=sys.argv[3]; # on renseigne l'ip en troisème argument. On diffuse en broadcast afin de contacter tous les serveurs qui écoute au même port.
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # création du socket UDP





    def envoyerMessage(self): # methode permettant l'envoie du message au serveur
        self.socket.sendto(bytes(sys.argv[1] ,'utf8'), (self.ip, self.port)) #Envoie du message au serveur, on renseigne le message en premier argument 



    def recevoirMessage(self):# methode permettant de recevoir un message si l'envoie du message au serveur a fonctionné
        rep=True
        while rep == True: # boucle permettant la demande de reception de réponse afin de voir s'il reste encore des serveurs qui ont répondu ou souhaitent répondre

            try:

                self.socket.settimeout(5) # attente de 5 seconde 
                data =self.socket.recv(self.buff)
                print('"ok:', data.decode("utf-8")+'"')
            except socket.timeout: # s'il n'y a pas de réponse la communication s'achève 
                print("Plus de réponse")
                rep = False;


clientTest=udpclient();   # on crée un client qui va effectuer l'envois et la récéption des messages.
clientTest.envoyerMessage()
clientTest.recevoirMessage()
