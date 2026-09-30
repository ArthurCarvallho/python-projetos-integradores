### 31\. Sistema bancário
import json
contas = []
class Conta:
    proximo_id = 1
    def __init__(self,  nome, saldo =0.0):
        self.id = Conta.proximo_id
        self.nome = nome 
        self.saldo = saldo
        Conta.proximo_id += 1
        
        
    def depositar(self, deposito):
            self.saldo += deposito
            return True 
        
    def sacar(self, saque):
            if saque <= self.saldo:
                self.saldo -= saque
                return True 
            
            else:
                return "Saldo insuficinte! "
            
    def consultar_saldo(self):
            return self.saldo  

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "saldo": self.saldo}
		
        
def criar_conta(contas, nome, saldo_inicial):
    try:
        nova_conta = Conta(nome, saldo_inicial)
        contas.append(nova_conta)
        print("Conta criada com Sucesso!")
    except Exception as Erro: 
                print(Erro)
     		
def listar_contas(contas):
    if not contas:
          print("Nenhuma conta cadastrada.")
          return 
    print("\n--- LISTA DE CONTAS ---")
    for conta in contas:
        print(f"ID: {conta.id} | Titular: {conta.nome} | Saldo: R$ {conta.saldo:.2f}")
    print("-----------------------\n")
	
def salvar_contas(contas):
    dados = [conta.to_dict() for conta in contas]
    with open('contas.json', 'w') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print("Dados salvos no arquivo 'contas.json' com sucesso!\n")

def carregar_contas(contas):
    try:
        with open('contas.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            contas.clear()
            maior_id = 0
            for d in dados:
               
                c = Conta(d['nome'], d['saldo'])
                c.id = d['id'] 
                contas.append(c)
                if d['id'] > maior_id:
                    maior_id = d['id']

            Conta.proximo_id = maior_id + 1        

        print("Dados carregados com sucesso!\n")
    except FileNotFoundError:
        print("Arquivo 'contas.json' não encontrado. Um novo será criado ao salvar.\n")


def buscar_conta(contas, id_conta):
    return next(
        (conta for conta in contas if conta.id == id_conta),
        None
    )

carregar_contas(contas)

while True:
    print("""
--- SISTEMA BANCÁRIO ---

1 - Criar conta
2 - Depositar
3 - Sacar
4 - Consultar saldo
5 - Listar contas
6 - Sair
""")

    try:
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            nome = input("Digite o nome do titular: ")
            saldo_inicial = float(
                input("Digite o saldo inicial da conta: ")
            )

            criar_conta(
                contas,
                nome,
                saldo_inicial
            )

        elif opcao == 2:
            if not contas:
                print("Nenhuma conta cadastrada.")
                continue

            id_conta = int(
                input("Digite o ID da conta: ")
            )

            conta_encontrada = buscar_conta(
                contas,
                id_conta
            )

            if conta_encontrada:
                deposito = float(
                    input("Digite o valor do depósito: ")
                )

                if conta_encontrada.depositar(deposito):
                    print(
                        f"Depósito de R$ {deposito:.2f} "
                        "realizado com sucesso."
                    )
                else:
                    print(
                        "O valor do depósito deve ser positivo."
                    )

            else:
                print("Conta não encontrada.")

        elif opcao == 3:
            if not contas:
                print("Nenhuma conta cadastrada.")
                continue

            id_conta = int(
                input("Digite o ID da conta: ")
            )

            conta_encontrada = buscar_conta(
                contas,
                id_conta
            )

            if conta_encontrada:
                saque = float(
                    input("Digite o valor do saque: ")
                )

                if conta_encontrada.sacar(saque):
                    print(
                        f"Saque de R$ {saque:.2f} "
                        "realizado com sucesso."
                    )
                else:
                    print(
                        "Saque não realizado. "
                        "Verifique o valor e o saldo disponível."
                    )

            else:
                print("Conta não encontrada.")

        elif opcao == 4:
            if not contas:
                print("Nenhuma conta cadastrada.")
                continue

            id_conta = int(
                input("Digite o ID da conta: ")
            )

            conta_encontrada = buscar_conta(
                contas,
                id_conta
            )

            if conta_encontrada:
                saldo = conta_encontrada.consultar_saldo()

                print(
                    f"Saldo de {conta_encontrada.nome}: "
                    f"R$ {saldo:.2f}"
                )

            else:
                print("Conta não encontrada.")

        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6:
            salvar_contas(contas)
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.")

    except ValueError:
        print("Digite um valor válido.")