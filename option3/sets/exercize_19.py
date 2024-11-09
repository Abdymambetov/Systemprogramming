def main():
    """Main program"""
    file_path = input_data()  # Путь к файлу
    vowels = solve(file_path)  # Нахождение всех гласных
    output_result(vowels)  # Вывод результата

def input_data():
    """Input problem data"""
    # Ввод пути к файлу
    return input("Введите путь к файлу: ")

def solve(file_path):
    """Solver: нахождение гласных букв"""
    # Множество русских строчных гласных
    vowels_set = set("аеёиоуыэюя")
    found_vowels = set()  # Множество для найденных гласных

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()  # Чтение текста из файла в нижнем регистре

        # Проходим по всем символам текста
        for char in text:
            if char in vowels_set:  # Проверяем, является ли символ гласной
                found_vowels.add(char)

    except FileNotFoundError:
        print(f"Файл по пути {file_path} не найден.")
        return set()

    return found_vowels

def output_result(vowels):
    """Output result"""
    if vowels:
        print("Гласные буквы, встречающиеся в тексте:")
        # Сортировка найденных гласных по алфавиту и вывод
        print(" ".join(sorted(vowels)))
    else:
        print("Гласные буквы не найдены.")

if __name__ == "__main__":
    main()
