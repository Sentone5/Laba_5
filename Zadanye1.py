#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти произведение положительных элементов кратных 3,
# их количество и вывести результаты на экран

if __name__ == '__main__':
    A = list(map(float, input("Введите список из 10 элементов ").split()))
    proiz = 1
    count = 0
    for item in A:
        if item > 0 and item % 3 == 0:
            proiz *= item
            count += 1
    print(proiz, count)