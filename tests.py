import unittest

class TestFarmaciaTotem(unittest.TestCase):

    def setUp(self):
        self.farmacia = FarmaciaTotem()
        self.farmacia.cadastrar_usuario("usuario_teste", "senha123", ["alergia ao dimenidrinato"])

    def test_buscar_medicamento_existente(self):
        medicamento = self.farmacia.buscar_medicamento("Paracetamol")
        self.assertIsNotNone(medicamento)
        self.assertEqual(medicamento["preco"], 10.0)
        self.assertEqual(medicamento["estoque"], 100)

    def test_buscar_medicamento_inexistente(self):
        medicamento = self.farmacia.buscar_medicamento("Aspirina")
        self.assertIsNone(medicamento)

    def test_sugerir_alternativas(self):
        alternativas = self.farmacia.sugerir_alternativas(["dor"], ["alergia ao dimenidrinato"])
        self.assertIn("Paracetamol", alternativas)
        self.assertNotIn("Dramin", alternativas)

    def test_fazer_pedido_medicamento_existente(self):
        resultado = self.farmacia.fazer_pedido("usuario_teste", "Paracetamol")
        self.assertEqual(resultado, "Obrigado por usar nossos serviços!")
        medicamento = self.farmacia.buscar_medicamento("Paracetamol")
        self.assertEqual(medicamento["estoque"], 99)

    def test_fazer_pedido_medicamento_inexistente(self):
        resultado = self.farmacia.fazer_pedido("usuario_teste", "Aspirina")
        self.assertIn("Medicamento não encontrado", resultado)

    def test_fazer_pedido_medicamento_requer_receita(self):
        resultado = self.farmacia.fazer_pedido("usuario_teste", "meclizina")
        self.assertEqual(resultado, "Este medicamento requer receita médica. Por favor, consulte um médico.")

    def test_fazer_pedido_medicamento_fora_de_estoque(self):
        resultado = self.farmacia.fazer_pedido("usuario_teste", "Nebacetin")
        self.assertEqual(resultado, "Medicamento fora de estoque.")

    def test_autenticar_usuario_existente(self):
        autenticado = self.farmacia.autenticar_usuario("usuario_teste", "senha123")
        self.assertTrue(autenticado)

    def test_autenticar_usuario_inexistente(self):
        autenticado = self.farmacia.autenticar_usuario("usuario_invalido", "senha123")
        self.assertFalse(autenticado)

if __name__ == '_main_':
    unittest.main()
