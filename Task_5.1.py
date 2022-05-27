"""
1) Напишите программу, которая будет считывать содержимое файла,
добавлять к считанным строкам порядковый номер и сохранять их в таком виде в новом файле.

Имя исходного файла необходимо запросить у пользователя, так же, как и имя целевого файла.

Каждая строка в созданном файле должна начинаться с ее номера, двоеточия и пробела,
после чего должен идти текст строки из исходного файла.
"""

# input_user_file = 'test1.txt'
input_user_file = input("Your file names: ")
output_file = 'test2.txt'

my_file1 = open(input_user_file, mode='r', encoding='UTF-8')
my_file2 = open(output_file, mode='w', encoding='UTF-8')  # a

# нумеация построчно начиная с 1
for num, line in enumerate(my_file1, 1):
    #if "Data" in line:
    print("Line " + str(num) + ' : ' + line.strip())
    my_file2.write(str(num) + ': ' + line)

# Закрытие файлов
my_file1.close()
my_file2.close()
