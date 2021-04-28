# -*- coding: utf-8 -*-

class Utilisateur:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UtilisateurAdmin(Utilisateur):
    def __init__(self, username, password):
        super().__init__(username, password)
