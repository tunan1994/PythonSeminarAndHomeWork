# 4.Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


s = ["123", "234", "123", "567", "qwe", "asd", "zxc", "qwe", "ertqwe"]
x = s.index("qwe")
s[x] = "change"
f = s.index("qwe")
print('Позиция элемента второго вхождения =', f)

