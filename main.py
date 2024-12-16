#Импортируем библиотеку json
import json

#Определяем имя файла, где будет храниться информация о звёздах
file = 'stars.json'

#Проверяем, существует ли файл, если нет, создаем его с начальными данными
try:
    with open(file, 'r') as f:
        stars = json.load(f)
except FileNotFoundError:
    #Создаём список с данными о звёздах и сохраняем его в переменную data_about_stars_1
    data_about_stars_1 = [
        {"id": 1, "name": "Сириус", "constellation": "Большой Пёс", "is_visible": True, "radius": 1.71},
        {"id": 2, "name": "Канопус", "constellation": "Корма", "is_visible": True, "radius": 0.73},
        {"id": 3, "name": "Арктур", "constellation": "Богатырь", "is_visible": True, "radius": 1.5},
        {"id": 4, "name": "Вега", "constellation": "Лира", "is_visible": True, "radius": 2.13},
        {"id": 5, "name": "Полиус", "constellation": "Центавр", "is_visible": False, "radius": 1.3}
    ]
    stars = data_about_stars_1
    with open(file, 'w') as f:
        json.dump(stars, f)

#Создаём переменную count_of_operations, которая будет использоваться для подсчета количества выполненных операций с записями о звездах
count_of_operations = 0

#Создаём бесконечный цикл, который будет работать до того момента, пока пользователь не захочет выйти
while True:
    #Выводим меню с пятью вариантами действий
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")

    #Создаём переменную user_choice, в которой происходит обработка того варианта действия, который выбрал пользователь
    user_choice = input("Выберите пункт меню: ")
    
    #Если пользователь выбрал 1-ый вариант действия
    if user_choice == '1':
        #Программа открывает файл stars.json для чтения данных
        with open(file, 'r') as f:
            #Данные о звёздах из файла загружаются в переменную stars
            stars = json.load(f)
            #Программа выводит: "Все записи: "
            print("\nВсе записи:")
            for star in stars:
                #Вывод данных о звёздах, используя json.dumps() для отступов
                print(json.dumps(star, ensure_ascii = False, indent = 4))
        
        #Счётчик операций увеличивается на 1
        count_of_operations += 1

    #Если пользователь выбрал 2-ой вариант действия
    elif user_choice == '2':
        try:
            #Программа запрашивает у пользователя ID звезды
            ID = int(input("Введите ID записи для поиска: "))
            #Программа открывает файл stars.json для чтения данных
            with open(file, 'r') as f:
                found = False
                #С помощью цикла for перебираем все ID звёзд
                for index, star in enumerate(stars):
                    #Если звёзда с указанным ID найдена
                    if star['id'] == ID:
                        #Программа выводит: "Запись найдена (позиция {index + 1})"
                        print(f"\nЗапись найдена (позиция {index + 1}):")
                        #Вывод информация о звёздах, используя json.dumps() для отступов
                        print(json.dumps(star, ensure_ascii = False, indent = 4))
                        #Флажок found изменяется на True
                        found = True
                        break
            #Если такой записи не обнаружено
            if not found:
                #Программа выводит: "Запись не найдена"
                print("Запись не найдена.")
            #Счётчик операций увеличивается на 1
            count_of_operations += 1
        except ValueError:
            #Выводится сообщение об ошибке
            print("Пожалуйста, введите корректный числовой ID.")

    #Если пользователь выбрал 3-ий вариант действия
    elif user_choice == '3':
        #Программа создаёт новый словарь с именем new_star для сохранения информации о новой звезде
        new_star = {
            #Запрашиваем у пользователя ID
            'id': len(stars) + 1,
            #Запрашиваем у пользователя название звезды
            'name': input("Введите имя звезды: "),
            #Запрашиваем у пользователя название созвездия
            'constellation': input("Введите созвездие: "),
            #Запрашиваем у пользователя информацию, можно ли увидеть звезду без телескопа
            'is_visible': input("Является ли звезда видимой (True/False): ") == 'True',
            #Запрашиваем у пользователя солнечный радиус звезды
            'radius': float(input("Введите радиус звезды: "))
        }
        #Новая звезда добавляется в список new_star
        stars.append(new_star)
        #Программа открывает файл stars.json для чтения данных
        with open(file, 'w') as f:
            json.dump(stars, f)
        #Счётчик операций увеличивается на 1
        count_of_operations += 1
        #Программа выводит: "Запись успешно добавлена."
        print("Запись успешно добавлена.")

    #Если пользователь выбрал 4-ый вариант действия
    elif user_choice == '4':
        try:
            #Программа запрашивает у пользователя ID звезды, которую он хочет удалить из файла
            ID_to_delete = int(input("Введите ID записи для удаления: "))
            stars = [star for star in stars if star['id'] != ID_to_delete]
            #Программа открывает файл stars.json для чтения данных
            with open(file, 'w') as f:
                json.dump(stars, f)
            #Счётчик операций увеличивается на 1
            count_of_operations += 1
            #Программа выводит: "Запись успешно удалена."
            print("Запись успешно удалена.")
        except ValueError:
            #Выводится сообщение об ошибке
            print("Пожалуйста, введите корректный числовой ID.")

    #Если пользователь выбрал 5-ый вариант действия
    elif user_choice == '5':
        #Программа выводит количество выполненных операций
        print(f"Количество выполненных операций: {count_of_operations}")
        break
    else:
        #Выводится сообщение об ошибке
        print("Неверный выбор. Пожалуйста, выберите пункт меню от 1 до 5.")
