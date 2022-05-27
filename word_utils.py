from string import punctuation


def word_list(user_str):
    file = open(user_str, 'r', encoding="UTF-8")

    # проход по строкам
    for line in file:
        strings = line.split()
        print("Список и длина строки - ", len(strings), strings)
    # return "Список и длина строки - ", len(strings), strings


def word_longest(user_str):
    file = open(user_str, 'r', encoding="UTF-8")
    long_word = ' '

    # проход по строкам
    for line in file:
        words = line.split()
        # проход по словам
        for word in words:
            word_punc = clear_punct(word)
            # проход по длине слов
            if len(word_punc) >= len(long_word):
                long_word = word_punc

    return "Самое длинное слово: " + long_word


def clear_punct(word):
    for punct in punctuation:
        # print(punctuation)
        # удаление знаков пунтуации
        if punct in word:
            word = word.replace(punct, '')
    return word


def word_clear_punct(user_str):
    file = open(user_str, 'r', encoding="UTF-8")
    text = file.read()
    for punc in punctuation:
        if punc in text:
            text = text.replace(punc, '')
            # print("Текст без пунктуаций:\n ", text)

    return "Текст без пунктуаций:\n " + text


