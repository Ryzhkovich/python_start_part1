# Задание №1
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    matrix_row = None
    matrix_col = None

    def __init__(self, matrix_row, matrix_col):
        self.matrix_row = matrix_row
        self.matrix_col = matrix_col
        self.matrix = [[]]
        # Задаем пустую матрицу
        if matrix_row < 1:
            self.set_empty_matrix(1, self.matrix_col)
        else:
            self.set_empty_matrix(self.matrix_row, self.matrix_col)
        if matrix_col < 1:
            self.set_empty_matrix(self.matrix_row, 1)
        else:
            self.set_empty_matrix(self.matrix_row, self.matrix_col)
        # Строим матрицу
        self.build_matrix()

    def __str__(self):
        str_res = ''
        for item in self.matrix:
            str_res += ' '.join(map(str, item)) + '\n'

        return str_res

    def __add__(self, other):
        # new_matrix = [[]]
        i = 0
        j = 0
        while i < self.matrix_row:
            while j < self.matrix_col:
                # new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                j += 1
                # print(f'(i:{i}, j:{j})')
            i += 1
            j = 0
        self.get_matrix_view()
        return self.matrix

    def set_empty_matrix(self, param_row, param_col):
        self.matrix = [[0 for col in range(param_col)] for row in range(param_row)]

    def get_matrix(self):
        return self.matrix

    def get_matrix_view(self):
        for item in self.matrix:
            print(item)

    def set_matrix_element(self, row, col, val):
        self.matrix[row][col] = val

    def build_matrix(self):
        i = 0
        j = 0
        while i < self.matrix_row:
            while j < self.matrix_col:
                try:
                    val = int(input(f'Введите число для матрицы со строкой {i} и колонкой {j}: '))
                except ValueError as verr:
                    continue
                    # pass  # do job to handle:
                    # s does not contain anything convertible to int
                except Exception as ex:
                    continue
                    # pass  # do job to handle: Exception occurred while converting to int
                self.matrix[i][j] = val
                j += 1
                self.get_matrix_view()
            i += 1
            j = 0
        print('Мы закончили!')


# Параметр можно поставить любой
# Сюда например я задавал значения от 1 до 9
m = Matrix(4, 2)
# Сюда например я задавал значения все десятки
n = Matrix(4, 2)

print('Вывод в строковом формате')
print(str(m))
print('Вывод в строковом формате')
print(str(n))
# Это суммирование матриц
m + n
