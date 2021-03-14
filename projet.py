from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from abc import ABC, abstractmethod
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from PIL import ImageTk, Image


#il faut avoir une liste des évènements pour enregistrer les events
#il faut utiliser les methodes static methods parce que nous savons pas le nombre des évènements
#tout ce qui est optionnel il faut le mettre en booléen



class Evenement:
    def __init__(self,nom,date,etype,debut,fin,salle,status,id):
        self.nom = nom
        self.date = date
        self.etype = etype
        self.debut = debut
        self.fin = fin
        self.salle = salle
        self.status = status
        self.id = id

class Utilisateur:

    def __init__(self):
        self.name = input("Enter your name: ")
        self.password = input("Enter your password: ")
"""
    def login(self):
        admin = False
        success = False
        file = open("users_details.txt","r")
        for i in file:
            a, b, c = i.split(",")
            c = c.strip()
            if(a == self.name) and (b == self.password):
                success = True
                if(c == '1'):
                    admin = True
        file.close()
        if success:
            print("Login Successful!!")
        else:
            print("Wrong username or password")
    

    def geteventlist(self):
        if success:
            return eventlist

    def consulter(self):
        pass
"""




class UtilisateurAdmin(Utilisateur):

    def __init__(self):
        super().__init__()

    def ajouter(self,event_name,eventD,eventM):
        if admin == True:
            eventlist.append([event_name,eventD,eventM])
        else:
            print("You don't have access to our event site")


    def supprimer(self,event_name,eventD,eventM):
        if admin == True:
            eventlist.remove([event_name,eventD,eventM])
        else:
            print("You don't have access to our event site")



