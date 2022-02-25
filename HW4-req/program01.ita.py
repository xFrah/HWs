from pronouncing import stresses, phones_for_word
from math import sqrt


def middleValue(values):
    return sum(values) / len(values)


def matrixFromFile(fileName):
    table = "".maketrans(
        {".": "", ",": "", "'": " ", ":": "", "?": "", "!": "", "(": "", ")": "", '"': "", "[": "", "]": "", ";": "",
         "—": "", "`": "", "-": " "})
    lengths = []
    rawMatrix = []
    with open(fileName, encoding="utf-8") as f:
        for line in f:
            line = line.strip("\n")
            if line:
                binLine = []
                for word in line.translate(table).split():
                    phones = phones_for_word(word)
                    if phones:
                        binLine += [x if x != "2" else "0" for x in stresses(phones[0])] + ["0"]
                    else:
                        binLine += ["0"] * (int(len(word) / 2) + 1)
                lengths.append(len(binLine))
                rawMatrix.append(binLine)
    return rawMatrix, lengths


def normalizeMatrix(raw, lengths, tau, output):
    limit = max(lengths)
    with open(output, 'w') as f:
        for i, line in enumerate(raw):
            newLine = line + ["0"] * (limit - lengths[i])
            f.write("".join(newLine) + "\n")
            raw[i] = [0] * tau + [int(c) for c in newLine]
            # print(newLine)
    return raw


def synchronizer(row1, row2, tau):
    mA = sum(row1)
    mB = sum(row2)
    if mA == 0 or mB == 0:
        return 0
    cBA = 0
    cAB = 0
    for n, (x, y) in enumerate(zip(row1, row2)):  # payload che si muove e controlla se ultimo elemento è 1 come cond
        if x == 1 and 1 in row2[n - tau:n + 1]:
            cAB += 1
        if y == 1 and 1 in row1[n - tau:n + 1]:
            cBA += 1
    return (0.5 * (cAB + cBA)) / sqrt(mA * mB)


# @profile
def PoemSync(inputfilename, outputfilename, tau):
    rawMatrix, lengths = matrixFromFile(inputfilename)
    matrix = normalizeMatrix(rawMatrix, lengths, tau, outputfilename)
    syncList = [synchronizer(x, y, tau) for i, x in enumerate(matrix) for j, y in enumerate(matrix) if j != i]
    return round(middleValue(syncList), 6)


if __name__ == "__main__":
    # your tests go here
    pass
