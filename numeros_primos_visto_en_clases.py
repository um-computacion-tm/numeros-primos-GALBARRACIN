import unittest

def is_primo(value):
    if value < 2:  # Los números menores que 2 no son primos
        return False
    div = 2
    while div * div <= value:  # No es necesario dividir más allá de la raíz cuadrada
        if value % div == 0:
            return False
        div += 1
    return True

class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, False)  # 1 no es primo
    
    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)  # 2 es primo

    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)  # 3 es primo

    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)  # 4 no es primo

    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)  # 5 es primo

    def test_6(self):
        result = is_primo(6)
        self.assertEqual(result, False)  # 6 no es primo

    def test_7(self):
        result = is_primo(7)
        self.assertEqual(result, True)  # 7 es primo

    def test_8(self):
        result = is_primo(8)
        self.assertEqual(result, False)  # 8 no es primo

    def test_9(self):
        result = is_primo(9)
        self.assertEqual(result, False)  # 9 no es primo

    def test_10(self):
        result = is_primo(10)
        self.assertEqual(result, False)  # 10 no es primo

if __name__ == "__main__":
    unittest.main()
