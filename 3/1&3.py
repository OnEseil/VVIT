def read1(file):
    try:
        with open(file, 'r', encoding='UTF-8') as text:
            content = text.read()
            return content
    except FileNotFoundError:
        print("Файл example.txt не найден")

def read2(file):
    try:
        with open(file, 'r', encoding='UTF-8') as text:
            for line in text:
                print(line.strip())

    except FileNotFoundError:
        print(f"Файл {file} не найден")

print(read1("example.txt"))
read2("example.txt")
