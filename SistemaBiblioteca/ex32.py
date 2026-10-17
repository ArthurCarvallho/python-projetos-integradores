import json
class Livro:
   
    maior_id = 0
    def __init__(self, titulo, autor, ano, disponivel=True, id = None):
        if id is not None:
            self.id = id
            if id > Livro.maior_id:
                Livro.maior_id = id
        else:
            self.id = Livro.maior_id + 1
            Livro.maior_id += 1
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel
     


class Usuario:
    maior_id = 0
    def __init__(self, nome, idade, id=None):
        if id is not None:
            self.id = id
            if id > Usuario.maior_id:
                Usuario.maior_id = id
        else:
            self.id = Usuario.maior_id + 1
            Usuario.maior_id += 1
              
        self.nome = nome
        self.idade = idade


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = [] 

    def cadastrar_usuario(self,nome,idade):
        try:
            novo_usuario = Usuario(nome, idade)
            self.usuarios.append(novo_usuario)
            print(f"Usuário '{nome}' cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar usuário: {e}" )

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        print("\n--- LISTA DE USUÁRIOS ---")
        for usuario in self.usuarios:
            print(f"ID: {usuario.id} | Nome: {usuario.nome} | Idade: {usuario.idade}")
        print("-----------------------\n")

    def cadastrar_livro(self, titulo, autor, ano, disponivel=True):
        try:
            novo_livro = Livro(titulo, autor, ano, disponivel)
            self.livros.append(novo_livro)
            print(f"Livro '{titulo}' cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar livro: {e}")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        print("\n--- LISTA DE LIVROS ---")
        for livro in self.livros:
            disponibilidade = "Disponível" if livro.disponivel else "Indisponível"
            print(f"ID: {livro.id} | Título: {livro.titulo} | Autor: {livro.autor} | Ano: {livro.ano} | Status: {disponibilidade}")
        print("-----------------------\n")

    def pesquisar_livro(self, titulo_buscado):
        for livro in self.livros:
            if livro.titulo.strip().lower() == titulo_buscado.strip().lower():
                print(f"Livro encontrado: ID: {livro.id} | Título: {livro.titulo} | Autor: {livro.autor} | Ano: {livro.ano} | Status: {'Disponível' if livro.disponivel else 'Indisponível'}")
                return ""            
        return "Não Encontrado"  
		
    def emprestar_livro(self, livro_id, usuario_id):
        for livro in self.livros:
            if livro.id == livro_id:
                for usuario in self.usuarios:
                    if usuario.id == usuario_id:                     
                            if livro.disponivel:
                                livro.disponivel = False
                                print(f"Livro '{livro.titulo}' emprestado para {usuario.nome}.")
                                novo_emprestimo = {livro.id: usuario.id}
                                self.emprestimos.append(novo_emprestimo)
                                return
                            else:
                                print(f"Livro '{livro.titulo}' não está disponível para empréstimo.")
                                return
                else:
                    print(f"Usuário '{usuario_id}' não encontrado na biblioteca.")
                    return
        else:
            print(f"Livro '{livro_id}' não encontrado na biblioteca.")
            return
        
    def devolver_livro(self, livro_id, usuario_id):
        for livro in self.livros:
            if livro.id == livro_id:
                for usuario in self.usuarios:
                    if usuario.id == usuario_id:
                        if not livro.disponivel:
                            if {livro.id: usuario.id} in self.emprestimos:
                                livro.disponivel = True
                                print(f"Livro '{livro.titulo}' devolvido por {usuario.nome}.")
                                self.emprestimos.remove({livro.id: usuario.id})
                                return
                            else: 
                                print(f"Erro: O livro '{livro_id}' não foi emprestado para {usuario.id}.")
                                return
                        else:
                            print(f"Livro '{livro.titulo}' não está emprestado.")
                            return
                else:
                    print(f"Usuário '{usuario_id}' não encontrado na biblioteca.")
                    return
        else:
            print(f"Livro '{livro_id}' não encontrado na biblioteca.")
            return

    def salvar_dados(self):
        livros = []
        usuarios = []
        emprestimos = []
        for livro in self.livros:
            livros.append({
                "id": livro.id,
                "titulo": livro.titulo,
                "autor": livro.autor,
                "ano": livro.ano,
                "disponivel": livro.disponivel
            })
        for usuario in self.usuarios:
            usuarios.append({
                "id": usuario.id,
                "nome": usuario.nome,
                "idade": usuario.idade
            })
        for emprestimo in self.emprestimos:
            emprestimos.append(emprestimo)
        with open("biblioteca.json", "w") as arquivo:
            json.dump({
                "livros": livros,
                "usuarios": usuarios,
                "emprestimos": emprestimos
            }, arquivo, indent=4)

    def carregar_dados(self):
        try:
            with open("biblioteca.json", "r") as arquivo:
                dados = json.load(arquivo)
                for livro in dados.get("livros", []):
                    self.livros.append(Livro(livro["titulo"], livro["autor"], livro["ano"], livro["disponivel"], livro["id"]))
                for usuario in dados.get("usuarios", []):
                    self.usuarios.append(Usuario(usuario["nome"], usuario["idade"], usuario["id"]))
                for emprestimo in dados.get("emprestimos", []):
                   self.emprestimos.append({int(list(emprestimo.keys())[0]): list(emprestimo.values())[0]})

        except FileNotFoundError:
            print("Arquivo de dados não encontrado. Iniciando com biblioteca vazia.")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

carregar_dados = True
if carregar_dados:
    biblioteca = Biblioteca()
    biblioteca.carregar_dados()

 
                
# --- TESTE DE EXECUÇÃO ---

# 1. Instância única da biblioteca
while True:
    
    print("\n--- MENU DA BIBLIOTECA ---")
    print("1. Cadastrar Usuário")
    print("2. Listar Usuários")
    print("3. Cadastrar Livro")
    print("4. Listar Livros")
    print("5. Pesquisar Livro")
    print("6. Emprestar Livro")
    print("7. Devolver Livro")
    print("8. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        biblioteca.cadastrar_usuario(nome, idade)
        
    elif opcao == "2":
        biblioteca.listar_usuarios()
        
    elif opcao == "3":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano de publicação do livro: "))
        biblioteca.cadastrar_livro(titulo, autor, ano)
        
    elif opcao == "4":
        biblioteca.listar_livros()
        
    elif opcao == "5":
        titulo_buscado = input("Digite o título do livro a ser pesquisado: ")
        resultado = biblioteca.pesquisar_livro(titulo_buscado)
        if resultado:
            print(resultado)
        
    elif opcao == "6":
        biblioteca.listar_livros()
        livro_id = int(input("Digite o ID do livro a ser emprestado: "))
        biblioteca.listar_usuarios()
        usuario_id = int(input("Digite o ID do usuário que deseja emprestar o livro: "))
        biblioteca.emprestar_livro(livro_id, usuario_id)
        
    elif opcao == "7":
        livro_id = int(input("Digite o ID do livro a ser devolvido: "))
        usuario_id = int(input("Digite o ID do usuário que deseja devolver o livro: "))
        biblioteca.devolver_livro(livro_id, usuario_id)
        
    elif opcao == "8":
        print("Saindo da biblioteca...")
        biblioteca.salvar_dados()
        break
        
    else:
        print("Opção inválida! Tente novamente.")