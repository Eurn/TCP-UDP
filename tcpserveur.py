#!/usr/bin/env python3
import socket
import sys
class tcpserveur():

    def __init__(self):# constructeur de la classe avec l'affectation des variables au serveur 
        self.ip = ""# l'ip s'affecte automatiquement 
        self.port = int(sys.argv[1])# on renseigne le port en premier argument
        self.buff = 20
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# création du socket TCP
        self.socket.bind((self.ip,self.port))# on lie l'ip et le port au socket
        self.socket.listen(1)# le serveur accepte la connection et écoute ce que le client a à lui dire 


    def repondre(self):# methode permettant au serveur d'envoyer un reponse au client
        while 1 :# boucle permettant au serveur de ne pas s'arreter
            connect, addr = self.socket.accept() # on accepte le socket envoyé
            print("client d'adresse " + addr[0] + " depuis port " + str(addr[1]))# affichage demandé
            data = connect.recv(self.buff)
            if not data: break 
            print('ok:', data.decode("utf-8")+'') # affichage demandé 
            connect.send(data) # on envoie la reponse au client
        connect.close()# on ferme la connection  


serverTest=tcpserveur();# on creer le serveur qui va effectuer la réponse

serverTest.repondre();