def main():
    """Main program"""
    file_path = input_data()  # Путь к файлу
    consonants = solve(file_path)  # Нахождение всех звонких согласных
    output_result(consonants)  # Вывод результата

def input_data():
    """Input problem data"""
    # Ввод пути к файлу
    return input("Введите путь к файлу: ")

def solve(file_path):
    """Solver: нахождение звонких согласных букв"""
    # Звонкие согласные буквы
    voiced_consonants = set("бвгджзклмнпрстфхцчшщ")
    found_consonants = set()  # Множество для найденных букв

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()  # Чтение текста из файла в нижнем регистре

        # Проходим по всем словам и добавляем звонкие согласные в множество
        for word in text.split():
            for char in word:
                if char in voiced_consonants:  # Проверяем, является ли символ звонкой согласной
                    found_consonants.add(char)

    except FileNotFoundError:
        print(f"Файл по пути {file_path} не найден.")
        return set()

    return found_consonants

def output_result(consonants):
    """Output result"""
    if consonants:
        print("Звонкие согласные буквы, встречающиеся в тексте:")
        # Сортировка найденных букв по алфавиту и вывод
        print(" ".join(sorted(consonants)))
    else:
        print("Звонкие согласные буквы не найдены.")

if __name__ == "__main__":
    main()
