#Mini project console ERP system
emp_data = []
while True:
	print("Select any option")
	print("1.Add Employee")
	print("2.Delete Employee")
	print("3.Search Employee")
	print("4.Change Employee data")
	print("5.Display Employeee details")
	print("6.EXIT")
	ch = int(input("Enter the Choice: "))
	if ch is None:
		print("No employees in the list")
	elif ch == 1:
		#Add employee
		name = input("Enter name of the employee to add: ")
		emp_data.append(name)
	elif ch == 2:
		#Delete employee
		print(emp_data)
		name = input("Enter the name of the employee to delete: ")
		emp_data.remove(name)
	elif ch ==3:
		#Search employee
		name = input("Enter the name of the employee to search: ")
		if name in emp_data:
			print(name +" is in the list")
		else:
			print(name +" is not in the list")
	elif ch == 4:
		#Change the employee data
		name = input("Enter the employee name to change: ")
		pos = emp_data.index(name)
		new_name = input("Enter new employee name: ")
		emp_data[pos] = new_name 
	elif ch == 5:
		#Display eemployee details
#		print(emp_data)
		for i in range(0,len(emp_data)):
			print(i+1,".",emp_data[i])
			i=i+1
	elif ch == 6:
		#To exit
		break
	else:
		print("Invalid choice")
