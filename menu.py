from csv import excel
import datetime as dt
from typing import Container
import pandas as pd
from openpyxl import *
from msilib.schema import ComboBox

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

# ================================================= ~~ =================================================
#                                                FORMULÁRIO
# ================================================= ~~ =================================================

def menuPrincipal():
    # ========================= ~~ =========================
    #                    FORMULÁRIO (Menu)
    # ========================= ~~ =========================

    crmMenu = tk.Toplevel()
    crmMenu.geometry("520x420")
    crmMenu.title("Menu Principal")

    #Criando menu bar
    barraDeMenus = Menu(crmMenu)

    # Adicionando uma opção no menur bar e subopções
    menuCadastro = Menu(barraDeMenus, tearoff=0)
    barraDeMenus.add_cascade(label='Gerenciamento', menu=menuCadastro)

    menuCadastro.add_command(label = "Gerenciar Logins")
    menuCadastro.add_command(label = "Gerenciar Bancos")
    menuCadastro.add_command(label = "Gerenciar Promotoras")
    menuCadastro.add_command(label = "Gerenciar Usuários Certificados")
    menuCadastro.add_command(label = "Gerenciar Usuários e Senhas de Bancos")

    menuCadastro.add_separator()
    menuCadastro.add_cascade(label = "Sair")

    # Adicionando segunda opção de menu
    menuCadastro = Menu(barraDeMenus, tearoff=0)
    barraDeMenus.add_cascade(label='Sobre', menu=menuCadastro)

    menuCadastro.add_command(label = "Sobre o Sistema")

    crmMenu.config(menu = barraDeMenus)
    crmMenu.mainloop() # Sempre deixará existente

    # ========================= ~~ =========================
    #                    FORMULÁRIO (Menu)
    # ========================= ~~ =========================