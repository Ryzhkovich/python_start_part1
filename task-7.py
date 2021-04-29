# Задание №7
# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexClass:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, ComplexClass):
            other = other.__complex

        complex_ = self.__complex + other
        return ComplexClass(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, ComplexClass):
            other = other.__complex

        complex_ = self.__complex * other
        return ComplexClass(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


if __name__ == '__main__':
    c1 = ComplexClass(3, 4)
    c2 = ComplexClass(5)
    # Вывод
    print(c1 + c2)
    print(c1 * c2)
    # Проверка
    print('\n')
    print(complex(3, 4) + complex(5))
    print(complex(3, 4) * complex(5))
