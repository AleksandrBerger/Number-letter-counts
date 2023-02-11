import inflect

def number_to_word(n: int):
    p = inflect.engine()
    listx = []
    for i in range(1, n+1):
        listx.append(p.number_to_words(i))
    print(listx)
    return listx


number_to_word(1000)