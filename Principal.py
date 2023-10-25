from chamadoDAO import *
from telaChamado import *
import tkinter as tk

if __name__ == "__main__":
    janela = tk.Tk()
    chamadoDAO = ChamadoDAO()
    tela = TelaChamado(janela, chamadoDAO)
    janela.title("Sistema de Controle de Chamados ")
    janela["bg"] = "blue"

    janela.mainloop()
