# -*- coding: utf-8 -*-
from line_profiler_pycharm import profile


def rect(cSet, D):
    return [e + [c] for e in rect(cSet, D - 1) for c in cSet if c != (e[-1] if e else [])] if D else [[]]


def null_primer(cSet, d, D):
    return [[c] + p for p in null_primer(cSet, d - 1, D) for c in cSet] if d else [[]]


def WastedTime(current, colors, done, state, counter, result, x, y, D):
    if state == father and x == D - 1:
        return result.append(tuple([tuple(row) for row in setColor(done, current, x, y)]))
    diff, newX, newY, newState, c, k, j = state(current, done, x, y, counter)
    for color in colors - diff:
        WastedTime(color, colors, setColor(done, current, k, j), newState, c, result, newX, newY, D)
    return result


def cross(colors, i, D, shouldI):
    return [e + [color] for e in cross(colors, i - 1, D, shouldI) for color in colors if
            color != (e[-1] if e else [])] if i else [[]]


def father(current, done, x, y, _):
    return {current, done[y - 1][x]}, x + 1, y, right, 0, x, y


def left(current, done, x, y, _):
    return {current, done[y - 1][x], done[y - 1][x - 1], done[y - 1][max(x - 2, 0)]}, x, y, leftRow, x - 1, x, y


def right(current, done, x, y, _):
    return {current, done[y - 1][x - 1], done[y][x - 1], done[max(y - 2, 0)][x - 1]}, x, y, rightColumn, y - 1, x, y


def leftRow(current, done, x, y, counter):
    return ({current, done[y - 1][counter], done[y - 1][counter - 1], done[y - 1][max(counter - 2, 0)]}, x, y, leftRow,
            counter - 1, counter, y) \
        if counter else ({done[y][x], done[y - 1][x], done[y - 1][x + 1]}, x + 1, y, father, 0, counter, y)


def rightColumn(current, done, x, y, counter):
    return (
        {current, done[counter][x - 1], done[counter - 1][x - 1], done[max(counter - 2, 0)][x - 1]}, x, y, rightColumn,
        counter - 1, x, counter) \
        if counter else ({done[y][x], done[y][x - 1], done[y][x - 2]}, x - 1, y + 1, left, 0, x, counter)


def setColor(image, color, x, y):
    image[y][x] = color
    return image


def convert(mat, D):
    return [row + ([None] * (D - len(row))) for row in mat] + [[None] * D for _ in range(D - len(mat))]


def startCross(colors, D):
    shouldI = 1 if D % 2 else 0
    lista = []
    for current in cross(colors, 2, D, shouldI):
        (whole := [tuple((current * (D // 2)) + ([current[0]] * shouldI))] * D)[1::2] = [tuple(
            (current[::-1] * (D // 2)) + ([current[1]] * shouldI))] * (D // 2)
        lista.append(whole)
    return [tuple(x) for x in lista]


def startHrect(colors, D):
    return [tuple([tuple([e] * len(x)) for e in x]) for x in rect(colors, D)]


def startVrect(colors, D):
    return [tuple([tuple(x)] * len(x)) for x in rect(colors, D)]


def startNormal(colors, D):
    return [tuple(x) for x in null_primer(tuple(map(tuple, null_primer(colors, D, D))), D, D)]


def startDiff(colors, D):
    result = []
    if D != 1:
        for mat in [[[h[0], h[1]], [h[2], h[3]]] for h in pls2(colors, 4)]:
            WastedTime(mat[1][1], set(colors), convert(mat, D), father, 0, result, 1, 1, D)
    else:
        result = tuple([tuple([x]) for x in colors])
    return result


def pls2(colors, D):
    return [e + [c] for e in pls2(colors, D - 1) for c in colors if c not in e] if D else [[]]


def ex(colors, D, img_properties):
    return {"pattern_cross_": startCross,
            "pattern_diff_": startDiff,
            "pattern_hrect_": startHrect,
            "pattern_vrect_": startVrect,
            "": startNormal
            }[img_properties](colors, D)


if __name__ == '__main__':
    pass
