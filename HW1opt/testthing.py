def ex2(int_seq, subtotal):
    splitted = [int(char) for char in int_seq.split(",")]
    globalcounter = 0
    counter = 1
    for elem in splitted:
        subtotal0 = elem
        for subelem in splitted[counter:]:
            subtotal0 += subelem
            if subtotal0 > subtotal:
                break
            elif subtotal == subtotal0:
                globalcounter += 1
        counter += 1
    k = 0
    print([splitted[i:len([z for k, z in enumerate(splitted[i:k], 1) if sum(splitted)[i:k] + z < subtotal])] for i, x in enumerate(splitted, 1) if sum(splitted[i:]) + x < subtotal])
    return globalcounter

def ex1(int_seq, subtotal):
    splitted = [int(char) for char in int_seq.split(",")]
    globalcounter = 0
    increment = 0
    listlen = len(splitted)
    for elem in splitted:
        counter = 1 + increment
        subtotal0 = elem
        if subtotal == subtotal0:
            globalcounter += 1
        while subtotal0 <= subtotal and counter < listlen:
            next = splitted[counter]
            subtotal0 += next
            if subtotal == subtotal0:
                globalcounter += 1
            counter += 1
        increment += 1

def ex3(int_seq, subtotal):
    splitted = [int(char) for char in int_seq.split(",")]
    globalcounter = 0
    increment = 0
    listlen = len(splitted)
    for elem in splitted:
        counter = 1 + increment
        subtotal0 = elem
        if subtotal == subtotal0:
            globalcounter += 1
        while subtotal0 <= subtotal and counter < listlen:
            next = splitted[counter]
            subtotal0 += next
            if subtotal == subtotal0:
                globalcounter += 1
            counter += 1
        increment += 1
    return globalcounter


def ex2(int_seq, subtotal):
    splitted = [int(char) for char in int_seq.split(",")]
    lenght = len(splitted)
    for i in range(lenght):
        lista = [splitted[x] for x in range(lenght) if sum(splitted[i:x + 1]) <= subtotal][i:]
        if sum(lista) == subtotal:
            ind = 1
            while lista[-ind] == 0:
                print(lista[:-ind])
                ind += 1
            print(lista)


# ex2('3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2', 9)

def ex4(int_seq, subtotal):
    splitted = [int(char) for char in int_seq.split(",")]
    lenght = len(splitted)
    globalcounter = 0
    for i, elem in enumerate(splitted):
        index = 1
        subtotal0 = elem
        while index + i < lenght:
            next1 = splitted[i + index]
            index += 1
            # subtotal0 += next1
            if subtotal0 == subtotal:
                globalcounter += 1
            if subtotal0 > subtotal:
                break
            subtotal0 += next1
            # print(subtotal0, i)
    # if subtotal0 + splitted[-1] == subtotal:
    # globalcounter += 1
    return globalcounter


def ex4(int_seq, subtotal):
    splitted = [int(char) for char in int_seq.split(",")]
    lenght = len(splitted)
    globalcounter = 0
    for i in range(lenght):
        lista = [splitted[x] for x in range(lenght) if sum(splitted[i:x + 1]) <= subtotal][i:]
        if sum(lista) == subtotal:
            ind = 1
            while lista[-ind] == 0:
                # print(lista[:-ind])
                globalcounter += 1
                ind += 1
            # print(lista)
            globalcounter += 1
    return globalcounter


def ex8(int_seq, subtotal):
    splitted = [int(char) for char in int_seq.split(",")]
    lenght = len(splitted)
    globalcounter = 0
    i = 0
    while i <= lenght:
        index2 = i
        subtotal0 = 0
        while index2 < lenght:

            subtotal0 += splitted[index2]
            if subtotal0 == subtotal:
                globalcounter += 1
            elif subtotal0 > subtotal:
                break

            index2 += 1
        i += 1
    return globalcounter


def occurrences(seq):
    singleset = []
    for n in seq:
        if n not in singleset:
            singleset.append(n)
    for k in singleset:
        print(seq.count(k))


def ex10(int_seq, subtotal):
    splitted = [int(char) for char in int_seq.split(",")]
    globalcounter = 0
    for i, _ in enumerate(splitted):
        subtotal0 = 0
        for k in splitted[i:]:
            subtotal0 += k
            if subtotal0 == subtotal:
                globalcounter += 1
            elif subtotal0 > subtotal:
                break

    return globalcounter


