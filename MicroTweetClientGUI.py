#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webbrowser
import tweepy
from Tkinter import *

def mostrar(window): 
	 window.deiconify()

def ocultar(window):
	 window.withdraw()

def ejecutar(f): 
	 ventana.after(0,f)

def tweet(webpin):

	 pin = webpin
	 token = auth.get_access_token(verifier=pin)
	
	 if token:
	 	 ejecutar(mostrar(ventana1))
	 	 ventana.withdraw() 	 

if __name__ == "__main__":

	 ventana = Tk()
	 ventana1 = Toplevel(ventana)
	 ventana.title('My Easy Tweet')
	 ventana.config(bg='#81BEF7')
	 ventana1.title('My Easy Tweet')
	 ventana1.config(bg='#81BEF7')
	 
	 #ventana
	 consumer_key = ""
	 consumer_secret = ""	 
	 auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	 webbrowser.open(auth.get_authorization_url())
	 api = tweepy.API(auth)	
	 label= Label(ventana,text="Autorización + PIN",bg='#81BEF7')
	 label.grid(row=1, column= 2)
	 caja= Entry(ventana, textvariable = "escrive el PIN aqui")
	 caja.grid(row=2, column=2)
	 boton1 = Button(ventana, text="Aceptar", bg='white', command=lambda: tweet(caja.get()))
	 boton1.grid(row=3, column=2)

	 #ventana1
	 label1= Label(ventana1, text = "Escrive tu tweet",  bg= '#81BEF7' )
	 label1.grid(row=1, column= 2)
	 caja1 = Entry(ventana1, textvariable = "Ya puedes escribir tu tweet")
	 caja1.grid(row=2, column =2)
	 boton2 = Button(ventana1, text="Enviar", command = lambda: api.update_status(caja1.get()) and caja1.delete(0,END))
	 boton2.grid(row=3, column=2)
	 ventana1.withdraw()
	 ventana.mainloop()