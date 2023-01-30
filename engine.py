


def lst_word():
    res = []
    with open('words3000.csv', encoding='utf-8', newline='') as file:
        for i in [i for i in file.readlines()]:
            res.append(i.strip().split(','))
    return res

word = lst_word()[6]

english_word = word[0]
transcription_word = word[1]

russian_word = word[2].split(';')

# if b in c:
#     print('ok')
