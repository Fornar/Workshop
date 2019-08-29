# Методы
print("Привет".upper())
print("Привет".replace("е", "@"))
# Списки
fruit = list()
print(fruit)
fruit = []
print(fruit)
fruit = ["Яблоко", "Апельсин", "Персик" ]
fruit.append("Банан")
fruit.append("Дыня")
print(fruit)

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Рандом")
print(random)

fruit = ["Яблоко", "Апельсин", "Персик"]
print(fruit[0])
print(fruit[1])
print(fruit[2])

colors = ["синий", "зелёный", "жёлтый"]
try:
    print(colors[3])
except IndexError:
    print("Ошибка индекса")

colors = ["синий", "зелёный", "жёлтый"]
print(colors)
colors[2] = "красный"
print(colors)


print(colors.pop())
print(colors)
colors.pop()
print(colors)
colors.pop()

colors_matrica = ["синий", "красный", "зелёный"]
colors = ["фиолетовый", "коричневый", "жёлтый"]
colors_matrica.pop()
print(colors_matrica + colors)
print("фиолетовый" in colors)
print("черный" not in colors + colors_matrica)

print("В списке 'colors_matrica'".replace("'", '"'), len(colors_matrica), "элементов")

# Пример использования списка на практике в файле "Списки.py"

#=================================================================================================================================
print("Кортежи".upper())
# Кортежи
# Два варианта создания кортежа:
my_tuple = tuple()
print(my_tuple)

my_tuple = ()
print(my_tuple)

# Добавление объектов в кортеж через второй способ

rndmeme = ("оооо либераху порвало", "Я: ", False)
print(rndmeme)
# Даже при одном элементе нужно после него ставить запятую
number = (27,)
print(number)

# При попытке добавить или изменить содержимое картежа сгенерируется исключение
# Получение осуществляется так же, как и в списках:
dys = ("1984", "О дивный новый мир", "451 градус по Фаренгейту")
print(dys[0])
# Проверка содержимого в кортеже
print("О дивный новый мир" in dys)
print("Мы" not in dys)
# Кортежи удобны при работе со значениями, которые никода не меняются. Они могут гарантировать,
# что другие части программы их не изменят.

#=================================================================================================================================

print("Словари".upper())
# Словари
# Два варианта создания словарей:
my_dict = dict()
print(my_dict)

my_dict = {}
print(my_dict)

# Добавление пары ключ-значение при создании словарей:
fruits = {"Яблоко":
          "красное"}
fruits = {"Яблоко":
          "красное",
          "Банан":
          "жёлтый"}
print(fruits)


# Пример изменения словаря:

facts = dict()

# Добавление значения
facts["код"] = "смешной"
# Поиск значения при помощи ключа
print(facts["код"])

facts["Билл"] = "Гейтс"
print(facts["Билл"])

facts["основание"] = 1776
print(facts["основание"])

# Значением в словаре может быть любой объект. Ключ словаря должен быть неизменяем - может быть или строкой, или кортежем.
# Слово in нельзя использовать для проверки наличия в словаре значеия.

bill = dict({"Билл Гейтс":
             "щедрый"})
print("Билл Гейтс" in bill)

# Если попытаться получить доступ к словарю, отсутствующему в словаре, Python сгенерирует исключение.
print("Билл Дорз" not in bill)

# Удаление их списка пары ключ-значение:
books = {"Дракула": "Стокер",
         "1984": "Оруэлл",
         "Процесс": "Кафка"}
print(books)
del books["Процесс"]
print(books)

# Пример программы, использующей словарь
rhymes = {"1": "смех",
          "2": "синий",
          "3": "я",
          "4": "этаж",
          "5": "жизнь"}

n = 3
if n in rhymes:
    print(rhymes[n])
else:
    print("Не найдено.")
    
print(rhymes)

#=================================================================================================================================
# Контейнеры внутри контейнеров
print("Контейнеры внутри контейнеров".upper())

