def main():
    """Main program"""
    array = input_data()  # Ввод массива
    result = solve(array)  # Получение чисел, которые больше своего индекса
    output_result(result)  # Вывод результата

def input_data():
    """Input problem data"""
    # Ввод элементов массива через пробел и преобразование их в список целых чисел
    return list(map(int, input("Введите элементы массива через пробел: ").split()))

def solve(array):
    """Solver: отбор чисел, которые больше своего индекса"""
    # Создаем новый список из элементов, для которых выполняется условие a[i] > i
    return [array[i] for i in range(len(array)) if array[i] > i]

def output_result(result):
    """Output result"""
    # Выводим результат в виде строки чисел через пробел
    if result:
        print("Числа, которые больше своего индекса:", " ".join(map(str, result)))
    else:
        print("Нет чисел, которые больше своего индекса.")

if __name__ == "__main__":
    main()
