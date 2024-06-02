class Farmacia:
    def __init__(self):
        self.usuarios = {"usuario1": "senha123"}
        self.medicamentos = {
            "Kuratop": {"estoque": 50, "preco": 20.00, "requer_receita": False, "sintomas": ["cortes", "ferimentos", "queimaduras"],
                        "contraindicacoes": ["hipersensibilidade a qualquer um dos componentes da fórmula"]},
            "Paracetamol": {"estoque": 15, "preco": 10.00, "requer_receita": False, "sintomas": ["febre", "dor"],
                            "contraindicacoes": ["Gravidez", "amamentação"]},
            "Nebacetin": {"estoque": 0, "preco": 15.00, "requer_receita": False, "sintomas": ["cortes", "ferimentos", "queimaduras"],
                          "contraindicacoes": ["Alergia a neomicina", "insuficiência renal"]},
            "Cicatrimed": {"estoque": 50, "preco": 25.00, "requer_receita": False, "sintomas": ["cortes", "ferimentos", "queimaduras"],
                           "contraindicacoes": ["alergia aos componentes"]},
            "meclizina": {"estoque": 50, "preco": 30.00, "requer_receita": True, "sintomas": ["enjoo"],
                          "contraindicacoes": ["alergia aos componentes", "idosos com quadro delirium"]},
            "Dimenidrinato": {"estoque": 50, "preco": 35.00, "requer_receita": True, "sintomas": ["enjoo"],
                              "contraindicacoes": ["contraindicado para pacientes porfíricos", "menores de 6 anos"]},
            "Dramin": {"estoque": 50, "preco": 40.0, "requer_receita": True, "sintomas": ["enjoo"],
                       "contraindicacoes": ["alergia ao dimenidrinato", "Pacientes com porfiria"]},
        }

    def adicionar_usuario(self, usuario, senha):
        if usuario in self.usuarios:
            return "Usuário já existe."
        self.usuarios[usuario] = senha
        return "Usuário adicionado com sucesso."

    def autenticar_usuario(self, usuario, senha):
        return usuario in self.usuarios and self.usuarios[usuario] == senha

    def buscar_medicamento(self, nome):
        return self.medicamentos.get(nome, None)

    def realizar_compra(self, nome, quantidade):
        medicamento = self.buscar_medicamento(nome)
        if not medicamento:
            return "Medicamento não encontrado."
        
        if medicamento["requer_receita"]:
            return "Este medicamento requer receita médica."

        if not isinstance(quantidade, int) or quantidade <= 0:
            return "Quantidade inválida. Deve ser um número inteiro positivo."

        if quantidade > medicamento["estoque"]:
            return "Quantidade solicitada excede o estoque disponível."
        
        valor_total = quantidade * medicamento["preco"]
        medicamento["estoque"] -= quantidade
        return f"Compra realizada com sucesso! Total a pagar: R${valor_total:.2f}"

# Funções para a Interface do Usuário

def mostrar_menu():
    print("\n== Totem de Autoatendimento da Farmácia ==")
    print("1. Adicionar Novo Usuário")
    print("2. Buscar Medicamento")
    print("3. Realizar Compra")
    print("4. Finalizar Compra")

def buscar_medicamento_interface(farmacia):
    nome_medicamento = input("Digite o nome do medicamento: ")
    medicamento = farmacia.buscar_medicamento(nome_medicamento)
    if medicamento:
        print(f"\nMedicamento: {nome_medicamento}")
        print(f"Estoque: {medicamento['estoque']}")
        print(f"Preço: R${medicamento['preco']:.2f}")
        print(f"Sintomas: {', '.join(medicamento['sintomas'])}")
        print(f"Contraindicações: {', '.join(medicamento['contraindicacoes'])}")
        print(f"Requer receita: {'Sim' if medicamento['requer_receita'] else 'Não'}")
    else:
        print("Medicamento não encontrado.")

def realizar_compra_interface(farmacia):
    nome_medicamento = input("Digite o nome do medicamento: ")
    try:
        quantidade = int(input("Digite a quantidade desejada: "))
    except ValueError:
        print("Quantidade inválida. Deve ser um número inteiro.")
        return
    resultado = farmacia.realizar_compra(nome_medicamento, quantidade)
    print(resultado)

def adicionar_usuario_interface(farmacia):
    usuario = input("Digite o nome do novo usuário: ")
    senha = input("Digite a senha do novo usuário: ")
    resultado = farmacia.adicionar_usuario(usuario, senha)
    print(resultado)

# Exemplo de uso
farmacia = Farmacia()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_usuario_interface(farmacia)
    elif opcao == "2":
       buscar_medicamento_interface(farmacia)
    elif opcao == "3":
        realizar_compra_interface(farmacia)
    elif opcao == "4":
        print("Obrigado por utilizar o totem de autoatendimento da Farmácia. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
