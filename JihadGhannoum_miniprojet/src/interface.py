# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from PIL import Image, ImageTk
import calendar

# dans la fonction affiche_menu_login(), j'ai utilisé PIL pour insérer des images donc si vous avez déjà installer le module PIL (pillow)
# ça va marcher très bien et vous pouvez enlever les commentaires dans les 2 parties (***** Background *****) et (***** Logo de Mairie *****)

class Interface:

    def __init__(self, root):
        self.fenetre = root
        self.affiche_menu_login()

    def affiche_menu_login(self):
        self.fenetre.title("Authentification")
        self.fenetre.geometry("1100x640+100+50")
        self.fenetre.iconbitmap("login_icon.ico")

        # ***** Background *****
        # Si vous avez  PIL, vous pouvez enlever les commentaires de cette partie pour afficher le background
        """
        self.bg = PIL.ImageTk.PhotoImage(Image.open('logo1.jpg'))
        self.bg_label = Label(self.fenetre, image=self.bg)
        self.bg_label.place(x=0, y=0)
        """

        # ****** Login Frame ******
        self.Frame_login = Frame(self.fenetre, bg="white", relief=RAISED)
        self.Frame_login.place(x=150, y=200, height=400, width=480)

        # ***** Logo de Mairie *****
        # Si vous avez  PIL, vous pouvez enlever les commentaires de cette partie pour afficher le logo du mairie
        """
        self.logo = PIL.ImageTk.PhotoImage(Image.open('mairie_logo.png'))
        self.logo_label = Label(self.fenetre, image=self.logo, bg='black')
        self.logo_label.place(x=290, y=140, width=200, height=150)
        """

        lbl_username = Label(self.Frame_login, text='Identifiant', font=('Goudy old style', 12, 'bold'), fg='gray', bg='white')
        lbl_username.place(x=90, y=140)

        self.txt_username = Entry(self.Frame_login, font=('times new roman', 12), bg='lightgray')
        self.txt_username.place(x=90, y=170, width=300, height=35)

        lbl_pass = Label(self.Frame_login, text='Mot de passe', font=('Goudy old style', 12, 'bold'), fg='gray', bg='white')
        lbl_pass.place(x=90, y=215)

        self.txt_password = Entry(self.Frame_login, font=('times new roman', 12), bg='lightgray', show='*')
        self.txt_password.place(x=90, y=245, width=300, height=35)

        self.new_account = Button(self.Frame_login, text='Je crée mon compte', bd=0, bg='white', fg='#f93949', font=('times new roman', 12))
        self.new_account.place(x=90, y=285)

        self.login_button = Button(self.Frame_login, text='Se connecter', relief=RAISED, command=self.seconnecter, fg='white', bg='#f01934', font=('times new roman', 15))
        self.login_button.place(x=150, y=340, width=180, height=40)

    # ***** Effacer la fenêtre pricipale et ses filles *****
    def efface(self):
        for c in self.fenetre.winfo_children():
            c.destroy()

    # ***** se connecter *****
    def seconnecter(self):
        self.admin_user = False
        success = False
        file = open("users_details.txt", "r")
        for i in file:
            a, b, c = i.split(",")
            c = c.strip()
            if(a == self.txt_username.get()) and (b == self.txt_password.get()):
                success = True
                if c == '1':
                    self.admin_user = True
        file.close()
        if success:
           self.afficher_main_menu()
        else:
            self.message2_label = Label(self.Frame_login, text='Wrong username or password', fg='red', bg='white', font=('Goudy old style', 11, 'bold'))
            self.message2_label.place(x=120, y=100)
        return self.admin_user

    # ***** Deconnecter *****
    def deconnecter(self):
        self.efface()
        self.affiche_menu_login()

    # ***** Affichage du menu principale *****
    def afficher_main_menu(self):
        self.efface()
        self.line = 0
        self.num_event = 0
        self.cpt_event = 1
        self.fenetre.config(background='white')
        self.fenetre.iconbitmap("cinemaicon.ico")
        self.fenetre.title("Gestion du cinéma club")
        self.fenetre.geometry("1550x900+0+0")

        # Titre du menu pricipale
        title_label = Label(self.fenetre, text='Gestion du cinéma club', fg='#008080', bg='#b0e0e6', font=('Times new roman', 20))
        title_label.place(relwidth=1, height=45)

        deconnecter = Button(self.fenetre, text='deconnecter', command=self.deconnecter, bd=0, fg='#468499', bg='#b0e0e6', font=('Times new roman', 12))
        deconnecter.place(x=1400, y=8)

        # ***** Calendrier *****
        self.calendrier_cadre = Frame(self.fenetre, relief=RAISED, borderwidth=3, bg='white')
        self.calendrier_cadre.place(x=445, y=55, relwidth=1, height=740)

        # Contient les différents boutons (ajouter - supprimer - modifier - consulter)
        # Contient tous les évènements ajoutés
        self.cadre_info = Frame(self.fenetre, relief=RAISED, borderwidth=3, bg='#fefefa')
        self.cadre_info.place(x=0, y=55, width=445, height=740)

        # titre de cadre à gauche
        cadre_title = Label(self.cadre_info, text='Evènements du cinéma', bg='#ffc3a0', fg='#008080', font=('Times new roman', 15))
        cadre_title.place(relwidth=1, height=40)

        self.affiche_bouton_new_admin()

        # Frames du Cadre à gauche
        self.affiche_cadre_info_frame()

        t = date.today()
        self.cal = Calendar(self.calendrier_cadre, selectmode='day', year=t.year, month=t.month, background='#EE3B3B', foreground='white', headersbackground='#F0F8FF', normalbackground='white', borderwidth=2, tooltipforeground='#99182C', tooltipbackground='#F08080')
        self.cal.place(x=0, y=0, width=1090, relheight=1)

        # ***** Calling Memorisation function *****
        self.memoriser_event()

        # Bouton pour ajouter
        self.add_button = Button(self.cadre_info, text='Ajouter', command=self.affiche_fenetre_add, relief=RAISED, fg='#008080', bg='#f0f8ff', font=('times new roman', 12))
        self.add_button.place(x=10, y=50)
        if self.admin_user == False:
            self.add_button.destroy()

    # ***** Construire frmae pour le cadre d'infos *****
    def affiche_cadre_info_frame(self):
        # Construire des colonnes (Num, Evènement, Date, Salle, Type, Debut, Fin)
        self.cadreNum = LabelFrame(self.cadre_info, text='Num', fg='black', bg='#fefefa', font=('Times new roman', 11))
        self.cadreNum.place(x=0, y=95, width=45, height=635)

        self.cadreEvent = LabelFrame(self.cadre_info, text='Evènement', fg='black', bg='#fefefa', font=('Times new roman', 11))
        self.cadreEvent.place(x=45, y=95, width=130, height=635)

        self.cadreDate = LabelFrame(self.cadre_info, text='Date', fg='black', bg='#fefefa', font=('Times new roman', 11))
        self.cadreDate.place(x=175, y=95, width=65, height=635)

        self.cadreSalle = LabelFrame(self.cadre_info, text='Salle', fg='black', bg='#fefefa', font=('Times new roman', 11))
        self.cadreSalle.place(x=240, y=95, width=50, height=635)

        self.cadreType = LabelFrame(self.cadre_info, text='Type', fg='black', bg='#fefefa', font=('Times new roman', 11))
        self.cadreType.place(x=290, y=95, width=50, height=635)

        self.cadreDebut = LabelFrame(self.cadre_info, text='Debut', fg='black', bg='#fefefa', font=('Times new roman', 11))
        self.cadreDebut.place(x=340, y=95, width=55, height=635)

        self.cadreFin = LabelFrame(self.cadre_info, text='Fin', fg='black', bg='#fefefa', font=('Times new roman', 11))
        self.cadreFin.place(x=395, y=95, width=42, height=635)

    # ***** Bouton supprimer - Bouton trier - Bouton modifier *****
    def affiche_boutons(self):
        if self.cpt_event > 1:
            self.delete_icon = PhotoImage(file='deleteicon.png')
            self.delete_image = self.delete_icon.subsample(12, 12)
            self.delete_button = Button(self.cadre_info, image=self.delete_image, command=self.affiche_fenetre_delete, text='', bg='#fefefa', compound=CENTER, border=0)
            self.delete_button.place(x=405, y=55)
            self.delete_button.image = self.delete_image

            self.edit_icon = PhotoImage(file='editicon.png')
            self.edit_image = self.edit_icon.subsample(12, 12)
            self.edit_button = Button(self.cadre_info, image=self.edit_image, command=self.affiche_fenetre_edit, text='', bg='#fefefa', compound=CENTER, border=0)
            self.edit_button.place(x=372, y=55)
            self.edit_button.image = self.edit_image
            self.box_value = StringVar()
            self.trier_box = ttk.Combobox(self.cadre_info, textvariable=self.box_value, values=('Nom', 'Date'), state='readonly')
            self.trier_box.place(x=90, y=55, width=70)
            self.trier_bouton = Button(self.cadre_info, text='Trier', bd=0, command=self.trier_event, font=('times new roman', 11), bg='#fefefa', fg='#008080')
            self.trier_bouton.place(x=165, y = 55)

            # Changement si l'utilisateur n'est pas un administrateur
            if self.admin_user == False:
                self.delete_button.destroy()
                self.edit_button.destroy()
                self.trier_box.place(x=10, y=55, width=70)
                self.trier_bouton.place(x=85,y=55)

    # ***** Affichage d'une nouvelle fenêtre pour choisir le numéro de l'évènement à supprimer  *****
    def affiche_fenetre_delete(self):
        self.supp_fenetre = Toplevel(self.fenetre)
        self.supp_fenetre.title("Suppression")
        self.supp_fenetre.geometry("400x200")
        self.supp_fenetre.config(background='#DBE6E0')
        self.supp_fenetre.resizable(False, False)

        label = Label(self.supp_fenetre, text="Veuillez entrer le numéro de l'évènement à supprimer", bg='#DBE6E0', fg='#426352', font=('times new roman', 12))
        label.pack()

        self.supp_event = IntVar()
        Spinbox(self.supp_fenetre, from_=0, to=self.num_event, textvariable=self.supp_event, state='readonly').pack(pady=10)

        self.bouton_supp = Button(self.supp_fenetre, text='Supprimer', font=('Times new Roman', 12), command=self.supprimer_event, anchor=CENTER, relief=RAISED, fg='#426352', bg='#f0f8ff')
        self.bouton_supp.place(x=165, y=150)

    # ***** Affichage d'une nouvelle fenêtre pour choisir le numéro de l'évènement à modifier  *****
    def affiche_fenetre_edit(self):
        self.edit_fenetre = Toplevel(self.fenetre)
        self.edit_fenetre.title("Modification")
        self.edit_fenetre.geometry("400x200")
        self.edit_fenetre.config(background='#DBE6E0')
        self.edit_fenetre.resizable(False, False)

        label = Label(self.edit_fenetre, text="Veuillez entrer le numéro de l'évènement à modifier", bg='#DBE6E0', fg='#426352', font=('times new roman', 12))
        label.pack()

        self.edit_event = IntVar()
        Spinbox(self.edit_fenetre, from_=0, to=self.num_event, textvariable=self.edit_event, state='readonly').pack(pady=10)

        self.bouton_mod = Button(self.edit_fenetre, text='Modifier', font=('Times new Roman', 12), command=self.recuperer_info, anchor=CENTER, relief=RAISED, fg='#426352', bg='#f0f8ff')
        self.bouton_mod.place(x=165, y=150)

    # ***** Affichage d'une nouvelle fenêtre pour ajouter des évènements *****
    def affiche_fenetre_add(self):
        self.add_fenetre = Toplevel(self.fenetre)
        self.add_fenetre.title("Ajouter un évènement")
        self.add_fenetre.geometry("490x270")
        self.add_fenetre.config(background='#DBE6E0')

        label_list = ["Nom du Film", "Date de l'évènement", "Salle", "Type de l'evenement \n (F/S)", "L'horaire du début", "L'horaire de la Fin"]

        # Création de 6 labels utilisés pour l'Entry
        for i in range(0, 6):
            label = Label(self.add_fenetre, text=label_list[i], font=('Times new roman', 11), bg='#DBE6E0', fg='#426352')
            label.grid(column=0, row=i+1, padx=3, pady=3)

        self.e1 = Entry(self.add_fenetre, font=('Times new roman', 11), width=40)
        self.e1.grid(column=1, row=1)

        self.e2 = DateEntry(self.add_fenetre, width=12, background='#3A66A7', foreground='white', headersbackground='#CAE1FF', borderwidth=2, state='readonly')
        self.e2.grid(column=1, row=2)

        self.e3 = Entry(self.add_fenetre, font=('Times new roman', 11), width=40)
        self.e3.grid(column=1, row=3)

        self.e4 = Entry(self.add_fenetre, font=('Times new roman', 11), width=40)
        self.e4.grid(column=1, row=4)

        self.e5 = Entry(self.add_fenetre, font=('Times new roman', 11), width=40)
        self.e5.grid(column=1, row=5)

        self.e6 = Entry(self.add_fenetre, font=('Times new roman', 11), width=40)
        self.e6.grid(column=1, row=6)

        self.bouton_valider = Button(self.add_fenetre, text='Valider', command=self.affiche_event, font=('Times new Roman', 12), anchor=CENTER, relief=RAISED, fg='#426352', bg='#f0f8ff')
        self.bouton_valider.place(x=220, y=225)

    # ***** Enregistrer les évènements ajoutés dans un fichier *****
    def enregistrer_event(self):
        self.event_list = [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e5.get(), self.e6.get()]
        f = open("event_list.txt", "a")
        for element in self.event_list:
            f.write(element)
            f.write(",")
        f.write("\n")
        f.close()

    # ***** Affichage des évènements dans le cadre à gauche en précisant le nombre maximale d'évènement possible *****
    def affiche_event(self):
        if self.cpt_event > 29:
            return messagebox.showwarning("Interdit", "Vous avez ajouté le maximum possible.")
        else:
            self.ajouter_event()

    # ***** Ajouter des évènements *****
    def ajouter_event(self):
        self.enregistrer_event()
        cpt_list = 0
        cadre_list = [self.cadreNum, self.cadreEvent, self.cadreDate, self.cadreSalle, self.cadreType, self.cadreDebut, self.cadreFin]
        for i in range(len(cadre_list)):
            if i == 0:
                self.ev_label = Label(cadre_list[i], text=self.cpt_event, fg='black', bg='#fefefa', font=('Times new Roman', 10), anchor='center')
                self.ev_label.grid(column=1, row=self.line)
            else:
                self.ev_label = Label(cadre_list[i], text=self.event_list[cpt_list], fg='black', bg='#fefefa', font=('Times new Roman', 10), anchor='center')
                self.ev_label.grid(column=1, row=self.line)
                cpt_list += 1

        self.affiche_event_calendrier()
        self.line += 1
        self.cpt_event += 1
        self.num_event += 1
        if self.num_event == 1:
            self.affiche_boutons()

        return self.line and self.cpt_event and self.num_event

    # ***** Affichage des évènements dans le calendrier *****
    def affiche_event_calendrier(self):
        d = self.event_list[1]
        t = d.split("/")
        mois = int(t[0])
        jour = int(t[1])
        annee = int("20" + t[2])
        date = self.cal.datetime(annee, mois, jour)

        if self.event_list[3] == 'F' or self.event_list[3] == 'f':
            self.cal.calevent_create(date, self.event_list[0], 'Film')
            self.cal.tag_config('Film', background='#6897bb', foreground='#b0e0e6')
        else:
            self.cal.calevent_create(date, self.event_list[0], 'Singulier')
            self.cal.tag_config('Singulier', background='#FA8072', foreground='#b0e0e6')

    # ***** Mémorisation des évènements *****
    def memoriser_event(self):
        cadre_list = [self.cadreNum, self.cadreEvent, self.cadreDate, self.cadreSalle, self.cadreType, self.cadreDebut, self.cadreFin]
        event_file = open("event_list.txt", "r")
        self.cal.calevent_remove('all')

        for event in event_file:
            for cadre in range(len(cadre_list)):
                self.event_list = event.split(",")
                self.event_list.pop(6)
                if cadre == 0:
                    self.ev_label = Label(cadre_list[cadre], text=self.cpt_event, fg='black', bg='#fefefa', font=('Times new Roman', 10), anchor='center')
                    self.ev_label.grid(column=1, row=self.line)
                else:
                    self.ev_label = Label(cadre_list[cadre], text=self.event_list[cadre-1], fg='black', bg='#fefefa', font=('Times new Roman', 10), anchor='center')
                    self.ev_label.grid(column=1, row=self.line)
            self.affiche_event_calendrier()
            self.line += 1
            self.cpt_event += 1
            self.num_event += 1

        event_file.close()
        self.affiche_boutons()
        return self.line and self.cpt_event

    # ***** Trier les évènements *****
    def trier_event(self):
        if self.box_value.get() == 'Nom':
            self.trier_nom()
        elif  self.box_value.get() == 'Date':
            self.trier_date()

        self.affiche_cadre_info_frame()
        self.line = 0
        self.num_event = 0
        self.cpt_event = 1
        self.memoriser_event()

    # ***** Trier selon le nom *****
    def trier_nom(self):
        lines = open("event_list.txt", "r").readlines()
        output = open("event_list.txt", 'w')
        for line in sorted(lines, key=lambda line: line.split()[0]):
            output.write(line)
        output.close()

    # ***** Trier selon la date *****
    def trier_date(self):
        lines = open("event_list.txt", "r").readlines()
        output = open("event_list.txt", 'w')
        for line in sorted(lines, key=lambda line: line.split()[0][1]):
            output.write(line)
        output.close()

    # ***** Supprimer des évènements *****
    def supprimer_event(self):
        self.supprimer_event_fichier()
        if self.valide:
            self.affiche_cadre_info_frame()
            self.line = 0
            self.num_event = 0
            self.cpt_event = 1
            self.memoriser_event()
            self.message_confi_supprimer()

    # ***** Supprimer les évènemenst dans le fichier txt *****
    def supprimer_event_fichier(self):
        self.valide = False
        val_supp = self.supp_event.get()
        if val_supp == 0:
            return messagebox.showwarning('Erreur', 'Le numéro qui a été entré n\'est pas valide.\n Veuillez réessayer')
        else:
            if self.message_verif_supprimer():
                event_file = open("event_list.txt", "r")
                lines = event_file.readlines()
                event_file.close()
                ev =lines[val_supp - 1].split(",")
                self.cal.calevent_remove(ev[0])
                del lines[val_supp - 1]

                new_file = open("event_list.txt", "w")
                for line in lines:
                    new_file.write(line)
                new_file.close()
                self.valide = True

    # ***** vérification de la supression/modification des évènemenst *****
    def message_verif_supprimer(self):
        return messagebox.askyesno("Suppression d'un évènement", "Voulez vous supprimer cet évènement?")

    # ***** Confirmation de la supression des évènemenst *****
    def message_confi_supprimer(self):
        return messagebox.showinfo("Information", "L'évènement est suprimé")

    # ***** Modifier les évènements *****
    def modifier_event(self):
        self.enregistrer_event()
        self.affiche_cadre_info_frame()
        self.line = 0
        self.num_event = 0
        self.cpt_event = 1
        self.memoriser_event()
        self.message_confi_modifier()

    # ***** Recupérer les données et les mettre dans add_fenetre *****
    def recuperer_info(self):
        val_edit = self.edit_event.get()
        if val_edit > 0:
            self.affiche_fenetre_add()
            self.bouton_valider.configure(command=self.modifier_event)
            self.add_fenetre.title("Modification d'un évènement")
            self.entry = [self.e1, self.e2, self.e3, self.e4, self.e5, self.e6]
            event_file = open("event_list.txt", "r")
            lines = event_file.readlines()
            event_file.close()

            lines = lines[val_edit - 1].split(",")
            for j in range(len(lines)-1):
                self.entry[j].insert(0, lines[j])

            event_file = open("event_list.txt", "r")
            lines = event_file.readlines()
            event_file.close()

            del lines[val_edit - 1]

            new_file = open("event_list.txt", "w")
            for line in lines:
                new_file.write(line)
            new_file.close()
        else:
            return messagebox.showwarning('Erreur', 'Le numéro qui a été entré n\'est pas valide.\n Veuillez réessayer')


    # ***** Confirmation de la modification des évènemenst *****
    def message_confi_modifier(self):
        return messagebox.showinfo("Information", "L'évènement est modifié")

    # ***** Affichage d'une nouvelle fenêtre pour ajouter un Administrateur *****
    def affiche_new_admin(self):
        self.fenetre_new_admin = Toplevel(self.fenetre)
        self.fenetre_new_admin.title("Ajouter un Administrateur")
        self.fenetre_new_admin.geometry("400x200")
        self.fenetre_new_admin.resizable(False, False)

        label = Label(self.fenetre_new_admin, text='Veuillez sélectionner un utilisateur', fg='black', font=('times new roman', 12))
        label.pack()

        self.new_admin = StringVar()
        new_admin_box = ttk.Combobox(self.fenetre_new_admin, textvariable=self.new_admin, values=('Bill', 'Dupont', 'Eddy', 'Jason', 'Martin'), state='readonly', width=15)
        new_admin_box.pack(pady=10)

        bouton_valider = Button(self.fenetre_new_admin, text='Valider', command=self.ajouter_admin, font=('Times new Roman', 12), anchor=CENTER, relief=RAISED, fg='#008080', bg='#f0f8ff')
        bouton_valider.place(x=170, y=150)

    def affiche_bouton_new_admin(self):
        self.bouton_new_admin = Button(self.fenetre, text='Ajouter un Administrateur', command=self.affiche_new_admin, bd=0, fg='#468499', bg='#b0e0e6', font=('Times new roman', 12))
        self.bouton_new_admin.place(x=5, y=8)
        if self.admin_user == False:
            self.bouton_new_admin.destroy()

    # ***** Ajouter un Admin *****
    def ajouter_admin(self):
        f = open("users_details.txt", "r")
        lines = f.readlines()
        l = ""
        replaced = []

        for line in lines:
            line = line.split(",")
            if line[0] == self.new_admin.get():
                if line[2] == "0\n":
                    line[2] = "1\n"
                    self.meesage_confi_new_admin()
                elif line[2] == "1\n":
                    self.message_user_isadmin()
            l = ",".join(line)
            replaced.append(l)
        lines =replaced

        new_file = open("users_details.txt", "w")
        for line in lines:
            new_file.write(line)
        new_file.close()

    # ***** Message d'erreur si l'utilisateur est un Administrateur *****
    def message_user_isadmin(self):
        return messagebox.showwarning("Erreur", "\"" + self.new_admin.get() + "\"" + " est un Administrateur")

    # ***** Confirmation que l'utilisateur devient un administrateur *****
    def meesage_confi_new_admin(self):
        return messagebox.showinfo("Information", "Vous avez ajouté " + "\"" + self.new_admin.get() + "\"" + " comme Administrateur")
