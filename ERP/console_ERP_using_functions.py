employees = {} #Empty dictionary
def add_emp():
	serial_no = input("\tEnter serial No ")
	if serial_no not in employees.keys():
		e_id = input("\tEnter emp id ")
		e_name = input("\tEnter emp name ")
		e_age = int(input("\tEnter emp age "))
		e_gender = input("\tEnter emp gender ")
		e_place = input("\tEnter emp place ")
		e_sal = input("\tEnter emp salary ")
		e_comp = input("\tEnter emp previous company ")
		e_doj = str(input("\tEnter emp joining date as dd/mm/yyyy "))
		temp ={
		"e_id":e_id,
		"e_name":e_name,
		"e_age":e_age,
		"e_gender":e_gender,
		"e_place":e_place,
		"e_sal":e_sal,
		"e_comp":e_comp,
		"e_doj":e_doj
		}
		employees[serial_no] = temp
	else:
		print("\tSerial No already Taken")
		
def delete_emp():
	serial_no = input("\tEnter serial no")
	if serial_no not in employees.keys():
		print("\tWrong serial No")
	else:
		del employees[serial_no]
		
def search_emp():
	name = input("\tEnter name")
	found = False #flag = False
	for i in employees.values():
		if i["e_name"] == name: # find name
			print(f"\t{i['e_id']} | {i['e_name']} | {i['e_age']} | {i['e_gender']} | {i['e_place']} | {i['e_sal']} | {i['e_comp']} | {i['e_doj']} ")
			found = True
			break

	if found == False :
		print("\tNot found")
			

def change_emp():
	serial_no = input("\tEnter serial no.")
	if serial_no not in employees.keys():
		print("\tWrong serial no")
	else:
		employees[serial_no]['e_name'] = input("\tEnter new emp name")
		employees[serial_no]['e_age'] = input("\tEnter new emp age")
		employees[serial_no]['e_gender'] = input("\tEnter new emp gender")
		employees[serial_no]['e_sal'] = input("\tEnter new emp salary")

def display_emp():			
	for serial,emp in employees.items():
		print(f"\t{serial} | {emp['e_id']} | {emp['e_name']} | {emp['e_age']} | {emp['e_gender']} | {emp['e_place']} | {emp['e_sal']} | {emp['e_comp']} | {emp['e_doj']}")

def main_menu():
	print("1. Add employee")
	print("2. Delete employee")
	print("3. Search employee by name")
	print("4. Change a employee data in the list")
	print("5. Display all student") 
	print("6. exit")



while True:
	
	main_menu()
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add employee
		add_emp()
	
	elif ch == 2:
		#Delete employee
		delete_emp()
		
	elif ch == 3:
		#Search employee
		search_emp()
		
	elif ch == 4:
		#Change a employee data in the list
		change_emp()
	elif ch == 5:
		#Display employee
		display_emp()

	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")


