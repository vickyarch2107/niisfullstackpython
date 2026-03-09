class Student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r
		self.mark=m
	def show(self):
		print("My name=",self.name)
		print("My rollno=",self.roll)
		print("My mark=",self.mark)
s1=Student("Muna",1,90.50)
s2=Student("Kuna",2,80.50)
s1.show()
s2.show()