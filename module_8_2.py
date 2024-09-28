def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except ZeroDivisionError:
            incorrect_data += 1
        except TypeError :
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')

    return (result,incorrect_data)

def calculate_average(numbers):
    """Среднее арифметическое - сумма всех данных делённая на их количество."""
    try:
        check_n = 0
        for i in numbers:
            if isinstance(i, int):
                check_n += 1
        average = personal_sum(numbers)[0] / check_n
    except ZeroDivisionError:
        average = 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return

    return average



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать


