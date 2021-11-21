#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Используя замыкания функций, объявите внутреннюю функцию,
которая преобразует строку из списка целых чисел, записанных
через пробел, либо в список, либо в кортеж. Тип коллекции
определяется параметром type внешней функции. Если type = 'list',
то используется список, иначе – кортеж. Далее, на вход программы
поступает две строки: первая – это значение для параметра type;
вторая – список целых чисел, записанных через пробел. С помощью
реализованного замыкания преобразовать эту строку в
коллекцию. Результат работы замыкания выведите на экран.
"""

from fun import func


if __name__ == '__main__':
    print(func('list')('1 2 3 4'))
    print(func('tuple')('1 2 3 4 5'))
