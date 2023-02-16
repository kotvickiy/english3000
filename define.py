from random import shuffle


def lst_word():
    res = []
    with open('words3000.csv', encoding='utf-8', newline='') as file:
        for i in [i for i in file.readlines()]:
            res.append(i.strip().split(','))
    return res


def crop_shuffle_list(n):
    if len(str(n).split(' ')) == 1:
        x = int(n)
        res = lst_word()[x - 1:x + 9]
    elif len(str(n).split(' ')) == 2:
        x = int(str(n).split(' ')[0])
        y = int(str(n).split(' ')[1])
        res = lst_word()[x - 1:x - 1 + y]
    shuffle(res)
    return res


def start_text():
    return '↷↷Введите число от 1 до 2990'


def verify_word(user_word, word):
    return user_word[0].lower() == word[0].lower()

def error_list(lst):
    # for i in lst:
    #     with open('err_words.csv', 'a', encoding='utf-8', newline='') as file:
    #         file.write(f'{i}\n')
    pass
