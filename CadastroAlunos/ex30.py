### 30\. Sistema de cadastro de alunos
import json
alunos = []

def cadastrar_aluno(alunos,nome, idade, notas):
    novo_aluno  = {"nome": nome, "idade": idade, "notas" : [notas]}
    alunos.append(novo_aluno)
    
def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Notas: {aluno['notas']}")
    print()
        
def pesquisar_aluno(alunos,nome):
    
    if nome.strip().lower() in [aluno["nome"].strip().lower() for aluno in alunos]:
        return True
    return False
        
        
def remover_aluno(alunos, nome):
    for aluno in alunos:
        if aluno["nome"].strip().lower() == nome.strip().lower():
            alunos.remove(aluno) 
            return True 
    return False
    

def salvar_alunos(alunos):
    with open('alunos.json', 'w', encoding='utf-8') as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)
    print('Alunos salvos com sucesso!\n')
        
                   
            
def carregar_alunos(alunos):
    try:
        with open('alunos.json', 'r', encoding='utf-8') as arquivo:
            lista_carregada = json.load(arquivo)
            alunos.clear() 
            alunos.extend(lista_carregada) 
        print('Alunos carregados com sucesso!\n')
    except FileNotFoundError:
        print('Arquivo de alunos ainda não existe. Salve primeiro.\n')
        

print("=="*10 + " Cadastro de Alunos "+"=="*10)            

while True:
    print("Painel de controle do sistema de cadastro de alunos\n" \
    "1 - Cadastrar aluno\n" \
    "2 - Listar alunos\n" \
    "3 - Pesquisar aluno\n" \
    "4 - Remover aluno\n" \
    "5 - Salvar alunos\n" \
    "6 - Carregar alunos\n" \
    "0 - Sair\n" \
    )

    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        notas = float(input("Digite a nota do aluno: "))
        cadastrar_aluno(alunos, nome, idade, notas)

    elif opcao == 2:
        listar_alunos(alunos)
    elif opcao == 3:
        nome = input("Digite o nome do aluno a ser pesquisado: ")
        if pesquisar_aluno(alunos, nome):
            print(f"Aluno {nome} encontrado!")
        else:
            print(f"Aluno {nome} não encontrado.")
    elif opcao == 4:
        nome = input("Digite o nome do aluno a ser removido: ")
        if remover_aluno(alunos, nome):
            print(f"Aluno {nome} removido com sucesso!")
        else:
            print(f"Aluno {nome} não encontrado.")
    elif opcao == 5:
        salvar_alunos(alunos)
    elif opcao == 6:
        carregar_alunos(alunos)
    elif opcao == 0:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

    