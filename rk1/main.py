# используется для сортировки
from operator import itemgetter


class Column:
    def __init__(self, id, name, size, table_id):
        self.id = id
        self.name = name
        self.size = size
        self.table_id = table_id


class Table:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class TableColumn:
    def __init__(self, table_id, column_id):
        self.table_id = table_id
        self.column_id = column_id


# Таблицы данных
tables = [
    Table(1, 'Пользователи'),
    Table(2, 'Заказы'),
    Table(3, 'Товары'),
    Table(4, 'Аналитика'),
    Table(5, 'Логи'),
]

# Колонки данных
columns = [
    Column(1, 'Счетчик просмотров', 8, 4),
    Column(2, 'Количество заказов', 4, 1),
    Column(3, 'Набор тегов', 64, 3),
    Column(4, 'Список файлов', 128, 5),
    Column(5, 'Идентификатор', 8, 1),
    Column(6, 'Электронная почта', 64, 1),
    Column(7, 'Стоимость', 8, 2),
    Column(8, 'Дата создания', 8, 2),
]

# Связь многие-ко-многим
tables_columns = [
    TableColumn(1, 2),
    TableColumn(1, 3),
    TableColumn(1, 5),
    TableColumn(1, 6),
    TableColumn(1, 8),
    TableColumn(2, 2),
    TableColumn(2, 4),
    TableColumn(2, 5),
    TableColumn(2, 7),
    TableColumn(2, 8),
    TableColumn(3, 1),
    TableColumn(3, 3),
    TableColumn(3, 5),
    TableColumn(3, 7),
    TableColumn(3, 8),
    TableColumn(4, 1),
    TableColumn(4, 5),
    TableColumn(4, 8),
    TableColumn(5, 1),
    TableColumn(5, 4),
    TableColumn(5, 5),
    TableColumn(5, 8),
]


def main():
    # Соединение данных один-ко-многим
    one_to_many = [
        (c.name, c.size, t.name)
        for t in tables
        for c in columns
        if c.table_id == t.id
    ]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [
        (t.name, tc.table_id, tc.column_id)
        for t in tables
        for tc in tables_columns
        if t.id == tc.table_id
    ]

    many_to_many = [
        (c.name, c.size, table_name)
        for table_name, table_id, column_id in many_to_many_temp
        for c in columns
        if c.id == column_id
    ]

    print('Задание Б1')
    res_1 = sorted(
        [(c_name, c_size, t_name) for c_name, c_size, t_name in one_to_many],
        key=itemgetter(0)
    )
    print(res_1)

    print('\nЗадание Б2')
    res_2_unsorted = []
    for t in tables:
        t_cols = list(filter(lambda i: i[2] == t.name, one_to_many))
        if len(t_cols) > 0:
            res_2_unsorted.append((t.name, len(t_cols)))
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    print('\nЗадание Б3')
    res_3 = {}
    for c in columns:
        if c.name.endswith('ов'):
            c_tables = list(filter(lambda i: i[0] == c.name, many_to_many))
            c_tables_names = [table_name for _, _, table_name in c_tables]
            res_3[c.name] = c_tables_names
    print(res_3)


if __name__ == '__main__':
    main()
