class voterError(BaseException):
	def __init__(self,name):
		super().__init__()
print("Enter age")
age=int(input())
if age>=18:
	print("Eligbale")
else:
	try:
		raise voterError("Age not allow")
	except:
		print("not allow")
print("End")