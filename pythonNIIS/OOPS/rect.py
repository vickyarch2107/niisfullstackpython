class Rectangle:
	def __init__(self,L,B):
		self.length=L
		self.breadth=B
	def show(self):
		print("Length=",self.length)
		print("Length=",self.length)
	def area(self):
		return self.length*self.breadth
	def perimeter(self):
		return 2*(self.length+self.breadth)
print("Enter Length and Breadth")
r1=Rectangle(float(input()), float(input()))
print("Area",r1.area())
print("Perimeter",r1.perimeter())