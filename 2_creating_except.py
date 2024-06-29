class PerfectionistException(Exception):
    """
    Класс исключения чисел типа 'float'.
    Только целые числа, только хардкор!
    """
    pass


class NoStringException(Exception):
    """
    Класс исключения строкового типа данных 'str'.
    Только целые числа, только хардкор!
    """
    pass


class LimitCharException(Exception):
    """
    Класс исключения выхода символов за допустимый лимит.
    """
    pass


def len_char_sum(num1, num2):
    result = num1 + num2
    return len(str(result))


def perfecto_sum(a, b):
    """
    Функция сложения без остатка.
    Никаких строк.
    """
    try:
        is_a_float = (float == type(a))
        is_b_float = (float == type(b))
        is_a_int = (int == type(a))
        is_b_int = (int == type(b))
        is_a_str = (str == type(a))
        is_b_str = (str == type(b))

        if (is_a_float and is_b_int) or (is_a_int and is_b_float):
            raise PerfectionistException(a + b)
        if is_a_float and is_b_float:
            raise PerfectionistException(a + b)
        if ((is_a_float or is_a_int) and is_b_str) or (is_a_str and (is_b_float or is_b_int)):
            raise TypeError('Числа со строками, они как две параллельные прямые - никогда не пересекаются.')
        if str == type(a) and str == type(b):
            raise NoStringException('Строкам тут не место! Давай по-новой, Миша, всё фигня.')

    except PerfectionistException as exc:
        len_char_sum(a, b)
        print(f'Ну что это такое: {exc}? Зачем эти некрасивые точки?'
              f'\nТак уж и быть, в этот раз исправлю за тебя.'
              f'\nБольше так не делай >_<')
        return print(f'Результат: {round(a + b)}')

    except NoStringException:
        print('\nПостарайся и в другой раз у тебя обязательно получится...\nНаверное)')
        raise

    except TypeError:
        print('\nПостарайся и в другой раз у тебя обязательно получится...\nНаверное)')
        raise

    else:
        len_char_sum(a, b)
        return print(f'Вот это по-нашему!\nРезультат: {a + b}')

    finally:
        print('\nЯ завершил свою работу,\nЯ - спать!\n')


def char_limit(a, b):
    perfecto_sum(a, b)
    fin = len_char_sum(a, b)
    try:
        if fin > 5:
            raise LimitCharException('Лимит символов исчерпан. На выходе должно быть не более 5-ти символов')

    except LimitCharException:
        raise


# Варианты для проверки ошибок разного типа:

# perfecto_sum(4151, 162)
# perfecto_sum(75.643, 326)
# perfecto_sum('Boba', 'Fett')
# perfecto_sum(32.57, 'Peppa')
# perfecto_sum('Kenny', 613)
# char_limit(1612, 56685)
# char_limit(652, 512638)
