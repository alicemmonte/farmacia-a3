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

    def autenticar_usuario(self, usuario, senha):
        return usuario in self.usuarios and self.usuarios[usuario] == senha

    def buscar_medicamento(self, nome):
        return self.medicamentos.get(nome, None)

    def realizar_compra(self, nome, quantidade):
        medicamento = self.buscar_medicamento(nome)
        if medicamento:
            if quantidade > 0 and quantidade <= medicamento["estoque"]:
                valor_total = quantidade * medicamento["preco"]
                medicamento["estoque"] -= quantidade
                return f"Compra realizada com sucesso! Total a pagar: R${valor_total:.2f}"
            else:
                return "Quantidade solicitada excede o estoque disponível."
        else:
            return "Medicamento não encontrado."

# Exemplo de uso
farmacia = Farmacia()

while True:
    print("\n== Totem de Autoatendimento da Farmácia ==")
    print("1. Buscar Medicamento")
    print("2. Realizar Compra")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
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

    elif opcao == "2":
        nome_medicamento = input("Digite o nome do medicamento: ")
        quantidade = int(input("Digite a quantidade desejada: "))
        resultado = farmacia.realizar_compra(nome_medicamento, quantidade)
        print(resultado)

    elif opcao == "3":
        print("Obrigado por utilizar o totem de autoatendimento da Farmácia. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
