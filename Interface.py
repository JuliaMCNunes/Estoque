from cgi import test
from cgitb import text
from itertools import count
from re import I, L
import tkinter
from tkinter import *
from random import *
from tkinter import ttk
import time
import os
import tkinter.messagebox
from Class_Estoque import *
from Class_Gerenciar_Estoque import * 
#import posiciona


def fabricante():
    f1.forget()    
    f2.pack()
    
def produto():
    f1.forget()
    f3.pack()

def procurar():
    f1.forget()
    f4.pack()

def alterar():
    f1.forget()
    f5.pack()

def deletar():
    f1.forget()
    f6.pack()

def abastecer():
    f1.forget()
    f7.pack()

def retirar():
    f1.forget()
    f8.pack()


meu_estoque = Tk()
meu_estoque.title('Gestão de Estoque')
meu_estoque.geometry('1000x700+200+200')
meu_estoque.resizable(width=False, height=False)

#meu_estoque.bind('<Button-1>', posiciona.inicio_place)
#meu_estoque.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, meu_estoque))
#meu_estoque.bind('<Button-2>', lambda arg: posiciona.para_geometry(meu_estoque))

f1 = Frame(meu_estoque)
f1.pack()
f2 = Frame(meu_estoque)
f3 = Frame(meu_estoque)
f4 = Frame(meu_estoque)
f5 = Frame(meu_estoque)
f6 = Frame(meu_estoque)
f7 = Frame(meu_estoque)
f8 = Frame(meu_estoque)





