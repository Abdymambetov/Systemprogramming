def main():
    """Main program"""
    array = input_data()  # Ввод массива
    counts = solve(array)  # Подсчет элементов
    output_result(counts)  # Вывод результата

def input_data():
    """Input problem data"""
    # Ввод элементов массива через пробел и преобразование их в список float
    return list(map(float, input("Введите элементы массива через пробел: ").split()))

def solve(array):
    """Solver: подсчет отрицательных, положительных и нулевых элементов"""
    negative_count = sum(1 for x in array if x < 0)
    positive_count = sum(1 for x in array if x > 0)
    zero_count = sum(1 for x in array if x == 0)
    return negative_count, positive_count, zero_count

def output_result(counts):
    """Output result"""
    negative_count, positive_count, zero_count = counts
    print(f"Количество отрицательных элементов: {negative_count}")
    print(f"Количество положительных элементов: {positive_count}")
    print(f"Количество нулевых элементов: {zero_count}")

if __name__ == "__main__":
    main()
