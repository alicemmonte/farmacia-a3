class FarmaciaTotem:
    def __init__(self):
        self.usuarios = {}
        self.medicamentos = {
            "Paracetamol": {
                "preco": 10.0,
                "requer_receita": False,
                "estoque": 100,
                "sintomas": ["febre", "dor"],
            },
            "Nebacetin": {
                "preco": 15.0,
                "requer_receita": False,
                "estoque": 50,
                "sintomas": ["cortes", "ferimentos", "queimaduras"],
                "contraindicacoes": ["Alergia a neomicina", "insuficiência renal"]
            },
            "Kuratop": {
                "preco": 20.0,
                "requer_receita": False,
                "estoque": 50,
                "sintomas": ["cortes", "ferimentos", "queimaduras"],
                "contraindicacoes": ["hipersensibilidade a qualquer um dos componentes da fórmula"]
            },
            "Cicatrimed": {
                "preco": 25.0,
                "requer_receita": False,
                "estoque": 50,
                "sintomas": ["cortes", "ferimentos", "queimaduras"],
                "contraindicacoes": ["alergia aos componentes"]
            },
            "meclizina": {
                "preco": 30.0,
                "requer_receita": True,
                "estoque": 50,
                "sintomas": ["enjoo"],
                "contraindicacoes": ["alergia aos componentes", "idosos com quadro delirium"]
            },
            "Dimenidrinato": {
                "preco": 35.0,
                "requer_receita": True,
                "estoque": 50,
                "sintomas": ["enjoo"],
                "contraindicacoes": ["contraindicado para pacientes porfíricos", "menores de 6 anos"]
            },
            "Dramin": {
                "preco": 40.0,
                "requer_receita": True,
                "estoque": 50,
                "sintomas": ["enjoo"],
                "contraindicacoes": ["alergia ao dimenidrinato", "Pacientes com porfiria"]
            },

        }

    def cadastrar_usuario(self, nome_usuario, senha, contraindicacoes):
        self.usuarios[nome_usuario] = {"senha": senha, "contraindicacoes": contraindicacoes}

    def buscar_medicamento(self, nome_medicamento):
        if nome_medicamento in self.medicamentos:
            return self.medicamentos[nome_medicamento]
        else:
            return None

    def sugerir_alternativas(self, sintomas, contraindicacoes):
        alternativas = []
        for nome, info in self.medicamentos.items():
            if all(sintoma in info["sintomas"] for sintoma in sintomas) and not any(contraindicacao in info["contraindicacoes"] for contraindicacao in contraindicacoes):
                alternativas.append(nome)
        return alternativas

    def fazer_pedido(self, nome_usuario, nome_medicamento):
        if nome_usuario not in self.usuarios:
            senha = input("Usuário não cadastrado. Por favor, crie uma senha: ")
            contraindicacoes = input("Por favor, informe suas contraindicações (separe por vírgulas): ").split(", ")
            self.cadastrar_usuario(nome_usuario, senha, contraindicacoes)
            print("Usuário cadastrado com sucesso!")
        medicamento = self.buscar_medicamento(nome_medicamento)
        if not medicamento:
            alternativas = self.sugerir_alternativas(["febre", "dor"], self.usuarios[nome_usuario]["contraindicacoes"])
            return f"Medicamento não encontrado. Alternativas: {', '.join(alternativas)}"
        if medicamento["requer_receita"]:
            return "Este medicamento requer receita médica."
        if medicamento["estoque"] == 0:
            return "Medicamento fora de estoque."
        medicamento["estoque"] -= 1
        return f"Pedido realizado com sucesso! Retire na seção {nome_medicamento}."

if __name__ == "__main__":
    farmacia = FarmaciaTotem()

    print("Bem-vindo ao Totem de Autoatendimento da Farmácia!")
    nome_usuario = input("Digite seu nome de usuário: ")
    nome_medicamento = input("Digite o nome do medicamento desejado: ")
    resultado_pedido = farmacia.fazer_pedido(nome_usuario, nome_medicamento)
    print(resultado_pedido)
