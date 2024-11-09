def main():
    """Main program"""
    text = input_data()  # Ввод текста
    max_series_length = solve(text)  # Нахождение длины максимальной серии не-букв
    output_result(max_series_length)  # Вывод результата

def input_data():
    """Input problem data"""
    # Ввод текста от пользователя
    return input("Введите текст: ")

def solve(text):
    """Solver: нахождение длины максимальной серии не-буквенных символов"""
    max_length = 0  # Длина максимальной серии
    current_length = 0  # Текущая длина серии

    for char in text:
        # Если символ не является буквой, увеличиваем текущую серию
        if not char.isalpha():
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            # Если символ — буква, сбрасываем текущую длину серии
            current_length = 0

    return max_length

def output_result(max_series_length):
    """Output result"""
    # Выводим длину максимальной серии не-буквенных символов
    print(f"Длина максимальной серии символов, отличных от букв: {max_series_length}")

if __name__ == "__main__":
    main()
