# Задача № 3
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел 
# для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random
from itertools import permutations

def is_valid_board(board):
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == j - i:
                return False
    return True

def generate_valid_boards():
    cols = range(8)
    solutions = []
    for perm in permutations(cols):
        if is_valid_board(perm):
            solutions.append(perm)
            if len(solutions) == 4:
                break
    return solutions

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == row else "." for col in range(8)))

def main():
    valid_boards = generate_valid_boards()
    print(f"Найдено {len(valid_boards)} решения:")
    for i, board in enumerate(valid_boards, 1):
        print(f"\nВариант {i}:")
        print_board(board)

if __name__ == "__main__":
    main()
