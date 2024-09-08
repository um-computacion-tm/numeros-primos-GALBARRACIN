import unittest  # Importamos el módulo unittest para crear pruebas unitarias.
from io import StringIO  # Importamos StringIO para capturar la salida impresa.
from contextlib import redirect_stdout  # Importamos redirect_stdout para redirigir la salida estándar.
from numeros_primos_propio import es_primo, mostrar_primos  # Importamos las funciones a probar.

# Definimos una clase de pruebas que hereda de unittest.TestCase.
class TestNumerosPrimos(unittest.TestCase):

    # Prueba para la función es_primo.
    def test_es_primo(self):
        self.assertTrue(es_primo(2))  # Verificamos que 2 es primo.
        self.assertTrue(es_primo(3))  # Verificamos que 3 es primo.
        self.assertFalse(es_primo(4))  # Verificamos que 4 no es primo.
        self.assertTrue(es_primo(5))  # Verificamos que 5 es primo.
        self.assertFalse(es_primo(10))  # Verificamos que 10 no es primo.

    # Prueba para la función mostrar_primos.
    def test_mostrar_primos(self):
        # Capturamos la salida estándar utilizando StringIO.
        f = StringIO()

        # Redirigimos la salida estándar para capturar la impresión de los números primos.
        with redirect_stdout(f):
            mostrar_primos(10)  # Llamamos a la función con 10 números primos.

        # Obtenemos la salida capturada.
        output = f.getvalue()

        # Verificamos que la salida capturada sea la esperada.
        self.assertEqual(output.strip(), '2 3 5 7 11 13 17 19 23 29')

# Este bloque asegura que las pruebas se ejecuten cuando este archivo se ejecute directamente.
if __name__ == '__main__':
    unittest.main()  # Ejecuta todas las pruebas definidas.
