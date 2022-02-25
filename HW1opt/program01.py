# -*- coding: utf-8 -*-

"""
Let int_seq be a string that contains a sequence of non-negative
    integers separated by commas and subtotal a non-negative integer.

Design a function ex1(int_seq, subtotal) that:
    – takes as parameters
      a string (int_seq) and a positive integer (subtotal >= 0), and
    – returns the number of substrings of int_seq such that
      the sum of their values is equal to subtotal.

Hint: you can obtain a substring by picking any consecutive
    elements in the original string.

For example, given int_seq = '3,0,4,0,3,1,0,1,0,0,5,0,4,2' and subtotal = 9,
    the function should return 7. The following substrings, indeed, consist of
    values whose sum is equal to 9:
    int_seq = '3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
            => _'0,4,0,3,1,0,1,0'_____________
               _'0,4,0,3,1,0,1'_______________
               ___'4,0,3,1,0,1,0'_____________
               ___'4,0,3,1,0,1'_______________
               ___________________'0,0,5,0,4'_
               _____________________'0,5,0,4'_
               _______________________'5,0,4'_

NOTE: it is FORBIDDEN to use/import any libraries

NOTE: Each test must terminate on the VM before the timeout of
    1 second expires.

WARNING: Make sure that the uploaded file is UTF8-encoded
    (to that end, we recommend you edit the file with Spyder)
"""


def zeroCounter(upper, lista, limit):
    ind = 1
    counter = 0
    while upper + ind < limit and lista[upper + ind] == 0:
        counter += 1
        ind += 1
    return counter


def ex1(int_seq, subtotal):
    splitted = [int(char) for char in int_seq.split(",")]
    globalcounter = 0
    length = len(splitted)
    somma = 0
    upper = 0
    x = 0
    while upper < length - 1:
        print(splitted[x:upper + 1])
        somma += splitted[upper]
        if somma == subtotal:
            globalcounter += zeroCounter(upper, splitted, length) + 1
            print("asd", splitted[x:upper + 1]) # qua gli manca qualche combinazione, precisamente 2, la terza e la quarta
        elif somma > subtotal:
            somma -= splitted[x]
            x += 1
        upper += 1
        # somma += splitted[upper]
    while True:
        x += 1
        if somma < subtotal:
            break
        elif somma == subtotal:
            globalcounter += 1
            #print(splitted[x - 1])
        somma -= splitted[x - 2]
        #print(splitted[x - 1])
    return globalcounter


if __name__ == '__main__':
    print(ex1('3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2', 9))

    pass
