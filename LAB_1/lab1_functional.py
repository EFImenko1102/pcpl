import sys
import math


def get_coef(index, prompt, is_a=False):
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


def get_x_from_y(y):
    clean_y = 0.0 if abs(y) < 1e-12 else y
    match clean_y:
        case 0.0:
            return [0.0]
        case val if val > 0.0:
            root = math.sqrt(val)
            return [-root, root]
        case _:
            return []


def get_roots(a, b, c):
    D = b * b - 4 * a * c
    clean_D = 0.0 if abs(D) < 1e-12 else D

    match clean_D:
        case d if d < 0.0:
            y_roots = []
        case 0.0:
            y_roots = [-b / (2.0 * a)]
        case d if d > 0.0:
            sqD = math.sqrt(d)
            y_roots = [
                (-b + sqD) / (2.0 * a),
                (-b - sqD) / (2.0 * a)
            ]
        case _:
            y_roots = []

    all_x = [x for y in y_roots for x in get_x_from_y(y)]
    return sorted(list(set(all_x)))


def print_roots(roots):
    match roots:
        case []:
            print('Нет корней')
        case [r1]:
            print(f'Один корень: {r1}')
        case [r1, r2]:
            print(f'Два корня: {r1} и {r2}')
        case [r1, r2, r3]:
            print(f'Три корня: {r1}, {r2}, {r3}')
        case [r1, r2, r3, r4]:
            print(f'Четыре корня: {r1}, {r2}, {r3}, {r4}')
        case _:
            print(f'Корни: {roots}')


def main():
    a = get_coef(1, 'Введите коэффициент А: ', is_a=True)
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')

    roots = get_roots(a, b, c)
    print_roots(roots)


if __name__ == '__main__':
    main()
