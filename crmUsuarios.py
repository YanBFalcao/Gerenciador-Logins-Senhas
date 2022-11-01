from csv import excel
import datetime as dt
from fileinput import close
import os
from typing import Container
import pandas as pd
from openpyxl import *
from msilib.schema import ComboBox

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

import menu as mn

# ================================================= ~~ =================================================
#                                                FUNÇÕES
# ================================================= ~~ =================================================

#colocar argumentos: login e senha para comparação com banco de dados
def loginSistema():
    messagebox.showinfo("Sucesso!", "Bem Vindo!")
    mn.menuPrincipal()

def clearDados():
    #limpar  tudo, mensagem abaixo somente teste
    messagebox.showinfo("Limpeza ⚠️","Limpeza realizada com sucesso")

def novoBanco():
    messagebox.showinfo("Sucesso!", "Botão cadastro banco criado com sucesso!")

# ================================================= ~~ =================================================
#                                                FUNÇÕES
# ================================================= ~~ =================================================

# ================================================= ~~ =================================================
#                                                FORMULÁRIO
# ================================================= ~~ =================================================

# Cria o Form
crmLogin = tk.Tk()

#define o tamanho do form que desejar
#crmUsuarios.geometry("520x420")

# Titulo da janela
crmLogin.title("Usuários e Senhas")

# ========================= ~~ =========================
#                    FORMULÁRIO (LOGIN)
# ========================= ~~ =========================

label_crmLogin = tk.Label(text="Bem vindo ao Sistema de \n Gerenciamento de Usuários e Senhas CORBAN. \n" 
                         "Para iniciar, insira o seu login e senha.")
label_crmLogin.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)


# Label na janela
label_crmLogin = tk.Label(text="Login")
label_crmLogin.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'nswe', columnspan = 2)
#padx => É o distanciamento/margem do eixo x

entry_crmLogin_nome = tk.Entry()
entry_crmLogin_nome.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'nswe', columnspan = 2)



label_crmLogin = tk.Label(text="Senha:")
label_crmLogin.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = 'nswe', columnspan = 2)

entry_crmLogin_nome = tk.Entry()
entry_crmLogin_nome.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'nswe', columnspan = 2)


botao_crmLogin_login = tk.Button(crmLogin, text="Entrar", command=loginSistema)
botao_crmLogin_login.grid(row=5, column=1, padx = 10, pady = 10, sticky = 'nswe', columnspan = 4)

botao_sair = tk.Button(crmLogin, text="Sair", command=crmLogin.destroy)
botao_sair.grid(row=6, column=1, padx = 10, pady = 10, sticky = 'nswe', columnspan = 4)


# ========================= ~~ =========================
#                    FORMULÁRIO (LOGIN)
# ========================= ~~ =========================


# ================================================= ~~ =================================================
#                                                FORMULÁRIO
# ================================================= ~~ =================================================

crmLogin.mainloop() # Sempre deixará existente