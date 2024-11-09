def main():
    """Main program"""
    array, K = input_data()  # Ввод массива и числа K
    counts = solve(array, K)  # Подсчет количества элементов относительно K
    output_result(counts, K)  # Вывод результата

def input_data():
    """Input problem data"""
    # Ввод элементов последовательности и числа K
    array = list(map(float, input("Введите элементы последовательности через пробел: ").split()))
    K = float(input("Введите число K: "))
    return array, K

def solve(array, K):
    """Solver: подсчет чисел, меньших, равных и больших K"""
    less_than_k = sum(1 for x in array if x < K)
    equal_to_k = sum(1 for x in array if x == K)
    greater_than_k = sum(1 for x in array if x > K)
    return less_than_k, equal_to_k, greater_than_k

def output_result(counts, K):
    """Output result"""
    less_than_k, equal_to_k, greater_than_k = counts
    print(f"Количество чисел меньше {K}: {less_than_k}")
    print(f"Количество чисел равно {K}: {equal_to_k}")
    print(f"Количество чисел больше {K}: {greater_than_k}")

if __name__ == "__main__":
    main()
