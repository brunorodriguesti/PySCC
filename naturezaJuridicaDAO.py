import sqlite3

class NaturezaJuridicaDAO:
    def abrirConexao(self):
        try:
            self.conexao = sqlite3.connect("trabalho.db")
            self.cursor = self.conexao.cursor()

            return True
        except sqlite3.DatabaseError as error:
            print("Erro na conexao:", error)
            return False
        
    def fecharConexao(self):
        if(self.conexao):
            self.cursor.close()
            self.conexao.close()

    def buscar(self):
        if(self.abrirConexao()):
            self.cursor.execute("select * from natureza_juridica")
            resultado = self.cursor.fetchall()
            self.fecharConexao() 
            return resultado
        else:
            return None
        
    def buscarPorCodigo(self, codigo):
        if(self.abrirConexao()):
            self.cursor.execute("select * from natureza_juridica where codigo = ?",(codigo,))
            resultado = self.cursor.fetchone()
            self.fecharConexao() 
            return resultado
        else:
            return None
        
    def inserir(self, codigo, descricao):
         if(self.abrirConexao()):
            try:
                self.cursor.execute("insert into natureza_juridica (codigo, descricao) values (?,?)",(codigo,descricao))            
                self.conexao.commit()
                self.fecharConexao()
            except sqlite3.DatabaseError as erro:
                print(erro) 
        
    def excluir(self, codigo):
         if(self.abrirConexao()):
            try:
                self.cursor.execute("delete from natureza_juridica where codigo = ?",(codigo,))            
                self.conexao.commit()
                self.fecharConexao()
            except sqlite3.DatabaseError as erro:
                print(erro) 
        
