"""
2) Реализуйте модуль  word_utils.py, позволяющий:

- очистить предложение от знаков препинания;
- получить список слов из предложения;
- получить самое длинное слово в предложении;
"""
import word_utils
#from word_utils import word_list, word_longest, word_clear_punct

user_str = input("Укажите путь и имя файла: ")
W = word_utils
print(W.word_longest(user_str))
print(W.word_list(user_str))
print(W.word_clear_punct(user_str))




