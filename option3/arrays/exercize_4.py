def main():
    """Main program"""
    sequence = input_data()  # Ввод данных
    result = solve(sequence)  # Проверка последовательности
    output_result(result)  # Вывод результата

def input_data():
    """Input problem data"""
    # Ввод последовательности чисел через пробел и преобразование их в список float
    return list(map(float, input("Введите последовательность чисел через пробел: ").split()))

def solve(sequence):
    """Solver: проверка, является ли последовательность возрастающей"""
    # Проверка, что каждый элемент меньше следующего
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
    return True

def output_result(is_increasing):
    """Output result"""
    # Вывод результата в зависимости от результата проверки
    if is_increasing:
        print("Последовательность является возрастающей.")
    else:
        print("Последовательность не является возрастающей.")

if __name__ == "__main__":
    main()
