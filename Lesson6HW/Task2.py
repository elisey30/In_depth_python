def queens_attack_each_other(queens):
    """
    Функция принимает список из 8 пар координат ферзей (где каждая пара - это (x, y)).
    Возвращает False, если хотя бы одна пара ферзей бьет друг друга, иначе True.
    """
    n = len(queens)
    for i in range(n):
        for j in range(i + 1, n):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or \
               abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

queens_positions = [(1, 4), (2, 2), (3, 7), (4, 3), (5, 6), (6, 8), (7, 5), (8, 1)]
print(queens_attack_each_other(queens_positions))
