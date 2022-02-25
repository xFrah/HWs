from images import save


def parser(filename):
    with open(filename, "r") as f:
        return [[row[x:x + 5] for x in range(0, len(row) - 1, 5)]
                for row in [[int(x) for x in line.replace(",", " ").split()] for line in f]]


def printer(matrix, s):
    x = maxWidth(matrix, s)
    fullDark = [(0, 0, 0)] * x
    image = [fullDark] * s
    for row, (maxH, minH) in zip(matrix, HMap(matrix)):
        spacing = findOffX(x - s * 2, row)
        upper, middle = [fullDark[:] for _ in range((maxH - minH) // 2)], fullDark[:]
        X = s if len(row) != 1 else s + spacing
        for width, height, r, g, b in row:
            comeTogether(middle, upper, (maxH - height) // 2, (height - minH) // 2, width, [(r, g, b)], X)
            X += width + spacing
        image += upper + ([middle] * minH) + upper[::-1] + ([fullDark] * s)
    return image, (x, len(image))


def HMap(matrix):
    return [(max((v := [e[1] for e in row])), min(v)) for row in matrix]


def comeTogether(middle, image, padding, height, width, color, x):
    cRow = color * width
    for c in range(padding, padding + height):
        image[c][x:x + width] = cRow
    middle[x:x + width] = cRow


def findOffX(mW, row):
    return (mW - sum([e[0] for e in row])) // (len(row) - 1) if len(row) != 1 else (mW - row[0][0]) // 2


def maxWidth(matrix, s):
    return max([sum([e[0] for e in row]) + s * (len(row) + 1) for row in matrix])


def ex(file_dati, file_png, spacing):
    l, c = printer(parser(file_dati), spacing)
    save(l, file_png)
    return c


if __name__ == '__main__':
    pass
