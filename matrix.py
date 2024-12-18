from random import randint


def gen_matrix(n, m, value=0, random=False):
    """
    Genera una matriz de n x m con el valor dado
    Si random es True, genera una matriz con valores aleatorios entre 0 y 9
    """
    return [[randint(0, 9) if random else value for _ in range(m)] for _ in range(n)]


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


def fill_diagonal(matrix, value, diagonal=True):
    # TODO: Implementar la función
    # Recibe una matriz, un valor y un booleano que indica si se debe rellenar la diagonal principal (por defecto) o la secundaria (si es False).
    # La diagonal principal es aquella que va desde la esquina superior izquierda a la inferior derecha.
    # La diagonal secundaria (o antidiagonal) es aquella que va desde la esquina superior derecha a la inferior izquierda.
    # Rellena la diagonal correspondiente con el valor dado
    # Si is_main es True, rellena la diagonal principal
    # Si is_main es False, rellena la diagonal secundaria
    # Si la matriz no es cuadrada, no hace nada
    # Les dejo un ejemplo de cómo debería funcionar en el docstring de la función
    """
    >>> m = gen_matrix(3, 3, 0)
    >>> fill_first_diagonal(m, 1) # Diagonal principal
    >>> print_matrix(m)
    1 0 0
    0 1 0
    0 0 1

    >>> m = gen_matrix(3, 3, 0)
    >>> fill_second_diagonal(m, 1, False) # Antidiagonal
    >>> print_matrix(m)
    0 0 1
    0 1 0
    1 0 0
    """
    pass


# Tiene 4 posibles valores para las 4 combinaciones de triángulos superiores e inferiores
def fill_triangle(matrix, value, upper=True, diagonal=True):
    # TODO: Implementar la función
    # Tiene 4 posibles valores para las 4 combinaciones de triángulos superiores e inferiores
    """
    >>> m = gen_matrix(4, 4, 0)
    >>> fill_triangle(m, 1) # Triángulo superior
    >>> print_matrix(m)
    1 1 1 1
    0 1 1 1
    0 0 1 1
    0 0 0 1

    >>> m = gen_matrix(4, 4, 0)
    >>> fill_triangle(m, 1, False) # Triángulo inferior
    >>> print_matrix(m)
    1 0 0 0
    1 1 0 0
    1 1 1 0
    1 1 1 1

    >>> m = gen_matrix(4, 4, 0)
    >>> fill_triangle(m, 1, True, False) # Triángulo superior
    >>> print_matrix(m)
    1 1 1 1
    1 1 1 0
    1 1 0 0
    1 0 0 0

    >>> m = gen_matrix(4, 4, 0)
    >>> fill_triangle(m, 1, False, False) # Triángulo inferior
    >>> print_matrix(m)
    0 0 0 1
    0 0 1 1
    0 1 1 1
    1 1 1 1
    """
    pass


def fill_border(matrix, value):
    # TODO: Implementar la función
    # Rellena el borde de la matriz con el valor dado
    # El borde de la matriz es la primera y última fila y columna
    """
    >>> m = gen_matrix(3, 3, 0)
    >>> fill_border(m, 1)
    >>> print_matrix(m)
    1 1 1
    1 0 1
    1 1 1
    """
    pass


def add_matrix(matrix1, matrix2):
    # TODO: Implementar la función
    # Suma dos matrices y devuelve una nueva matriz con el resultado
    # Si las matrices no tienen las mismas dimensiones, devuelve None
    # La suma de dos matrices es la suma de los elementos de la misma posición
    """
    >>> m1 = gen_matrix(2, 2, 1)
    >>> m2 = gen_matrix(2, 2, 2)
    >>> m3 = sum_matrix(m1, m2)
    >>> print_matrix(m3)
    3 3
    3 3

    >>> m1 = gen_matrix(2, 2, 1)
    >>> m2 = gen_matrix(3, 3, 2)
    >>> m3 = sum_matrix(m1, m2)
    >>> print(m3)
    None

    >>> m1 = gen_matrix(4, 4, 2)
    >>> m2 = gen_matrix(4, 4, 3)
    >>> m3 = sum_matrix(m1, m2)
    >>> print_matrix(m3)
    5 5 5 5
    5 5 5 5
    5 5 5 5
    5 5 5 5
    """
    pass


def sub_matrix(matrix1, matrix2):
    # TODO: Implementar la función
    # Resta dos matrices y devuelve una nueva matriz con el resultado
    # Si las matrices no tienen las mismas dimensiones, devuelve None
    # La resta de dos matrices es la resta de los elementos de la misma posición
    """
    >>> m1 = gen_matrix(2, 2, 1)
    >>> m2 = gen_matrix(2, 2, 2)
    >>> m3 = sub_matrix(m1, m2)
    >>> print_matrix(m3)
    -1 -1
    -1 -1

    >>> m1 = gen_matrix(2, 2, 1)
    >>> m2 = gen_matrix(3, 3, 2)
    >>> m3 = sub_matrix(m1, m2)
    >>> print(m3)
    None

    >>> m1 = gen_matrix(4, 4, 2)
    >>> m2 = gen_matrix(4, 4, 3)
    >>> m3 = sub_matrix(m1, m2)
    >>> print_matrix(m3)
    -1 -1 -1 -1
    -1 -1 -1 -1
    -1 -1 -1 -1
    -1 -1 -1 -1
    """


def mult_matrix(matrix1, matrix2):
    # TODO: Implementar la función
    # Multiplica dos matrices y devuelve una nueva matriz con el resultado
    # Si las matrices no tienen las mismas dimensiones, devuelve None
    # La multiplicación de dos matrices es la suma de los productos de los elementos de la misma posición
    # Busquen en internet cómo se multiplican dos matrices
    # Ojo con las dimensiones de las matrices. Tienen que controlar que se puedan multiplicar
    # Este ejercicio es para obtener el sobresaliente
    pass


def transpose(matrix):
    # TODO: Implementar la función
    # Devuelve la matriz transpuesta
    # Este ejercicio es para obtener la matrícula de honor
    # Buscar como se calcula la matriz transpuesta
    # https://es.wikipedia.org/wiki/Matriz_transpuesta
    pass


if __name__ == "__main__":
    m = gen_matrix(5, 5, 0, True)
    print_matrix(m)
