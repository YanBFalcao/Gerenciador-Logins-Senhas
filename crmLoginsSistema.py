from csv import excel
import datetime as dt
from tkinter.tix import COLUMN
from typing import Container
from numpy import column_stack
import pandas as pd
from openpyxl import *
from msilib.schema import ComboBox

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

import menu as mn

# ================================================= ~~ =================================================
#                                                FORMULÁRIO
# ================================================= ~~ =================================================



def retornoMenu():
    mn.menuPrincipal()
    encerrarFormulario()

def encerrarFormulario():
    #crmLoginsSistema.destroy()
    print("encontrar maneira de encerrar formulário e manter no menu principal")

def salvarLogin():
    # Aqui, criar lógica para salvar dado no banco de dados
    messagebox.showinfo("Sucesso!", "A chamada do Botão de Salvar login deu Certo!")

def menuLoginsUsuarios():
    # ========================= ~~ =========================
    #                    FORMULÁRIO (Menu)
    # ========================= ~~ =========================

    crmLoginsSistema = tk.Tk()
    #crmLoginsSistema = tk.Toplevel()
    crmLoginsSistema.geometry("320x220")
    crmLoginsSistema.title("Gerenciar Logins de Sistema")

    # Label na janela
    label_crmCriar_Login = tk.Label(text = "Insira o novo nome de Login")
    label_crmCriar_Login.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)
    #padx => É o distanciamento/margem do eixo x

    entry_crmInserir_Login = tk.Entry()
    entry_crmInserir_Login.grid(row = 1, column = 3, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)

    label_crmCriar_Senha = tk.Label(text = "Insira uma nova senha")
    label_crmCriar_Senha.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)

    entry_crmInserir_Senha = tk.Entry()
    entry_crmInserir_Senha.grid(row = 2, column = 3, padx = 10, pady = 10, sticky = 'nswe', columnspan = 2)

    botao_crmCriar_Login = tk.Button(crmLoginsSistema, text="Salvar Login", command=salvarLogin)
    botao_crmCriar_Login.grid(row=5, column=1, padx = 10, pady = 10, sticky = 'nswe', columnspan = 4)

    botao_crmRetornar_Menu = tk.Button(crmLoginsSistema, text="Retornar ao Menu", command=retornoMenu)
    botao_crmRetornar_Menu.grid(row=6, column=1, padx = 10, pady = 10, sticky = 'nswe', columnspan = 4)

    botao_sair = tk.Button(crmLoginsSistema, text="Sair", command=crmLoginsSistema.destroy)
    botao_sair.grid(row=7, column=1, padx = 10, pady = 10, sticky = 'nswe', columnspan = 4)

    crmLoginsSistema.mainloop() # Sempre deixará existente

    # ========================= ~~ =========================
    #                    FORMULÁRIO (Menu)
    # ========================= ~~ =========================

menuLoginsUsuarios()