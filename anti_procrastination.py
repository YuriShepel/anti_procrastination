from math import ceil


def main(commands, activity_dict):
    while True:
        print_menu()
        choice = input_data('Выберите номер меню: ')
        if choice == '5':
            quit()

        try:
            choice = commands[choice]
        except KeyError:
            print('Такого пункта меню нет')
            continue

        try:
            choice(activity_dict)
        except Exception as e:
            print(e)


def print_menu():
    """Функция выводит информационное меню программы."""

    print('-' * 31)
    print('Программа "Анти-Прокрастинация"')
    print('-' * 31)
    print('МЕНЮ ПРОГРАММЫ:')
    print('1. Рассчитать статистику по вашему свободному временив.')
    print('2. Добавить новую активность в список')
    print('3. Удалить активность из списка.')
    print('4. Посмотреть список активностей.')
    print('5. Выйти из программы')
    print('*' * 41)
    print('Для завершения ввода данных введите "Все"')
    print('*' * 41)
    print()


def input_data(message):
    """Функция запрашивает данные при ее вызове и возвращает результат."""

    data = input(message).lower()
    return data


def get_activities_time(activity_dict):
    """Функция возвращает сумму минут из дневных активностей введенных пользователем."""

    activity_time = []
    while True:
        activity = input_data('Введите режим дня: ')
        if activity == 'все':
            break

        try:
            key = activity_dict[activity]
        except KeyError:
            print('Такая активность отсутствует. Вы можете ее добавить в список.')
            continue
        activity_time.append(activity_dict[activity])

    print('Информация об активности получена.')
    return sum(activity_time)


def make_calculation(activity_dict):
    """Функция делает расчеты на основании дневной активности пользователя
    из функции "get_activities_time"."""

    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24
    WORKING_DAYS_IN_MONTH = 20.6
    WORKING_DAYS_IN_YEAR = 247

    busy_minutes = get_activities_time(activity_dict)
    busy_hours = ceil(busy_minutes / MINUTES_IN_HOUR)
    rest_per_day = HOURS_IN_DAY - busy_hours
    rest_per_month = rest_per_day * WORKING_DAYS_IN_MONTH
    rest_per_year = rest_per_day * WORKING_DAYS_IN_YEAR
    rest_days_per_year = ceil(rest_per_year / HOURS_IN_DAY)

    message = (
        'Вы тратите в рабочий день примерно %d минут '
        'или %.0f часов на активность.\n'
        'На отдых у вас остается %d часов.\n'
        'В месяц на отдых в рабочие дни у вас уходит %d часов.\n'
        'В год на отдых у вас уходит %d часов,\n'
        'а это %d дней, не считая выходных и праздников.'
    )
    print('-' * 20)
    print(message % (busy_minutes, busy_hours,
                     rest_per_day, rest_per_month, rest_per_year,
                     rest_days_per_year
                     ))


def add_activity(activity_dict):
    """Функция добавляет в словарь новую активность и время."""

    while True:
        name = input_data('Введите название активности: ')
        if name == 'все':
            break
        try:
            if name in activity_dict:
                raise KeyError(f'Активность "{name.capitalize()}" уже существует.')
        except KeyError as e:
            print(e)
            continue

        time = input_data('Введите время активности в минутах: ')
        try:
            if not time.isdecimal():
                raise TypeError(f'Нужно время в минутах.')
        except TypeError as e:
            print(e)
            continue

        activity_dict.update({name: time})


def del_activity(activity_dict):
    """Функция удаляет из словаря активность."""

    while True:
        activity_for_del = input_data('Введите название активности для удаления: ')
        if activity_for_del == 'все':
            break

        try:
            activity_dict.pop(activity_for_del)
            print(f'Удаление активности "{activity_for_del.capitalize()}" произведено.')
        except KeyError:
            print('Данная активность отсутствует.')
            continue


def print_activities(activity_dict):
    """Функция выводит распакованный словарь с названием активности и ее время."""

    print('Текущий список активностей:')

    for activity, time in activity_dict.items():
        print(f'{activity.capitalize():20}{time} минут')
    print()


daily_activity = {
    'сон': 480,
    'подъем': 15,
    'душ': 15,
    'завтрак': 30,
    'одевание': 10,
    'дорога на работу': 50,
    'работа': 480,
    'дорога с работы': 50,
    'покупки': 30,
    'приготовление еды': 40,
    'ужин': 30
}

commands = {
    '1': make_calculation,
    '2': add_activity,
    '3': del_activity,
    '4': print_activities
}

main(commands, daily_activity)
