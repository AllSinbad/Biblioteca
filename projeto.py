id_livro = 1
num_mebro = 1

class Livro:
    def __init__(self, titulo:str, autor:str, id:int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.disponivel = True

class Membro:
    def __init__(self, nome:str, numero_membro: int) -> None:
        self.nome = nome
        self.numero = numero_membro
        self.historico = []

class Biblioteca:
    def __init__(self) -> None:
        self.catalogo_livros = []
        self.registro_membros = []

    def adicionar_livro(self):
        global id_livro
        titulo_livro = str(input("Escreva o título do livro: "))
        autor_livro = str(input("Escreva o nome do autor livro: "))
        livro = Livro(titulo=titulo_livro, autor=autor_livro, id=id_livro)
        self.catalogo_livros.append(livro)
        id_livro +=1
        return "Livro adicionado com sucesso"

    def adicionar_membro(self):
        global num_mebro
        nome_membro = str(input("Escreva o seu nome: "))
        membro = Membro(nome=nome_membro, numero_membro=num_mebro)
        self.registro_membros.append(membro)
        num_mebro +=1
        return "Membro adicionado com sucesso"


    def emprestar_livro(self):
        membro_existe = False
        livro_existe = False
        ver_membro = str(input("Digite seu nome ou seu numero de membro: "))
        for buscar_membro in self.registro_membros:
            if buscar_membro.nome == ver_membro or str(buscar_membro.numero) == ver_membro:
                membro_existe = True
                emprest_livro = str(input("Digite o nome ou o ID do livro: "))
                for buscar_livros in self.catalogo_livros:
                    if buscar_livros.titulo == emprest_livro or str(buscar_livros.id) == emprest_livro:
                        livro_existe = True
                        if buscar_livros.disponivel == True:
                            print("Livro alugado com sucesso")
                            buscar_livros.disponivel == False
                            print("Livro não disponível")
                            buscar_membro.historico.append(buscar_livros)
        if membro_existe == False:
            print("Membro não encontrado")
        if livro_existe == False:
            print("Livro não encontrado")
       
    
    def devolver_livro(self):
        livro_existe = False
        emprest_livro = str(input("Digite o nome ou o ID do livro: "))
        for buscar_livros in self.catalogo_livros:
            if buscar_livros.titulo == emprest_livro or str(buscar_livros.id) == emprest_livro:
                livro_existe = True
                if buscar_livros.disponivel == False:
                    print("Livro devolvido com sucesso")
                    buscar_livros.disponivel == True

        if livro_existe == False:
            print("Livro não encontrado")

    def pesquisar_livro(self):
        livro_existe = False

        pesq_livro = str(input("Digite o nome, o autor, ou o ID do livro:"))
        for livro_atual in self.catalogo_livros:
            if livro_atual.titulo == pesq_livro or livro_atual.autor == pesq_livro or str(livro_atual.id) == pesq_livro:
                livro_existe = True
                print(f"""
                Informações do Livro:
                ID do livro: {livro_atual.id}
                Titulo do livro: {livro_atual.titulo}
                Autor do livro: {livro_atual.autor}
                Status: {livro_atual.disponivel}
                """)
        if livro_existe == False:
            print("Livro não encontrado")



biblioteca1 = Biblioteca()

while True:
    menu = int(input("""
    Escolha uma opção
    1 - Adicionar Livro
    2 - Adicionar Membro
    3 - Emprestar Livro
    4 - Devolver Livro
    5 - Pesquisar Livro
    0 - Sair
    """))
    match menu:
        case 1:
            biblioteca1.adicionar_livro()
        case 2:
            biblioteca1.adicionar_membro()
        case 3:
            biblioteca1.emprestar_livro()
        case 4:
            biblioteca1.devolver_livro()
        case 5:
            biblioteca1.pesquisar_livro()
        case 0:
            print("Valeu meu fi, volte mais nao")
            break
        case _:
            print("Opção inválida")
