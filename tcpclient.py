#!/usr/bin/env python3
import socket
import sys
class tcpclient():

    def __init__(self):# constructeur de la classe avec l'affectation des variables au client

            self.port = int(sys.argv[2])# on renseigne le port en premier argument
            self.ip = sys.argv[3]# on renseigne l'ip en troisème argument. On diffuse en broadcast afin de contacter tous les serveurs qui écoute au même port.
            self.buff = 1024
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# création du socket TCP
            


    def envoyerMessage(self):# methode permettant l'envoie du message au serveur
        self.socket.connect((self.ip,self.port)) #demande de connection au serveur 
        self.socket.send(bytes(sys.argv[1] ,'utf8'))#Envoie du message au serveur, on renseigne le message en premier argument


    def recevoirMessage(self):# methode permettant de recevoir un message si l'envoie du message au serveur a fonctionné
        rep=True
        while rep == True:# boucle permettant la demande de reception de réponse afin de voir s'il reste encore des serveurs qui ont répondu ou souhaitent répondre
            try:      
                self.socket.settimeout(5)# attente de 5 seconde
                data, addr =self.socket.recvfrom(self.buff)
                print('"ok:', data.decode("utf-8")+'"')
            except socket.timeout:# s'il n'y a pas de réponse la communication s'achève
                print("Plus de réponse")
                rep = False;
                self.socket.close()# on ferme la connection


clientTest = tcpclient() # on crée un client qui va effectuer l'envois et la récéption des messages.
clientTest.envoyerMessage()
clientTest.recevoirMessage()