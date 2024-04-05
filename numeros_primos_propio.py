"""Esta función que verifica si un número dado es primo."""

def es_primo(numero):
    if numero <= 1:
        return False  #Los números menores o iguales a 1 no son primos
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  #Si el número es divisible por algún otro número, no es primo.
    return True  #Si no se encontró ningún divisor, el número es primo.


""" Esta función muestra la cantidad especifica dada de números primos."""
def mostrar_primos(cantidad):
    contador = 0
    numero = 2  #Empezamos con el primer número primo.
    while contador < cantidad:
        if es_primo(numero):
            print(numero, end=" ")  # Muestra el número primo.
            contador += 1
        numero += 1  #Paso al siguiente número para verificar si es primo.

#Pruebo la función mostrar_primos con 10 números primos.
mostrar_primos(10)


'''  Defino las funciones de prueba para cada parte del código '''

def test_es_primo():
    assert es_primo(2) == True   #Los assert son aserciones, sirven para verificar si las funciones producen los resultados esperados.
    assert es_primo(3) == True
    assert es_primo(4) == False
    assert es_primo(5) == True
    assert es_primo(10) == False

def test_mostrar_primos():
    #Redirijo la salida estándar para capturar la impresión.
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        mostrar_primos(10)
    output = f.getvalue()
    assert output.strip() == '2 3 5 7 11 13 17 19 23 29'

#Ejecuto las pruebas.
test_es_primo()
test_mostrar_primos() 

#Si el test funciona correctamente (si no se produce ninguna excepción), el programa se ejecuta sin imprimir nada en la terminal.