"""class Sical:
	def __init__(self,p,t,r):
		self.p=p
		self.time=t
		self.rate=r
	def show(self):
		print("Enter principle=",self.p)
		print("Enter time=",self.time)
		print("Enter rate=",self.rate)
	def sical(self):
		return self.p*self.time*self.rate/100
s1=Sical(1000,2,5.0)
s1.show()
print("Simple Intrest=",s1.sical())"""







#User input
class Sical:
	def __init__(self,p,t,r):
		self.p=p
		self.time=t
		self.rate=r
	def show(self):
		print("Enter principle=",self.p)
		print("Enter time=",self.time)
		print("Enter rate=",self.rate)
		#print("Simple Intrest=",self.sical())
	def sical(self):
		return self.p*self.time*self.rate/100
print("Enter Principle, time and rate")
#s1=Sical(float(input()),float(input()),float(input()))
pr=float(input())
t=float(input())
r=float(input())
s1=Sical(pr,t,r)
s1.show()
print("Simple Intrest=",s1.sical())









"""class Sical:
	def __init__(self,p,t,r):
		self.principle=p
		self.time=t
		self.rate=r
		self.si=p*t*r/100
	def show(self):
		print("Enter principle=",self.principle)
		print("Enter time=",self.time)
		print("Enter rate=",self.rate)
		print("Simple Intrest=",self.si)
s1=Sical(1000,2,5.0)
s1.show()"""