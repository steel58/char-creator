def padleft(string, length):
    result = string
    while len(result) < length:
        result = ' ' + result

    return result


def padright(string, length):
    result = string
    while len(result) < length:
        result = result + ' '

    return result


def build_bonus(bonus):
    if bonus < 0:
        result = str(bonus)
    else:
        result = f'+{bonus}'

    return padleft(result, 3)

def build_saves(count):
    first = ' '
    second = ' '
    third = ' '
    if (count >= 1):
        first = 'X'

    if (count >= 2):
        second = 'X'

    if (count >= 3):
        third = 'X'

    return f'[{first}] [{second}] [{third}]'

def segment(string, length):
    words = string.split(' ')
    line_builder = ""
    new_lines = []
    for word in words:
        if len(line_builder) + len(word) + 1 <= length:
            line_builder = line_builder + ' ' + word
        else:
            new_lines.append(line_builder)
            line_builder = word

    new_lines.append(line_builder)
    return new_lines
