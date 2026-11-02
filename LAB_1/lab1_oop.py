import sys
import math


class BiquadraticEquation:

    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.roots = []

    def get_coef(self, index, prompt, is_a=False):
        if len(sys.argv) > index:
            try:
                val = float(sys.argv[index])
                if not (is_a and val == 0.0):
                    return val
            except ValueError:
                pass

        while True:
            try:
                val = float(input(prompt).strip())
                if is_a and val == 0.0:
                    print("Коэффициент А не может быть равен 0.")
                    continue
                return val
            except ValueError:
                print("Некорректное значение. Введите число.")

    def read_coeffs(self):
        self.a = self.get_coef(1, 'Введите коэффициент А: ', is_a=True)
        self.b = self.get_coef(2, 'Введите коэффициент B: ')
        self.c = self.get_coef(3, 'Введите коэффициент C: ')

    def solve(self):
        self.roots = []
        D = self.b * self.b - 4 * self.a * self.c

        if D < 0.0:
            return self.roots

        y_list = []
        if D == 0.0:
            y_list.append(-self.b / (2.0 * self.a))
        elif D > 0.0:
            sqD = math.sqrt(D)
            y_list.append((-self.b + sqD) / (2.0 * self.a))
            y_list.append((-self.b - sqD) / (2.0 * self.a))

        res = []
        for y in y_list:
            if abs(y) < 1e-12:
                y = 0.0

            if y > 0.0:
                rx = math.sqrt(y)
                res.append(rx)
                res.append(-rx)
            elif y == 0.0:
                res.append(0.0)

        self.roots = sorted(list(set(res)))
        return self.roots

    def print_roots(self):
        count = len(self.roots)
        if count == 0:
            print('Нет корней')
        elif count == 1:
            print(f'Один корень: {self.roots[0]}')
        elif count == 2:
            print(f'Два корня: {self.roots[0]} и {self.roots[1]}')
        elif count == 3:
            print(f'Три корня: {self.roots[0]}, {self.roots[1]}, {self.roots[2]}')
        elif count == 4:
            print(f'Четыре корня: {self.roots[0]}, {self.roots[1]}, {self.roots[2]}, {self.roots[3]}')


def main():
    eq = BiquadraticEquation()
    eq.reёad_coeffs()
    eq.solve()
    eq.print_roots()


if __name__ == '__main__':
    main()
