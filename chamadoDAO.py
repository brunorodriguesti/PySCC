import sqlite3


class ChamadoDAO:
    def __init__(self):
        self.conexao = sqlite3.connect("SCC.db")
        cursor = self.conexao.cursor()
        try:
            comando = "CREATE TABLE IF NOT EXISTS TB_CHAMADO (CODIGO INTEGER, DESCRICAO TEXT, ABERTO_POR TEXT, DATA_ABERTURA DATE, DATA_FECHAMENTO DATE, QTD_ABERT INTEGER, STATUS TEXT, PRIMARY KEY(CODIGO));"
            cursor.execute(comando)
            print("Banco de dados criado com sucesso")
        except sqlite3.DatabaseError as err:
            print("Erro ao criar o banco de dados")
        finally:
            if self.conexao:
                cursor.close()
                self.conexao.close()

    def abrirConexao(self):
        try:
            self.conexao = sqlite3.connect("SCC.db")
            self.cursor = self.conexao.cursor()

            return True
        except sqlite3.DatabaseError as error:
            print("Erro na conexao:", error)
            return False

    def fecharConexao(self):
        if self.conexao:
            self.cursor.close()
            self.conexao.close()

    def buscar(self):
        if self.abrirConexao():
            self.cursor.execute(
                "select codigo, descricao, julianday(date()) - julianday(DATA_ABERTURA) AS qtdDias, status, DATA_ABERTURA, aberto_por from tb_chamado"
            )
            resultado = self.cursor.fetchall()
            self.fecharConexao()
            return resultado
        else:
            return None

    def buscarPorFechados(self):
        if self.abrirConexao():
            self.cursor.execute(
                "select codigo, descricao, julianday(date()) - julianday(DATA_ABERTURA) AS qtdDias, status, DATA_ABERTURA, aberto_por, data_fechamento from tb_chamado where status = 'FECHADO'"
            )
            resultado = self.cursor.fetchall()
            self.fecharConexao()
            return resultado
        else:
            return None

    def buscarFechados(self):
        if self.abrirConexao():
            self.cursor.execute(
                "select codigo, descricao, julianday(date()) - julianday(DATA_ABERTURA) AS qtdDias, status, DATA_ABERTURA, aberto_por from tb_chamado where status = 'FECHADO'"
            )
            resultado = self.cursor.fetchall()
            self.fecharConexao()
            return resultado
        else:
            return None

    def buscarPorAbertos(self):
        if self.abrirConexao():
            self.cursor.execute(
                "select codigo, descricao, julianday(date()) - julianday(DATA_ABERTURA) AS qtdDias, status, DATA_ABERTURA, aberto_por from tb_chamado where status = 'ABERTO'"
            )
            resultado = self.cursor.fetchall()
            self.fecharConexao()
            return resultado
        else:
            return None

    def buscarAbertos(self):
        if self.abrirConexao():
            self.cursor.execute(
                "select codigo, descricao, julianday(date()) - julianday(DATA_ABERTURA) AS qtdDias, status, DATA_ABERTURA, aberto_por from tb_chamado where status = 'ABERTO'"
            )
            resultado = self.cursor.fetchall()
            self.fecharConexao()
            return resultado
        else:
            return None

    def buscarPorCodigo(self, codigo):
        if self.abrirConexao():
            self.cursor.execute("select * from tb_chamado where codigo = ?", (codigo,))
            resultado = self.cursor.fetchone()
            self.fecharConexao()
            return resultado
        else:
            return None

    def inserir(self, codigo, descricao, pessoa, dataAbertura):
        if self.abrirConexao():
            try:
                self.cursor.execute(
                    "insert into tb_chamado (codigo, descricao, aberto_por, data_abertura, status) values (?,?,?,?,?)",
                    (codigo, descricao, pessoa, dataAbertura, "ABERTO"),
                )
                self.conexao.commit()
                self.fecharConexao()
            except sqlite3.DatabaseError as erro:
                print(erro)

    def excluir(self, codigo):
        if self.abrirConexao():
            try:
                self.cursor.execute(
                    "delete from tb_chamado where codigo = ?", (codigo,)
                )
                self.conexao.commit()
                self.fecharConexao()
            except sqlite3.DatabaseError as erro:
                print(erro)

    def fechar(self, codigo, dataFechamento):
        if self.abrirConexao():
            try:
                self.cursor.execute(
                    "update tb_chamado set status = 'FECHADO', DATA_FECHAMENTO = ? where codigo = ?",
                    (
                        dataFechamento,
                        codigo,
                    ),
                )
                self.conexao.commit()
                self.fecharConexao()
            except sqlite3.DatabaseError as erro:
                print(erro)