def ex10(int_seq, subtotal):
    splitted = tuple(int(char) for char in int_seq.split(","))
    globalcounter = 0
    lenght = len(splitted)
    for i in range(lenght):
        subtotal0 = 0
        for k in range(i, lenght):
            if splitted[k] != 0:
                subtotal0 += splitted[k]
                if subtotal0 > subtotal:
                    break
            if subtotal0 == subtotal:
                globalcounter += 1

    return globalcounter


def MIGLIORE(int_seq, subtotal):
    splitted = tuple(int(char) for char in int_seq.split(","))
    globalcounter = 0
    lenght = len(splitted)
    for i in range(lenght):
        subtotal0 = 0
        for k in range(i, lenght):
            subtotal0 += splitted[k]
            if subtotal0 < subtotal:
                continue
            elif subtotal0 == subtotal:
                globalcounter += 1
            elif subtotal0 > subtotal:
                break

    return globalcounter


def ex11(int_seq, subtotal):
    splitted = tuple(int(char) for char in int_seq.split(","))
    globalcounter = 0
    lenght = len(splitted)
    for i in range(lenght):
        subtotal0 = 0
        for k in range(i, lenght):
            subtotal0 += splitted[k]
            if subtotal0 < subtotal:
                continue
            elif subtotal0 == subtotal:
                globalcounter += 1
            elif subtotal0 > subtotal:
                break

    return globalcounter


def ex12(int_seq, subtotal):
    splitted = [int(char) for char in int_seq.split(",")]
    media = int(subtotal / (sum(splitted) / len(splitted)))
    index = 0
    globalcounter = 0
    for x in range(len(splitted)):
        somma = sum(splitted[x:media])
        offset = 0
        goinglower = None
        # while somma != subtotal:
        if somma < subtotal:
            while somma < subtotal:
                offset += 1
                somma += splitted[media + offset]
        elif somma > subtotal:
            while somma > subtotal:
                offset -= 1
                somma -= splitted[media + offset]
        if somma == subtotal:
            globalcounter += 1

        index += 1
    return globalcounter


# while x + index <= length:
#    somma += direction * next1
#    if somma < subtotal:
#        index += 1
#        continue
#    elif somma == subtotal:
#        index += 1
#        somma -= splitted[x]
#        last = splitted[x]
#        globalcounter += 1
#    elif somma > subtotal:
#        last2 = next1
#        somma -= last2
#        index -= 1
#        accumulator += last2
#        break

def ex15(int_seq, subtotal):
    splitted = [int(char) for char in int_seq.split(",")]
    globalcounter = 0
    shit = False
    length = len(splitted)
    somma = 0
    last = 0
    index2 = 0
    stringa = ""
    for x in range(length):
        index = 0
        if shit:
            stringa = stringa[1:]
            somma -= splitted[x - 1]
            tempstringa = stringa
            tempsomma = somma
            while tempsomma <= subtotal:

                ind = 0
                while splitted[index2 - ind] == 0:
                    globalcounter += 1
                    print(tempstringa[:-ind])
                    ind += 1

                next1 = splitted[index2 + 1]
                if tempsomma == subtotal:
                    globalcounter += 1
                    print(tempstringa)
                tempstringa += str(next1)
                tempsomma += next1
                if tempsomma > subtotal:
                    break
                somma = tempsomma
                index2 += 1

        if not shit:
            stringa = ""
        while not shit:
            somma += splitted[x + index]
            if somma < subtotal:
                stringa += str(splitted[x + index])
                index += 1
                continue
            elif somma == subtotal:
                # last = splitted[x + index]
                shit = True
                stringa += str(splitted[x + index])
                globalcounter += 1
                ind = 1
                print(stringa)
                somma = subtotal
                while splitted[x + index + ind] == 0:
                    globalcounter += 1
                    stringa += str(splitted[x + index + ind])
                    print(stringa)
                    ind += 1
                index2 = index
            elif somma > subtotal:
                somma = 0
                break
    return globalcounter

def asd(lista : list):
    return [(x - 32)/1.8 for x in lista]

