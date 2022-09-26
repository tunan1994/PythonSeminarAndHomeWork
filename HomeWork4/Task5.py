# 5 - Реализуйте RLE алгоритм: реализуйте модуль
# сжатия и восстановления данных. Входные и выходные 
# данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.


def rle_for_numbers(data):
    string = ''
    cout = 1
    for i in range(len(string)-1):
        if i <= len(string):
            if string[i] == string[i + 1]:
                cout += 1
            else:
                a = string[i]
                print(cout, string[i])
                cout = 1
    print(cout, string[i])

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

with open("RLEencode.txt", "r", encoding= 'utf-8') as enterFile:
    enterData = enterFile.readline()
print(f'Ваша запись во входящем файле: {enterData}')

encoded_val = rle_encode(enterData) 
print(f'Ваша запись после RLE-сжатия: {encoded_val}')

decoded_val = rle_decode(encoded_val)
print(f'Ваша запись после RLE-восстановления: {decoded_val}')

with open("RLEdecode.txt", "w", encoding= 'utf-8') as exitFile:
    exitFile.write(decoded_val)

enterFile.close()
exitFile.close()