class Circle:
	def __init__(self, radius):
		self.radius = radius
	def get_radius(self):
		return self.radius
	def set_radius(self, new_radius):
		self.radius = new_radius

circle = Circle(int(input("Введите радиус: ")))
print(circle.get_radius())
circle.set_radius(int(intput("Новый радиус: ")))
print(circle.get_radius())
