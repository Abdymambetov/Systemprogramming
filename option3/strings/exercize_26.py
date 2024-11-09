def main():
    """Main program"""
    encrypted_message = input_data()  # Ввод зашифрованного сообщения
    decrypted_message = solve(encrypted_message)  # Расшифровка сообщения
    output_result(decrypted_message)  # Вывод результата

def input_data():
    """Input problem data"""
    # Ввод зашифрованного сообщения
    return input("Введите зашифрованное сообщение: ")

def solve(encrypted_message):
    """Solver: расшифровка сообщения"""
    # Разделяем сообщение на слова, переворачиваем каждое и объединяем их обратно в строку
    return ' '.join(word[::-1] for word in encrypted_message.split())

def output_result(decrypted_message):
    """Output result"""
    # Вывод расшифрованного сообщения
    print("Расшифрованное сообщение:", decrypted_message)

if __name__ == "__main__":
    main()
