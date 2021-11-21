#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from moduls import get_human, display_people, whois


if __name__ == '__main__':

    def main():
        """
        Главная функция программы.
        """
        people = []
        # Организовать бесконечный цикл запроса команд.
        while True:
            # Запросить команду из терминала.
            command = input(">>> ").lower()

            # Выполнить действие в соответствие с командой.
            if command == 'exit':
                break

            elif command == 'add':
                get_human(people)

            elif command == 'list':
                display_people(people)

            elif command == 'whois':
                whois(people)

            else:
                print('Неизвестная команда', command, file=sys.stderr)

    main()