class Book:
	def __init__(self, title, author, year):
		self.title = title
		self.author = author
		self.year = year
	def get_info(self):
		return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

book = Book(input("Название"), input("Автор: "), input("Год издания: "))
print(book.get_info())
