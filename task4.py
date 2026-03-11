# get tuple of employ names, role and salary names frm user : eval(3)
# add new employee data (name,role,salary) : 4th
#get unique employee id from user : eval==>set

emp = eval(input("Enter the tuple(name,role,salary) :"))

new_emp = eval(input("Enter the new empl details(name,role,salary) :"))

emp =  emp + (new_emp)
print("Updated emp data",emp)

emp_id = eval(input("Enter empl unique id :"))

unq_id = set(emp_id)

print("Emp Unique ids",unq_id)