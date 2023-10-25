import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
from tkcalendar import Calendar, DateEntry


class TelaChamado:
    def __init__(self, janela, dao):
        self.dao = dao

        self.quadro = tk.Frame(janela, pady=10)
        self.quadro.pack(fill=tk.BOTH, expand=tk.YES)

        self.lblCodigo = tk.Label(self.quadro, text="Código: ")
        self.lblCodigo.grid(row=0, column=0)
        self.etyCodigo = tk.Entry(self.quadro)
        self.etyCodigo.grid(row=0, column=1)

        self.lblDescricao = tk.Label(self.quadro, text="Descrição: ")
        self.lblDescricao.grid(row=1, column=0)
        self.etyDescricao = tk.Entry(self.quadro)
        self.etyDescricao.grid(row=1, column=1)

        self.lblPessoa = tk.Label(self.quadro, text="Aberto por: ")
        self.lblPessoa.grid(row=2, column=0)
        self.etyPessoa = tk.Entry(self.quadro)
        self.etyPessoa.grid(row=2, column=1)

        self.lblDataAbertura = tk.Label(self.quadro, text="Data da Abertura: ")
        self.lblDataAbertura.grid(row=3, column=0)
        self.etyDataAbertura = DateEntry(self.quadro)
        self.etyDataAbertura.grid(row=3, column=1)

        self.lblDataFechamento = tk.Label(self.quadro, text="Data Fechamento: ")
        self.lblDataFechamento.grid(row=4, column=0)
        self.etyDataFechamento = tk.Entry(self.quadro)
        self.etyDataFechamento.grid(row=4, column=1)

        self.btnInserir = tk.Button(self.quadro, text="Inserir")
        self.btnInserir.grid(row=5, column=0)
        self.btnInserir.bind("<Button-1>", self.inserirChamado)

        self.btnExcluir = tk.Button(self.quadro, text="Excluir")
        self.btnExcluir.grid(row=5, column=1)
        self.btnExcluir.bind("<Button-1>", self.excluirChamado)

        self.btnBuscar = tk.Button(self.quadro, text="Buscar")
        self.btnBuscar.grid(row=5, column=2)
        self.btnBuscar.bind("<Button-1>", self.buscarChamado)

        columns = ("codigo", "descricao", "diasAbertos", "status")
        self.tree = ttk.Treeview(janela, columns=columns, show="headings")

        # Cabeçalho
        self.tree.heading("codigo", text="Código")
        self.tree.heading("descricao", text="Descrição")
        self.tree.heading("diasAbertos", text="Dias Aberto")
        self.tree.heading("status", text="Status")

        # adicionando barra de rolagem
        self.scrollbar = ttk.Scrollbar(janela)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # vinculando o treeview ao scrollbar
        self.scrollbar.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.scrollbar.set)

        self.tree.pack(fill=tk.BOTH, expand=tk.YES)

        # evento de clique
        self.tree.bind("<Double-1>", self.selecionarLinha)

        #
        self.atualizarTabela(self.dao.buscar())

    def atualizarTabela(self, registros):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for registro in registros:
            self.tree.insert("", tk.END, values=registro)

    def selecionarLinha(self, event):
        item = self.tree.item(self.tree.selection())
        self.etyCodigo.delete(0, tk.END)
        self.etyCodigo.insert(0, item["values"][0])

        self.etyDescricao.delete(0, tk.END)
        self.etyDescricao.insert(0, item["values"][1])

        print("you clicked on", item["values"])

    def inserirChamado(self, event):
        if self.etyCodigo.get() != "" or self.etyDescricao.get() != "":
            self.dao.inserir(
                self.etyCodigo.get(),
                self.etyDescricao.get(),
                self.etyPessoa.get(),
                self.etyDataAbertura.get(),
            )
            self.atualizarTabela(self.dao.buscar())
        else:
            mb.showinfo("Informação", "É necessário informar código e nome")

    def excluirChamado(self, event):
        if self.etyCodigo.get() != "":
            self.dao.excluir(self.etyCodigo.get())
            self.atualizarTabela(self.dao.buscar())
        else:
            mb.showinfo("Informação", "É necessário informar código para excluir")

    def buscarChamado(self, event):
        if self.etyCodigo.get() != "":
            self.dao.buscarPorCodigo(self.etyCodigo.get())
            self.atualizarTabela(self.dao.buscar())
        else:
            mb.showinfo("Informação", "É necessário informar código para buscar")
