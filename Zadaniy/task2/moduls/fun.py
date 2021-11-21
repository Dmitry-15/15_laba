#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_human(people):
    """
    Запросить данные о человеке.
    """
    name = input("Фамилия и инициалы? ")
    zodiac = input("Знак Зодиака? ")
    year = list(map(int, input("Дата рождения? ").split()))
    # Создать словарь.
    human = {
        'name': name,
        'zodiac': zodiac,
        'year': year,
    }
    # Добавить словарь в список.
    people.append(human)
    # Отсортировать список в случае необходимости.
    if len(people) > 1:
        people.sort(key=lambda x: x.get('year')[::-1])


def display_people(people):
    """
    Отобразить список людей.
    """
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Знак Зодиака",
            "Дата рождения"
        )
    )
    print(line)
    # Вывести данные о всех людях.
    for idx, human in enumerate(people, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                idx,
                human['name'],
                human['zodiac'],
                ' '.join((str(i) for i in human['year']))
            )
        )
    print(line)


def whois(people):
    """
    Выбрать человека по фамилии.
    """
    who = input('Кого ищем?: ')
    count = 0
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Знак Зодиака",
            "Дата рождения"
        )
    )
    print(line)
    for i, num in enumerate(people, 1):
        if who == num['name']:
            count += 1
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    count,
                    num['name'],
                    num['zodiac'],
                    ' '.join((str(i) for i in num['year']))))
    print(line)
    if count == 0:
        print('Никто не найден')