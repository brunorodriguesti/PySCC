from naturezaJuridicaDAO import *
from telaNaturezaJuridica import *
import tkinter as tk

if __name__ == '__main__':

    janela = tk.Tk()
    naturezaDAO = NaturezaJuridicaDAO()
    telaNatureza = TelaNaturezaJuridica(janela, naturezaDAO) 
    janela.title('Sistema ')
    janela['bg'] = "blue"
    
    janela.mainloop()

    # naturezaDAO = NaturezaJuridicaDAO()

    # resultado = naturezaDAO.buscar()
    # print(resultado)
    # resultado = naturezaDAO.buscarPorCodigo(10000)
    # # print(resultado)
    # naturezaDAO.inserir(1, 'Nova Natureza')
    # naturezaDAO.inserir(2, 'Nova Natureza 2')
    # naturezaDAO.inserir(3, 'Nova Natureza 3')



    