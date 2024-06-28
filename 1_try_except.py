def add_everything_up(a, b):
    some_data = [a, b]
    try:
        return print(sum(some_data))

    except TypeError:
        if (type(some_data[0]) == int or float) and type(some_data[1]) == str:
            print(f'{some_data[0]}{some_data[1]}'
                  f'\n^Не по-ГОСТу конечно^...')
        if (type(some_data[1]) == int or float) and type(some_data[0]) == str:
            print(f'{some_data[0]}{some_data[1]}'
                  f'\n^Не по-ГОСТу конечно^...')


add_everything_up(75.312, 'YaY')
add_everything_up('BeB', 51632)
add_everything_up(865.67, 14)
