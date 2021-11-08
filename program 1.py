def getNameAgeAddress():
    Name = input("Enter name: ")
    Age = int(input("Enter age: "))
    Address = input("Enter address: ")
    return Name, Age, Address

def display(name_, age_, address_):
    print (f'Hi, my name is {name_}. I am {age_} years old and I live in {address_}.')

name, age, address = getNameAgeAddress() 

display(name, age, address)
