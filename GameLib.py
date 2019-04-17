from collections import defaultdict


def renewEmptyCell(field, newField, i, j):
    neighbors = calcNeighbors(field, i, j)
    if neighbors['f'] == 3:
        newField[i][j] = 'f'
    elif neighbors['s'] == 3:
        newField[i][j] = 's'


def calcNeighbors(field, i, j):
    neighbors = defaultdict(int)
    for k in range(3):
        for p in range(3):
            if i - 1 + k in range(0, len(field)) and j - 1 + p in range(0, len(field[0])):
                if not(k == 1 and p == 1):
                    neighbors[field[i - 1 + k][j - 1 + p]] += 1
    return neighbors


def renewRock(field, newField, i, j):
    newField[i][j] = 'r'


def renewFish(field, newField, i ,j):
    neighbors = calcNeighbors(field, i, j)
    if neighbors['f'] in range(2, 4):
        newField[i][j] = 'f'
    else:
        newField[i][j] = '.'


def renewShrimp(field, newField, i, j):
    neighbors = calcNeighbors(field, i, j)
    if neighbors['s'] in range(2, 4):
        newField[i][j] = 's'
    else:
        newField[i][j] = '.'


def renewCell(field, newField, i, j):
    if field[i][j] == '.':
        renewEmptyCell(field, newField, i, j)
    elif field[i][j] == 'f':
        renewFish(field, newField, i, j)
    elif field[i][j] == 's':
        renewShrimp(field, newField, i, j)
    elif field[i][j] == 'r':
        renewRock(field, newField, i, j)


def renewField(field):
    emptyLine = []
    newField = []

    for _ in range(len(field[0]) + 2):
        emptyLine.append('.')

    for i in field:
        i.insert(0, '.')
        i.insert(len(i), '.')
    field.insert(0, emptyLine[:])
    field.insert(len(field), emptyLine[:])

    for i in range(len(field)):
        newField.append(emptyLine[:])

    for i in range(len(field)):
        for j in range(len(field[i])):
            renewCell(field, newField, i, j)
    return newField


def game(generations, field):
    for i in range(generations):
        field = renewField(field)
    return field
