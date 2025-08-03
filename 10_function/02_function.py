#more than one return statement 
def formate_string(f_name,l_name):
    if f_name=="" or l_name=="":
        return print("please inter all fields")
    
    formate_f_name=f_name.title()
    formate_l_name=l_name.title()

    return f"Result: {formate_f_name} and the {formate_l_name}"


f_name= input("enter the value of the firstname")
l_name=input("enter the value of the last name")
fullName = formate_string(f_name,l_name)
print(fullName)
