"""
    Ваша задача дописать функции, чтобы они проходили все тесты

    Именование функций проиходит по шаблону: `t{number_of_task}`. Пожалуйста не меняйте эти имена.

    Разрешается использовать только стандартные библиотеки языка.
"""


def t1(number):
    """
    Поправьте код что бы возвращаемое значение было ближайшим сверху, кратным к 20

    Пример: number=21 тогда нужно вернуть 40
    Пример: -5 -> 0

    """
    return number if number%20 == 0 else number + 20 - (number % 20)


def t2(string):
    """
    На вход подается набор слов разделенных пробелом, инвертируйте каждое слово.

    Пример: `abc abc abc` -> `cba cba cba`
    """
    return " ".join([i[::-1] for i in string.split(' ')])



def t3(dictionary):
    """
    На вход подается словарь. Преорбазуйте его в строку по следующему шаблону 'key: value; key: value' и так далее

    """
    return str(dictionary).replace(",", ";").replace("{", "").replace("}", "").replace("'", "")


def t4(string, sub_string):
    """
    проверить есть ли в строке инвертированная подстрока
    """
    return string.find(sub_string[::-1]) != -1

def t5(strings):
    """
    На вход подается список строк,
    Отфильтруйте список строк, оставив только строки в формате: `x y z x*y*z`, где x,y,z - целые положительные числа
    """
    nums = [i.split(" ") for i in strings]
    return [" ".join(i) for i in nums if int(i[0]) * int(i[1]) * int(i[2]) == int(i[3])]


def t6(string):
    """
    Предположим у вас есть строки содержащие `#` символ, который означает backspace (удаление предыдущего) обработаете
        такие строки

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
    """
    del_count = 0
    s = ""
    for i in string[::-1]:
        if i!= "#":
            if del_count == 0:
                s += i
            else:
                del_count -= 1
        else:
            del_count += 1
    return s[::-1]


def t7(lst):
    """
    На вход подается список элементов, найдите сумму уникальных элементов списка.

    Например: [4,5,7,5,4,8] -> 15 потому что 7 и 8 уникальны
    """
    return sum([i for i in lst if lst.count(i) == 1])


def t8(string):
    """
    Найдите все последовательности числев в строке и среди них найдите максимальное число

    gh12cdy695m1 -> 695
    """
    nums = []
    i = 0
    while i < len(string):
        snum = ""
        a = string[i]
        while "0" <= a <= "9":
            snum += a
            i += 1
            if i < len(string):
                a = string[i]
            else:
                break
        i += 1
        if snum != "":
            nums.append(int(snum))
    return max(nums)


def t9(number):
    """
    Приведите число number к пятизначному виду.

    Т.е. для числа 5 верните `00005`
    """
    return str(number) if len(str(number)) >=5 else "0"*(5-len(str(number)) )+ str(number)


def t10(string):
    """
    Произведите смешивание цветов. Вам будет дана строка, необходимо смешать все пары цветов и вернуть результируюший
        цвет

    Комбинации цветов:    G G     B G    R G   B R
    Результирующий цвет:   G       R      B     G

    R R G B R G B B  <- ввод
     R B R G B R B
      G G B R G G
       G R G B G
        B B R R
         B G R
          R B
           G  <-- вывод

    """
    colors = {"GG": "G",
              "BG": "R",
              "GB": "R",
              "RG": "B",
              "GR": "B",
              "BR": "G",
              "RB": "G",
              "RR": "R",
              "BB": "B"}
    #
    # while len(string) != 1:
    #     for i in colors.keys():
    #         string = string.replace(i, colors[i])
    # return string
    while len(string) != 1:
        for i in range(len(string)-1):
            if i == len(string)-1:
                continue
            key = string[i] + string[i+1]
            string = string[:i] + colors[key] + string[i+1:]
        string = string[:len(string)-1]
    return string


def t11(lst):
    """
    Вам дам список из целых чисел. Найдите индекс числа такого, что левая и правая части списка от него равны
        Если такого элемента нет - верните -1. Если вы нашли два элемента -> верните тот, который левее.
    [1,2,3,5,3,2,1] = 3
    [1,12,3,3,6,3,1] = 2
    [10,20,30,40] = -1
    """
    for i in range(len(lst)-1):
        if sum(lst[0:i]) == sum(lst[i+1:len(lst)]):
            return i
    return -1

def t12(lst):
    """
    На вход подается список строк вида `Что-то происходит бла бла бла +7495 123-45-67` содержащие номер телефона.
        Используя regex выражения запишите всевозможноые комбинации телефонов, например программа должна корректно
        работать с 790112345678 или 890112345678
    Вход: [`Что-то происходит бла бла бла +7495 123-45-67`]
    Выход: [`84951234567`]

    """
    pass


def t13(number_1, number_2):
    """
    Сложите два числа по элементно:
        248
       +208
        4416
    """
    rank = 1
    res = 0
    while number_1 > 0 or number_2 > 0:
        a = number_1 % 10
        b = number_2 % 10
        c = a + b
        res += rank * c
        if c // 10 == 0:
            rank *= 10
        else:
            rank *= 100
        number_1 = number_1 // 10
        number_2 = number_2 // 10

    return res


def t14(string):
    """
    Преобразуйте математическое выражение (символьное) в буквенное выраэение

    Для операций используйте следующую таблицу
        { '+':   'Plus ',
          '-':   'Minus ',
          '*':   'Times ',
          '/':   'Divided By ',
          '**':  'To The Power Of ',
          '=':   'Equals ',
          '!=':  'Does Not Equal ' }
    Примеры:
        4 ** 9 -> Four To The Power Of Nine
        10 - 5 -> Ten Minus Five
        2 = 2  -> Two Equals Two
    """
    dictionary = {'+': 'Plus',
     '-': 'Minus',
     '**': 'To The Power Of',
     '*': 'Times',
     '/': 'Divided By',
     '!=': 'Does Not Equal',
     '=': 'Equals ',
     '10': 'Ten',
     '0': 'Zero',
     '1': 'One',
     '2': 'Two',
     '3': 'Three',
     '4': 'Four',
     '5': 'Five',
     '6': 'Six',
     '7': 'Seven',
     '8': 'Eight',
     '9': 'Nine'
     }

    for i in dictionary.keys():
        string = string.replace(i, dictionary[i])
    return string


def t15(lst):
    """
    Найдите сумму элементов на диагоналях

    [[ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]]
    Результат: 30
    """
    n = len(lst)
    diagsum = 0
    for i in range(n):
        diagsum += lst[i][i] + lst[n-i-1][n-i-1]
    return diagsum

