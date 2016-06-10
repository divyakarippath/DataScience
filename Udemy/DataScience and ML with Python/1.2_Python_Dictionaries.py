employee = {}
employee["name"] = "Divya"
employee["age"]=27
employee["salary"] = 120000
print employee["name"]

# To access elements in a safe way
print employee.get("name") #returns Divya
print employee.get("Nickname") #returns None

for elem in employee:
    print elem + ":%r" %(employee[elem])
    