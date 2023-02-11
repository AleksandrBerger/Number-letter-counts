#developed in pycharm


import inflect


def number_to_word(n1: int, n2: int):
    p = inflect.engine()
    listx = []
    for i in range(n1, n2+1):
        listx.append(p.number_to_words(i))
    return listx


def letter_counts(list_numbers_x: list):
    count = 0
    for i in list_numbers_x:
        count += len(i)
        if i.count("-") > 0 or i.count(" ") > 0 or i.count("and"):
            count -= i.count("-") - i.count(" ") - i.count("and")

    return count


print(letter_counts(number_to_word(1, 1000)))
