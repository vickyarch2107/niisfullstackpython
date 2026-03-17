from abc import *
class Shape(ABC):
	def __init__(self,name):
		self.name=name
	@abstractmethod
	def peremeter(self):
		pass
class Rectangle(Shape):
	def __init__(self,n,L,B):
		super().__init__(n)
		self.L=L
		self.B=B
	def peremeter(self):
		return 2*(self.L+self.B)
class Square(Shape):
	def __init__(self,n,L):
		super().__init__(n)
		self.L=L
	def peremeter(self):
		return 4*self.L
r1=Rectangle("rect",5,7)
print(r1.peremeter())
s1=Square("squ",7)
print(s1.peremeter())
		
