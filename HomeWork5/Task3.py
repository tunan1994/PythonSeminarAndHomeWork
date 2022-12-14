# 3-Создайте два списка — один с названиями языков программирования, 
# другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, 
# состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма 
# очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж
# остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв 
# в слове. Порядковые номера смотрите в этой таблице, в третьем столбце:
# https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с 
# преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

lang = ['java', 'python', 'c#', 'c', 'c++', 'javascript', 'typescript', 'php']
nums = [i for i in range(1, len(lang)+1)]
ln = list(zip(nums,lang))
for i in range(len(ln)):
    ln[i] = list(ln[i])
    ln[i][1] = str(ln[i][1]).upper()
    ln[i] = tuple(ln[i])
print(ln)
for i in range(len(ln)):
    ln[i] = list(ln[i])
sums = []
for i in range(len(ln)):
    sum = 0
    for j in ln[i][1]:
        sum += ord(j)
    sums.append(sum)
print(sums)
ln_new = []
for i in range(len(ln)):
    if sums[i] % ln[i][0] == 0:
        ln_new.append((sums[i], ln[i][1]))
print(ln_new)