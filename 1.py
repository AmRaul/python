user_num = input('write ')
translate_number = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate():
    for key in translate_number.keys():
        if key == user_num:
            i = translate_number[key]
            return i


i = num_translate()
print(i)