lists = []
rap = ["Баста", "Кравц", "Злой дух",]
rock = ["Наутилус Помпилиус", "Кино", "Ария"]
djs = ["Paul Oakenfold", "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)
# Получение доступа к списком через индекс
print(lists[2])

lists[2].append("Srillax")
print(lists[2])
# Или через названия подсписков
rap.append("Оксимирон")

print(lists[0][3]) # Вывод: Оксимирон. 1 индекс - список rap.
                   # 2 индекс - элемент "Оксимирон"

# Кортежи внутри списка:
locations = []

tula = (54.1960, 37.6182)
moscow = (55.7522, 37.6155)

locations.append(tula)
locations.append(moscow)

print(locations)


# Списки внутри кортежа

eights = ["Эдгард Алан По",
          "Чарльз Диккенс"]
nines = ["Хемингуэй",
         "Фицджеральд",
         "Оруэлл"]

authors = (eights, nines)
print(authors)
eights.append("Ноу Нейм")
print(authors)
# P.S. списки изменять можно, кортеж нет

bday = {"Хемингуэй": "21.07.1899",
        "Фицджерпльд": "24.09.1896"}
# Словарь внутри списка
my_list = [bday]
print(my_list)
# Словарь внутри кортежа
my_tuple = (bday,)
print(my_tuple)

# Список, кортеж или словарь могут быть значеними в словаре.
ru = {"рсположение": (55.7522, 37.6155),
      "знаменитости": ["Андрей Звягинцев",
                       "Юрий Дудь",
                       "Владимир Путин"],
      "факты": {"столица": "Москва",
                "страна": "Россия"}
}

print(ru)


#=================================================================================================================================

# Множества.
print('Множество'.upper())

# Множества - это структура данных, которая содержит неупорядочные неиндексированные элементы.
# Множества позволяет внесение и удаление элементов.
# Существет ряд особенностей, которые определяют множество от других структур данных:
#  множества не содеражат дубликаты элементов;
#  элементы множества являются неименяемыми,однако само по себе множетсов является изменяемым, и его можно менять;
#  Так как элементы не индексируются, множества не поддерживают никаких операций среза и индексирования.

# Создание множества.
print("Создание множеств".upper())

# Множество может содеражать любое количество элементов и элементы могут быть разных типов,
# к примеру, целые числа, строки, кортежи и т.д.
# Однако, множество не поддерживает изменяемые элементы, такие как списки, словари, и так далее.
# Существует два способа создания множества:

# Можно создать множества путём передачи всех элементов множества внутри фигурных скобок {} и разделить элементы при помощи (,)
num_set = {1, 2, 3, 4, 5, 6}
print(num_set)

string_set = {"Nicholas", "Michelle", "John", "Mercy"}
print(string_set)

# Элементы выдачи могут находится в произвольном порядке.
mixed_set = {2.0, "Nicholas", (1, 2, 3)}
print(mixed_set)



# Можно создать множество из списков.
num_set = set([1, 2, 3, 4, 5, 6])
print(num_set)


# Множество не содержит дубликато элементов:
num_set = set([1, 2, 3, 1, 2])
print(num_set)
# Множество удалило дубликаты 1 и 2
# Это также происходит при создании множества с нуля:
num_set = {1, 2, 3, 1, 2}
print(num_set)


# Создание пустого множества подразумевает определённую хитрость
# Если использовать пустые фигурные скобки, то создастся пустой словарь, а не множество. Например:
x = {}
print(type(x))
# Чтобы создать пустое множество, нужно использовать фунцию set()
x = set()
print(type(x))




# Проверка наличия эелемента во множестве при помощи in
months = set(["Jan", "Feb", "March", "Apr", "May", "June", "Jule", "Aug", "Sep", "Oct", "Nov", "Dec"])
print("May" in months)
print("John" not in months)



# Добавление элементов во множество при помощи фунции add().
months = set(["Jan", "March", "Apr", "May", "June", "Jule", "Aug", "Sep", "Oct", "Nov", "Dec"])
print(months)

months.add("Feb")
print(months)


num_set = {1, 2, 3}
num_set.add(4)
print(num_set)
# При добавлении изменяемых элементов во множество (списков, словарей и т.д.) выйдет исключение TypeError.


# Удаление элемента из множеств
# Элементы могут быть удалены при помощи методов discard() и remove()

num_set = {1, 2, 3, 4, 5, 6}  
num_set.discard(3)  
print(num_set)

num_set = {1, 2, 3, 4, 5, 6}  
num_set.remove(3)  
print(num_set)

# Метод discard() не будет выдавать ошибку, если элемент не найден в отличии от remove()

num_set = {1, 2, 3, 4, 5, 6}  
num_set.discard(7)  
print(num_set)

try:
    num_set = {1, 2, 3, 4, 5, 6}  
    num_set.remove(7)  
    print(num_set)
except KeyError:
    print("Ошибка: этого элемента нет во множестве.")

# С методом pop(), можно удалить и вернуть элемент.
# Так как элементы находятся в произвольном порядке, нельзя утверждать или предсказать, какой элемент будет удален.
# Пример:
num_set = {1, 2, 3, 4, 5, 6}
print(num_set.pop())

# Можно использовать этот метод при удалении элемента и возврате элементов, которые остаются во множестве. Например:

num_set = {1, 2, 3, 4, 5, 6}  
num_set.pop()  
print(num_set)

# Метод clear() поможет удалить все элементы во множестве. Например:

num_set = {1, 2, 3, 4, 5, 6}  
num_set.clear()

print(num_set)


# Объединение множеств.
# Операция объединения двух или более множеств union().
# Пример:

months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])  
months_b = set(["July", "Aug", "Sep", "Oct", "Nov", "Dec"])

all_months = months_a.union(months_b)  
print(all_months)

#

x = {1, 2, 3}  
y = {4, 5, 6}  
z = {7, 8, 9}

output = x.union(y, z)

print(output)

# При выполнении операции объединения, дубликаты игнорируются, так что только один из двух элементов дубликатов будет отображаться.

x = {1, 2, 3}  
y = {4, 3, 6}  
z = {7, 4, 9}

output = x.union(y, z)

print(output)

# Оператор | может также использоваться при поиске объединения двух или более множеств. Например:

months_a = set(["Jan", "Feb", "March", "Apr", "May", "Jun"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov", "Dec"])

print(months_a | months_b)

#

x = {1, 2, 3}  
y = {4, 3, 6}  
z = {7, 4, 9}

print(x | y | z)


