class interface:

    def __init__(self,root):
        self.fenetre = root
        self.fenetre.title("Login System")
        self.fenetre.geometry("1100x640+100+50")
        self.fenetre.iconbitmap("cinemaicon.ico")

        # ***** Background *****
        self.bg = ImageTk.PhotoImage(Image.open('logo1.jpg'))
        self.bg_label = Label(self.fenetre, image = self.bg)
        self.bg_label.place(x = 0, y = 0)


        #****** Login Frame ******
        self.Frame_login = Frame(self.fenetre, bg = "white", relief = RAISED)
        self.Frame_login.place(x = 150, y = 200, height = 400, width = 480)


        #***** Logo de Mairie *****
        self.logo = ImageTk.PhotoImage(Image.open('mairie_logo.png'))
        self.logo_label = Label(self.fenetre, image=self.logo, bg='black')
        self.logo_label.place(x = 290, y = 140, width = 200 ,height=150)


        lbl_user = Label(self.Frame_login, text = 'Username', font = ('Goudy old style', 12, 'bold'),fg = 'gray', bg = 'white')
        lbl_user.place(x = 90, y = 140)

        self.txt_user = Entry(self.Frame_login, font = ('times new roman', 12), bg = 'lightgray')
        self.txt_user.place(x = 90, y = 170, width = 300, height = 35)

        lbl_pass = Label(self.Frame_login, text = 'Password', font = ('Goudy old style', 12, 'bold'), fg = 'gray', bg = 'white')
        lbl_pass.place(x = 90, y = 215)

        self.txt_pass = Entry(self.Frame_login, font = ('times new roman', 12), bg = 'lightgray', show ='*')
        self.txt_pass.place(x = 90, y = 245, width = 300, height = 35)


        self.new_account = Button(self.Frame_login, text = 'Create a new account', bd = 0, bg = 'white', fg = '#f93949', font = ('times new roman', 12))
        self.new_account.place(x = 90, y = 285)
        self.login_button = Button(self.Frame_login, text = 'Login', relief = RAISED, command = self.login, fg = 'white', bg = '#f01934', font = ('times new roman', 15))
        self.login_button.place(x = 150, y = 340, width = 180, height = 40)

    def efface(self):
        for c in self.fenetre.winfo_children():
            c.destroy()

    def login(self):
        global success
        global admin_use
        success = False
        admin_user = False
        file = open("users_details.txt","r")
        for i in file:
            a, b, c = i.split(",")
            c = c.strip()
            if(a == self.txt_user.get()) and (b == self.txt_pass.get()):
                success = True
                if(c == '1'):
                    admin_user = True
        file.close()
        if success:
           return self.afficher_menu()
        else:
            self.message2_label = Label(self.Frame_login, text = 'Wrong username or password', fg = 'red', bg = 'white', font = ('Goudy old style', 12, 'bold'))
            self.message2_label.place(x = 120, y = 100)


    def afficher_menu(self):
        # ***** Destroying the old labels *****
        self.efface()

        self.line = 0
        self.fenetre.config(background = 'white')
        self.fenetre.title("Gestion du cinéma club")
        self.fenetre.geometry("1550x900+0+0")

        # ***** New title *****
        title_label = Label(self.fenetre, text = 'Gestion du cinéma club', fg = 'white', bg = '#008080', font = ('Times new roman', 20))
        title_label.place(relwidth = 1, height = 45)
        deconnecter = Button(self.fenetre, text = 'deconnecter', bd = 0, fg = '#f0f8ff', bg = '#008080', font = ('Times new roman', 12))
        deconnecter.place(x = 1400, y = 8)

        # ***** Cadre des informations *****
        #Contient les différents boutons (ajouter - supprimer - modifier - consulter)
        #Contient tous les évènements ajoutés

        self.cadre_info = Frame(self.fenetre, relief = RAISED, borderwidth = 3, bg = '#eeeeee')
        self.cadre_info.place(x = 0, y = 55, width = 500, height = 740)

        #titre de cadre à gauche
        cadre_title = Label(self.cadre_info, text ='Evènements du cinéma', fg = 'black', bg = '#ffc0cb', font = ('Times new roman', 15))
        cadre_title.place(relwidth = 1, height = 40)

        # Construire des colonnes (Num, Evènement, Date, Salle, Type, Debut, Fin)
        self.cadreNum = LabelFrame(self.cadre_info, text = 'Num',fg = 'black', bg = '#eeeeee', font=('Times new roman', 11))
        self.cadreNum.place(x=0, y= 95,width = 45, height =635)

        for num in range(1,28):
            label = Label(self.cadreNum, text= num, fg='black', bg='#eeeeee',font=('Times new Roman', 11))
            label.grid(column=1,row=num)

        self.cadreEvent = LabelFrame(self.cadre_info, text='Evènement',fg = 'black', bg = '#eeeeee', font = ('Times new roman', 11))
        self.cadreEvent.place(x=45, y=95, width=130, height =635)

        self.cadreDate = LabelFrame(self.cadre_info, text='Date',fg = 'black', bg = '#eeeeee', font = ('Times new roman', 11))
        self.cadreDate.place(x=175, y=95, width=130, height =635)

        self.cadreSalle = LabelFrame(self.cadre_info, text='Salle', fg='black', bg='#eeeeee', font=('Times new roman', 11))
        self.cadreSalle.place(x=295, y=95, width=50, height =635)
        self.cadreType = LabelFrame(self.cadre_info, text='Type', fg='black', bg='#eeeeee', font=('Times new roman', 11))
        self.cadreType.place(x=345, y=95, width=50, height =635)
        self.cadreDebut = LabelFrame(self.cadre_info, text='Debut', fg='black', bg='#eeeeee', font=('Times new roman', 11))
        self.cadreDebut.place(x=395, y=95, width=55, height =635)
        self.cadreFin = LabelFrame(self.cadre_info, text='Fin', fg='black', bg='#eeeeee', font=('Times new roman', 11))
        self.cadreFin.place(x=450, y=95, width=45, height =635)

        # ***** Calling Memorisation function *****
        self.memoriser_event()

        add_button = Button(self.cadre_info, text='Ajouter', command=self.affiche_add_event, relief=RAISED,fg='#008080', bg='#f0f8ff', font=('times new roman', 12))
        add_button.place(x=10, y=50)


        #delete_button = Button(self.cadre_info, text = '-', bd = 0, fg ='white', bg = '#f0f8ff', font = ('times new roman', 12))
        #delete_button.place(x = 90, y = 230)

        #edit_button = Button(self.cadre_info, text = 'Modifier', bd = 0, fg ='white', bg = '#eeeeee', font = ('times new roman', 12))
        #edit_button.place(x = 90, y = 260)


        # ***** Calendrier *****
        self.calendrier_cadre = Frame(self.fenetre, relief = RAISED, borderwidth = 5, bg='#eeeeee')
        self.calendrier_cadre.place(x = 500, y = 55, relwidth = 1, height = 740)

        #Titre du cadre calendrier
        cal_title = Label(self.calendrier_cadre, text='Calendrier du cinéma', fg='black', bg='#407294',font=('Times new roman', 15),)
        cal_title.place(relwidth = 1, height = 40)

        # ***** Date du jour ******

        t = date.today()
        mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre',
                'Novembre', 'Décembre']

        month_label = Label(self.calendrier_cadre, text=mois[t.month - 1], font=('Myriad Pro', 17, 'bold'), fg='black',bg='#eeeeee')
        month_label.place(x=10, y=50)
        year_label = Label(self.calendrier_cadre, text=t.year, font=('Myriad Pro', 17), fg='black', bg='#eeeeee')
        year_label.place(x=65, y=50)





    def affiche_add_event(self):
        self.add_fenetre = Toplevel(self.fenetre)
        self.add_fenetre.title("Ajouter un évènement")
        self.add_fenetre.geometry("720x270")

        # Entry 1
        label = Label(self.add_fenetre, text="Nom du Film",font = ('Times new roman', 11))
        label .grid(column=0, row=1, padx=3, pady=3)

        # Entry 2
        label = Label(self.add_fenetre, text="Date de l'évènement",font = ('Times new roman', 11))
        label.grid(column=0, row=2, padx=3, pady=3)

        # Entry 3
        label = Label(self.add_fenetre, text="Salle",font = ('Times new roman', 11))
        label.grid(column=0, row=3, padx=3, pady=3)

        # Entry 4
        label = Label(self.add_fenetre, text="Type de l'evenement \n (singulier/film)",font = ('Times new roman', 11))
        label.grid(column=0, row=4, padx=3, pady=3)

        # Entry 5
        label = Label(self.add_fenetre, text="L'horaire du début",font = ('Times new roman', 11))
        label.grid(column=0, row=5, padx=3, pady=3)

        # Entry 6
        label = Label(self.add_fenetre, text="L'horaire de la Fin",font = ('Times new roman', 11))
        label.grid(column=0, row=6, padx=3, pady=3)


        self.e1 = Entry(self.add_fenetre,font = ('Times new roman', 11), width = 40)
        self.e1.grid(column=1, row=1)

        self.e2 = Entry(self.add_fenetre,font = ('Times new roman', 11), width = 5)
        self.e2.grid(column=1, row=2)

        self.month_value = ttk.Combobox(self.add_fenetre,values=('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre','Novembre', 'Décembre'),state = 'readonly')
        self.month_value.grid(column = 2, row = 2)

        t = date.today()
        year_later = t + timedelta(days = 730)

        self.year_value = ttk.Combobox(self.add_fenetre,values = (t.year,year_later.year),state = 'readonly')
        self.year_value.grid(column = 3, row = 2)

        self.e3 = Entry(self.add_fenetre,font = ('Times new roman', 11), width = 40)
        self.e3.grid(column=1, row = 3)

        self.e4 = Entry(self.add_fenetre,font = ('Times new roman', 11), width = 40)
        self.e4.grid(column=1, row=4)
        self.e5 = Entry(self.add_fenetre,font = ('Times new roman', 11), width = 40)
        self.e5.grid(column=1, row=5)
        self.e6 = Entry(self.add_fenetre,font = ('Times new roman', 11), width = 40)
        self.e6.grid(column=1, row=6)


        bouton_valider = Button(self.add_fenetre, text='Valider', command = self.affiche_event_cadre, font = ('Times new Roman', 12), anchor = CENTER, relief = RAISED, fg = '#008080', bg = '#f0f8ff')
        bouton_valider.place(x = 350, y = 220)

        #self.add_fenetre.mainloop()

    # ***** Enregistrer les évènements ajoutés dans un fichier
    def enregistrer_event(self):
        self.event_list = [self.e1.get(), self.e2.get(), self.month_value.get(), self.year_value.get(), self.e3.get(),self.e4.get(), self.e5.get(), self.e6.get()]
        event = map(lambda x: x + ',', self.event_list)
        event_file = open("event_list.txt", "a")
        event_file.writelines(event)
        event_file.writelines("\n")
        event_file.close()


    # ***** Fonction pour afficher les évènements ajoutés dans le cadre à gauche *****
    def affiche_event_cadre(self):
        self.enregistrer_event()
        cpt_list = 0
        cadre_list =  [self.cadreEvent,self.cadreDate,self.cadreSalle,self.cadreType, self.cadreDebut,self.cadreFin]
        for i in range(len(cadre_list)):
            if i == 1:
                label = Label(cadre_list[i], text=self.event_list[cpt_list], fg='black', bg='#eeeeee',font=('Times new Roman', 10))
                label.grid(column = 1, row = self.line)
                label = Label(cadre_list[i], text=self.event_list[cpt_list+1], fg='black', bg='#eeeeee',font=('Times new Roman', 10))
                label.grid(column=2, row = self.line)
                label = Label(cadre_list[i], text=self.event_list[cpt_list+2], fg='black', bg='#eeeeee',font=('Times new Roman', 10))
                label.grid(column = 3, row = self.line)
                cpt_list=4
            else:
                label = Label(cadre_list[i], text=self.event_list[cpt_list], fg='black', bg='#eeeeee',font=('Times new Roman', 10))
                label.grid(column = 1, row = self.line)
                cpt_list+=1

        self.line += 1
        return self.line

    # ***** Fonction de Mémorisation *****
    def memoriser_event(self):
        cpt_list = 0
        cadre_list = [self.cadreEvent, self.cadreDate, self.cadreSalle, self.cadreType, self.cadreDebut, self.cadreFin]

        event_file = open("event_list.txt", "r")
        for event in event_file:
            for cadre in range(len(cadre_list)):
                event_list = event.split(",")
                event_list.pop(8)
                if cadre == 1:
                    label = Label(cadre_list[cadre], text=event_list[cadre], fg='black', bg='#eeeeee',font=('Times new Roman', 10))
                    label.grid(column=1, row=self.line)
                    label = Label(cadre_list[cadre], text=event_list[cadre+1], fg='black', bg='#eeeeee',font=('Times new Roman', 10))
                    label.grid(column=2, row=self.line)
                    label = Label(cadre_list[cadre], text=event_list[cadre+2], fg='black', bg='#eeeeee',font=('Times new Roman', 10))
                    label.grid(column=3, row=self.line)
                    cadre = 4

                else:
                    label = Label(cadre_list[cadre], text=event_list[cadre], fg='black', bg='#eeeeee',font=('Times new Roman', 10))
                    label.grid(column=1, row=self.line)
                    cpt_list += 1

            self.line += 1
        return self.line































root = Tk()
i = interface(root)

root.mainloop()

"""


t = date.today()
print(t)
jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
mois = ['Jan', 'Fev', 'Mars','Avr', 'Mai', 'Juin', 'Juillet', 'Aout', 'Sept', 'Oct', 'Nov', 'Dec']

#ev1 = Event("HarryPoter")
u1 = UtilisateurAdmin()
u1.login()
u1.ajouter("HarryPoter",jours[t.weekday()],mois[t.month-1]) #t.day t.month t.year)

u2 = UtilisateurAdmin()
u2.login()


print(u2.geteventlist())
u2.ajouter("Avengers",jours[t.weekday()],mois[t.month-1])
print(u2.geteventlist())

u1.supprimer("HarryPoter",jours[t.weekday()],mois[t.month-1])
print(u2.geteventlist())
print(u1.name)
print(u2.name)

"""