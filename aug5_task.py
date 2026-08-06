                                # 1.IDENTITY CARD

name = input("Enter name of the student : ")
age = int(input("Enter age of the student : "))
city = input("Enter city of the student : ")
dob = input("Enter DOB of the student : ")
college = input("Enter college of the student : ")
blood_g = input("Enter blood group of the student : ")

print("-----------STUDENT IDENTITY CARD-----------")
print("\n")
print("Name : ",name)
print("Age : ",age)
print("City : ",city)
print("DOB : ",dob)
print("College : ",college)
print("Blood Group :",blood_g)
print("\n")

                                # 2.MEMORY DETECTION

v1 = int(input("Enter a First number : "))
v2 = int(input("Enter a Second number : "))
v3 = int(input("Enter a Third number : "))

print("\n")
print(f'The memory location of the variable {v1} is {id(v1)}')
print(f'The memory location of the variable {v2} is {id(v2)}')
print(f'The memory location of the variable {v1} is {id(v3)}')
print("\n")
