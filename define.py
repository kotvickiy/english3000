from random import shuffle


def lst_word():
    res = []
    with open('words3000.csv', encoding='utf-8', newline='') as file:
        for i in [i for i in file.readlines()]:
            res.append(i.strip().split(','))
    return res


def crop_shuffle_list(x):
    res = lst_word()[x - 1:x + 9]
    shuffle(res)
    return res


def start_text():
    return '↷Введите число от 1 до 2990'
