def find_min_max(arr):
    # Базові випадки
    if len(arr) == 0:
        return (None, None)
    if len(arr) == 1:
        return (arr[0], arr[0])
    if len(arr) == 2:
        return (min(arr), max(arr))

    # Рекурсивний випадок
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Об'єднання результатів
    return (min(left_min, right_min), max(left_max, right_max))


if __name__ == "__main__":
    tests = [
        [3, 7, 2, 9, 1, 5],
        [42],
        [10, 5],
        [-5, -2, -10, 3, 0, 8]
    ]
    for arr in tests:
        minimum, maximum = find_min_max(arr)
        print(f"Масив: {arr}")
        print(f"Результат: мінімум = {minimum}, максимум = {maximum}")
        print()
