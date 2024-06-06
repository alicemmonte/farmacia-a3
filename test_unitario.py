import unittest

class TestFarmacia(unittest.TestCase):
    def setUp(self):
        self.farmacia = Farmacia()

    def test_autenticar_usuario(self):
        self.assertTrue(self.farmacia.autenticar_usuario("usuario1", "senha123"))
        self.assertFalse(self.farmacia.autenticar_usuario("usuario1", "senha_errada"))

    def test_buscar_medicamento(self):
        medicamento = self.farmacia.buscar_medicamento("Paracetamol")
        self.assertIsNotNone(medicamento)
        self.assertIsNone(self.farmacia.buscar_medicamento("medicamento_inexistente"))

    def test_realizar_compra(self):
        self.assertEqual(self.farmacia.realizar_compra("Paracetamol", 5), "Este medicamento requer receita.")
        self.assertEqual(self.farmacia.realizar_compra("Paracetamol", 20), "Quantidade solicitada excede o estoque disponível.")
        self.assertEqual(self.farmacia.realizar_compra("medicamento_inexistente", 1), "Medicamento não encontrado.")

if __name__ == '__main__':
    unittest.main()
