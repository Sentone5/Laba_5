#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В списке, состоящем из вещественных элементов, вычислить:
# 1) сумму отрицательных элементов списка;
# 2) произведение элементов списка, расположенных между максимальным и минимальным
# элементами.
# Упорядочить элементы списка по возрастанию.

import sys

if __name__ == '__main__':
    print(((4 + 15) ** 2) % 19 + 1)
    a = list(map(float, input().split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    a_min = a_max = a[0]
    i_min = i_max = 0
    for i, item in enumerate(a):
        if item < a_min:
            i_min, a_min = i, item
        if item >= a_max:
            i_max, a_max = i, item

    if i_min > i_max:
        i_min, i_max = i_max, i_min

    sum = 0
    for item in a:
        if item < 0:
            sum += item

    proiz = 1
    for i, item in enumerate(a):
        if i_min < i < i_max:
            proiz *= item

    a.sort()
    print("Список, упорядоченные по возрастанию:\n", a)
    print("Сумма отрицательных эл. списка = {}\n"
          "Произведение элементов списка между максимальным и минимальным = {}".format(sum, proiz)
          )
