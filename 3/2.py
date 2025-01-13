def writeText(file, text):
    with open(file, "a", encoding='UTF-8') as file:
        file.write(text)


writeText("user_input.txt", "Текст")
writeText("user_input.txt"," :3")