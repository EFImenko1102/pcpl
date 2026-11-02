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


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c

    if D < 0.0:
        return result

    y_list = []
    if D == 0.0:
        y_list.append(-b / (2.0 * a))
    elif D > 0.0:
        sqD = math.sqrt(D)
        y_list.append((-b + sqD) / (2.0 * a))
        y_list.append((-b - sqD) / (2.0 * a))

    for y in y_list:
        if abs(y) < 1e-12:
            y = 0.0

        if y > 0.0:
            root_x = math.sqrt(y)
            result.append(root_x)
            result.append(-root_x)
        elif y == 0.0:
            result.append(0.0)

    return sorted(list(set(result)))


def main():
    a = get_coef(1, 'Введите коэффициент А: ', is_a=True)
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')

    roots = get_roots(a, b, c)

    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print(f'Один корень: {roots[0]}')
    elif len_roots == 2:
        print(f'Два корня: {roots[0]} и {roots[1]}')
    elif len_roots == 3:
        print(f'Три корня: {roots[0]}, {roots[1]}, {roots[2]}')
    elif len_roots == 4:
        print(f'Четыре корня: {roots[0]}, {roots[1]}, {roots[2]}, {roots[3]}')


if __name__ == '__main__':
    main()
