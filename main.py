import json 

import pycountry

from tkinter import *

from phone_iso3166.country import phone_country

import phonenumbers

from phonenumbers import geocoder, carrier, timezone

#MasterLipakumu
# après avoir proceder au importations dont nous aurons besoin attaquons nous a l'initialisation de l'application en 1er lieu 


class Location_Tracker:
    #initialisation de l'écran
    def __init__(self, App):
        self.window = App
        #titre de l'application
        self.window.title("Master Lipakumu Phone number Tracker")
        #taille de l'écran
        self.window.geometry("500x500")
        #couleur de fond ou background
        self.window.configure(bg="#0040ff")
        #interdiction de pouvoir redimentionner avec la souris
        self.window.resizable(False, False)

       #menu de notre application phrase d'affiche de notre app
        Label(App, text="Enter a phone number",fg="white", font=("Times", 20), bg="#3f5efb").place(x=150,y= 30)
        #champ d'etre de notre app
        self.phone_number = Entry(App, width=16, font=("Arial", 15), relief="flat")
        #boutton 1 de nottre app 
        self.track_button = Button(App, text="Track Country", bg="#22c1c3", relief="sunken")
        #boutton 2 de notre app
        self.plus = Button(App, text="plus d'infos", bg="#22c1c3", relief="sunken")
        #création des phrases a afficher sur notre app
        self.country_label = Label(App,fg="white", font=("Times", 20), bg="#3f5efb")
        self.geocoder_label = Label(App,fg="white", font=("Times", 20), bg="#3f5efb")
        self.carrier_label = Label(App,fg="white", font=("Times", 20), bg="#3f5efb")
        self.timezone_label = Label(App,fg="white", font=("Times", 20), bg="#3f5efb")

        #positionnement de tout nos éléments précedemment crée 
        self.phone_number.place(x=170, y=120)
        self.track_button.place(x=200, y=200)
        self.plus.place(x=100, y=200)
        self.country_label.place(x=100, y=280)
        self.geocoder_label.place(x=100, y=310)
        self.carrier_label.place(x=100, y=360)
        self.timezone_label.place(x=100, y=395)

        #lier nos boutton a une fonction bien précis
        self.track_button.bind("<Button-1>", self.Track_location)
        self.plus.bind("<Button-1>", self.Tracker_plus)

    #1er fonction d'excution evenementiel
    def Track_location(self,event):
        #récuperation du numero inscrit dans le champs précedament crée 
        phone_number = self.phone_number.get()
        #initialiser une variable d'affichage
        country = "Country is Unknown"
        #si il y a un numero dans la variable phone_number
        if phone_number:
            #la variable tracked aura les donnée de contry suivant 
            tracked = pycountry.countries.get(alpha_2=phone_country(phone_number))
            #affiche tracked
            print(tracked)
            #si tracked il y a la variable tracked
            if tracked:
                #la variable contry precedemment crée dois contenir cette liste de donnée
                country = [tracked.official_name, tracked.numeric, tracked.name]
            #affiche contry dans les phrases initale
        self.country_label.configure(text=country)

        #2nd fonction d'excution evenemmentiel
    def Tracker_plus(self, event):
        
        phone_number = self.phone_number.get()

        #geocoder utilisation
        ch_number = phonenumbers.parse(phone_number, "CH")
        #affichage du pays
        geocoder.description_for_number(ch_number, "en")

        #carrier utilisation
        ro_number = phonenumbers.parse(phone_number, "RO")
        #affichage du réseau de ce numero
        carrier.name_for_number(ro_number, "en")

        #timezone utilisation 
        gb_number = phonenumbers.parse(phone_number, "GB")
        #affichage du continent et ville
        timezone.time_zones_for_number(gb_number)

        #affichage des données dans les phrases precedemment crée
        self.geocoder_label.configure(text=geocoder.description_for_number(ch_number, "en"))

        self.carrier_label.configure(text=carrier.name_for_number(ro_number, "en"))

        self.timezone_label.configure(text=timezone.time_zones_for_number(gb_number))



#lancement de l'app
PhoneTracker = Tk()

MyApp = Location_Tracker(PhoneTracker)

PhoneTracker.mainloop()
# MASTER LIPAKUMU

