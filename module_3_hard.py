def calculate_structure_sum(data):
    total_sum = 0  # Инициализация переменной total_sum значением 0

    # Если data является числом (int или float):
    if isinstance(data, (int, float)):
        total_sum += data  # Добавляем значение data к total_sum

    # Если data является строкой (str):
    elif isinstance(data, str):
        total_sum += len(data)  # Добавляем длину строки к total_sum

    # Если data является списком (list), кортежем (tuple) или множеством (set):
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            total_sum += calculate_structure_sum(item)  # Рекурсивно вызываем функцию для каждого элемента

    # Если data является словарём (dict):
    elif isinstance(data, dict):
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)  # Рекурсивно вызываем функцию для каждого ключа
            total_sum += calculate_structure_sum(value)  # Рекурсивно вызываем функцию для каждого значения

    return total_sum  # Возвращаем сумму




data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый вывод: 99


'''Разберем, как функция работает на этом примере:
1. data_structure — это список, содержащий различные типы данных: списки, словари, кортежи и строки.
2. Для каждого из элементов списка функция вызывается рекурсивно.
3. Сначала обрабатывается вложенный список [1, 2, 3], каждый элемент которого является числом. В итоге,
 сумма этих чисел: 1 + 2 + 3 = 6.
4. Затем обрабатывается словарь {'a': 4, 'b': 5}. Ключи являются строками, их длина 1, что даёт 1 + 1 = 2.
 Значения являются числами, итоговая сумма: 2 + 4 + 5 = 11.
5. Далее идёт кортеж (6, {'cube': 7, 'drum': 8}). Сначала добавляется число 6, затем обрабатывается словарь,
 аналогично предыдущему примеру. Итоговая сумма этого кортежа: 6 + 1 (длина 'cube') + 7 + 1 (длина 'drum') + 8 = 23.
6. Следующая строка "Hello", длина которой 5.
7. Последний элемент — это кортеж, содержащий пустой кортеж и список с множеством, в котором находится кортеж.
 Это добавит 2 (число внутри вложенного кортежа) и длину строки 'Urban', а также числа внутри самого вложенного 
 кортежа: 2 + 5 (длина 'Urban') + 1 (длина 'Urban2') + 35 = 99.

Суммируя все результаты, приведённый код должен вернуть 99, как и указано в комментарии.'''