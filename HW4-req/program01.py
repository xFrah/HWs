# -*- coding: utf-8 -*-
from pronouncing import stresses, phones_for_word
from math import sqrt


def middleValue(values):
    return round(sum(values) / len(values), 6)


def matrixFromFile(fileName):
    with open(fileName, encoding="utf-8") as f:
        return ["".join(map(mFormat, alphaCheck(line).split())).replace("2", "0") for line in filter(None, f.read().splitlines())]


def mFormat(word):
    return stresses(phones[0]) + "0" if (phones := phones_for_word(word)) else "0" * ((len(word) // 2) + 1)


def alphaCheck(stringa):
    return "".join([char if char.isalpha() else " " for char in stringa])


def fixAndWrite(raw, tau, output):
    limit = max(map(len, raw))
    with open(output, 'w') as f:
        for i, line in enumerate(raw):
            temp = line.ljust(limit, "0")
            raw[i] = ("0" * tau + temp, [k + tau for k, char in enumerate(line) if char == "1"])
            f.write(temp + "\n")
    return raw


def synchronizer(a, b, tau):
    return 0 if not len(a[1]) * len(b[1]) else (0.5 * (getC(a[0], b[1], tau) + getC(b[0], a[1], tau))) / sqrt(len(a[1]) * len(b[1]))


def getC(row, ind, tau):
    c = 0
    for n in ind:
        if "1" in row[n - tau:n + 1]:
            c += 1
    return c


def PoemSync(inputfilename, outputfilename, tau):
    matrix = fixAndWrite(matrixFromFile(inputfilename), tau, outputfilename)
    rangeLen = range(len(matrix))
    return middleValue([synchronizer(matrix[x], matrix[y], tau) for x, y in {TwoOfUs(i, j) for i in rangeLen for j in range(i + 1, len(matrix))}])


def TwoOfUs(i, j):
    return (i, j) if i < j else (j, i)


if __name__ == "__main__":
    pass
