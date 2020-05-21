#n = int(input("Enter number of courses this semester: "))

last = tuple(input("Enter the acheived and total credits of last sem: ")

n = int(input("Enter number of courses in which you CAN take P*: "))

print("\nFor courses this semester in which you CANNOT take P*: ")
temp = input("Enter the COMBINED acheived and total credits: ").strip(' ').split(' ')
temp = [int(num) for num in temp]
noP = (tuple(temp)) # Stores achieved and total credits for courses you cant take P* in


print("\nFor courses in which you CAN take P*: ")
P=[]
for i in range(n):
	temp = input("Enter the acheived and total credits: ").strip(' ').split(' ')
	temp = [int(num) for num in temp]
	P.append(tuple(temp))	

temp = input("Enter the expected SGPA(out of 10) and total credits for future courses: ").strip(' ').split(' ')
temp = [int(num) for num in temp] #currently working with integer sgpa
fut = tuple(temp) #A tuple that holds expected SGPA and total future credits

All=[] # Holds all 2^n possibilities of this sem grades
for i in range(2**n):
	temp=[0, 0]
	num = bin(i).replace('0b', '') #binary form of i
	for j in num:
		if j=='1':
			temp=[x+y for x,y in zip(temp, P[j])]
	All.append(tuple(temp))

y=0
for i in All:
	temp = float(last[0] + noP[0] + i[0])
	temp/= last[1] + noP[1] + i[1]
	if temp>y:
		y=temp
