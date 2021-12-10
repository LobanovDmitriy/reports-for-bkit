from main import Book, Lib, BookLib, sorting_by_name, sorting_by_sum_of_books, output_books_of_libs_with_NAUCHNAYA
import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        # Библиотеки
        self.libs = [
            Lib(1, 'российская государственная библиотека'),
            Lib(2, 'научная библиотека МГТУ им.Баумана'),
            Lib(3, 'научная библиотека МГУ'),
            Lib(4, 'центральная молодежная библиотека')
        ]

        # Книги
        self.books = [
            Book(1, 'Война и мир', 1225, 1),
            Book(2, 'Горе от ума', 145, 1),
            Book(3, 'Прикладные информационные технологии', 334, 2),
            Book(4, 'Радио и связь', 543, 2),
            Book(5, 'Телекоммуникационные сети', 192, 2),
            Book(6, 'Первая научная история войны 1812 года', 896, 3),
            Book(7, 'Компьютерные сети', 907, 3),
            Book(8, 'Гарри Поттер и философский камень', 223, 4),
            Book(9, 'Бэтмен. Убийственная шутка', 72, 4),
        ]

        self.books_libs = [
            BookLib(1, 1),
            BookLib(2, 1),
            BookLib(3, 2),
            BookLib(4, 2),
            BookLib(5, 2),
            BookLib(6, 3),
            BookLib(7, 3),
        ]
        # Соединение данных один-ко-многим
        self.one_to_many = [(b.name, b.len, l.name)
                            for l in self.libs
                            for b in self.books
                            if b.lib_id == l.id]

        # Соединение данных многие-ко-многим
        self.many_to_many_temp = [(l.name, bl.lib_id, bl.book_id)
                                  for l in self.libs
                                  for bl in self.books_libs
                                  if l.id == bl.lib_id]

        self.many_to_many = [(b.name, b.len, lib_name)
                             for lib_name, lib_id, book_id in self.many_to_many_temp
                             for b in self.books if b.id == book_id]

    def test_sorting_by_name(self):
        result = sorting_by_name(self.one_to_many)
        desired_result = [('Прикладные информационные технологии', 334, 'научная библиотека МГТУ им.Баумана'),
                          ('Радио и связь', 543, 'научная библиотека МГТУ им.Баумана'),
                          ('Телекоммуникационные сети', 192, 'научная библиотека МГТУ им.Баумана'),
                          ('Первая научная история войны 1812 года', 896, 'научная библиотека МГУ'),
                          ('Компьютерные сети', 907, 'научная библиотека МГУ'),
                          ('Война и мир', 1225, 'российская государственная библиотека'),
                          ('Горе от ума', 145, 'российская государственная библиотека'),
                          ('Гарри Поттер и философский камень', 223, 'центральная молодежная библиотека'),
                          ('Бэтмен. Убийственная шутка', 72, 'центральная молодежная библиотека')]
        self.assertEqual(result, desired_result)

    def test_sorting_by_sum(self):
        result = sorting_by_sum_of_books(self.one_to_many, self.libs)
        desired_result = [('научная библиотека МГУ', 1803), ('российская государственная библиотека', 1370),
                          ('научная библиотека МГТУ им.Баумана', 1069), ('центральная молодежная библиотека', 295)]
        self.assertEqual(result, desired_result)

    def test_output_NAUCHNAYA(self):
        result = output_books_of_libs_with_NAUCHNAYA(self.many_to_many, self.libs)
        desired_result = {
            'научная библиотека МГТУ им.Баумана': ['Прикладные информационные технологии', 'Радио и связь',
                                                   'Телекоммуникационные сети'],
            'научная библиотека МГУ': ['Первая научная история войны 1812 года', 'Компьютерные сети']}
        self.assertEqual(result, desired_result)
