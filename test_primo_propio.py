# Definimos una clase de pruebas que hereda de unittest.TestCase.
class TestNumerosPrimos(unittest.TestCase):

    # Prueba para la función es_primo.
    def test_es_primo(self):
        self.assertTrue(es_primo(2))  # Verificamos que 2 es primo.
        self.assertTrue(es_primo(3))  # Verificamos que 3 es primo.
        self.assertFalse(es_primo(4))  # Verificamos que 4 no es primo.
        self.assertTrue(es_primo(5))  # Verificamos que 5 es primo.
        self.assertFalse(es_primo(10))  # Verificamos que 10 no es primo.