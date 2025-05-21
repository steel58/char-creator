import random
import time
from conversion_tables import *


def roll_drop(die, count, drop):
    random.seed()
    rolls = []
    for _ in range(count):
        rolls.append(random.randint(1, die))

    rolls.sort(reverse=True)
    return sum(rolls[0:-1])


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


def currency_convert(count, start, finish):
    if start.lower()[0] == "c":
        return copper_convert[finish.lower()[0]] * count
    elif start.lower()[0] == "s":
        return silver_convert[finish.lower()[0]] * count
    elif start.lower()[0] == "e":
        return electrum_convert[finish.lower()[0]] * count
    elif start.lower()[0] == "g":
        return gold_convert[finish.lower()[0]] * count
    elif start.lower()[0] == "p":
        return platinum_convert[finish.lower()[0]] * count
    else:
        return None


def get_total_copper(money):
    total_copper = self.copper
    total_copper += currency_convert(money[1], 's', 'c')
    total_copper += currency_convert(money[2], 'e', 'c')
    total_copper += currency_convert(money[3], 'g', 'c')
    total_copper += currency_convert(money[4], 'p', 'c')

    return total_copper
