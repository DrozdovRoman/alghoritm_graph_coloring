def GraphColoring(rows):
    lenght, i = len(rows), 0
    result = [[] for i in range(lenght)]
    for i in range(lenght):
        result[i] = [i] if rows[i][i] != -1 else []
        for j in range(len(rows[i])):
            if rows[i][j] == 0:
                ConcatinateRows(rows[i], rows[j])
                result[i].append(j)
                ChangeZeroElement(rows, j)
    return result


def ConcatinateRows(rows1, rows2):
    for i in range(len(rows1)):
        rows1[i] += rows2[i]


def ChangeZeroElement(rows, index):
    for i in range(len(rows)):
        for j in range(len(rows)):
            if i == index or j == index:
                rows[i][j] = -1
