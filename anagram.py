s1=input("enter the string:")
s2=input("enter the string:")
"""    method1

s1=sorted(s1)
s2=sorted(s2)
if s1==s2:
	print("yes")
else:
	print("no")
"""
"""
	method2
if len(s1)!=len(s2):
	print("no")
else:
	c=0
	for i in s1:
		if s1.count(i)==s2.count(i):
			c=c+1
	if c==len(s1):
		print("yes")
	else:
		print("no")
"""
c=0
d1={}
d2={}
for i in s1:
	d1[i]=s1.count(i)
print(d1)
print()
for i in s2:
	d2[i]=s2.count(i)
print(d2)
if len(s1)!=len(s2):
	print("no")
else:
	for k in d1.keys():
		if k in d2 and d1[i]==d2[i]:
			c=c+1
	if c==len(d1):
		print("yes")
	else:
		print("no")
