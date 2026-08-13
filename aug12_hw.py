# Question 1 — Loan Eligibility

# Write a Python program that takes age, monthly salary, and credit score as input.

# Check whether the person is eligible for a loan when:
# i)age is at least 21,
# ii)salary is at least ₹25,000,
# iii)credit score is at least 700.
# iv)Display the final eligibility result as a Boolean value.

customer_name = input("Enter name of the customer : ")
age = int(input("Enter age : "))
monthly_salary = float(input("Enter a salary : "))
credit_score = float(input("Enter credit score : "))

if age >= 21 and monthly_salary >=25000 and credit_score >=700:
    print(customer_name,"is eligible for loan.......!")
else :
    print(customer_name,"is not eligible for loan")
print("\n")

# Question 2 — Number Analyzer

# Write a Python program that takes two integer numbers A and B.

# i)Create a Boolean expression that checks whether A is greater than B OR A is equal to B, and display the result.
# ii)Perform bitwise AND and XOR between A and B, then display both results.

A = int(input("Enter value of A : "))
B = int (input("Enter value of B : "))
print("\n")

if A > B:
    print(A,"is greater than",B)
elif A == B:
    print(A,"is equal to",B)
else :
    print(f'{A} is neither greater than {B} or nor equal to {B}')

res1 = A & B
res2 = A ^ B
print("Bitwise AND : ",res1)
print("Bitwise XOR : ",res2)
print("\n")

# Question 3 — Variable & Assignment Challenge

# Write a Python program that takes an integer num from the user.

# i)Display its value, data type, and memory ID using print(), type(), and id().
# ii)Update the same variable using a compound assignment operator so that its value becomes three times its original value,
# then display the updated value.

num = int(input("Enter a number : "))

print("Value : ",num)
print("Data Type : ",type(num))
print("Memory Address : ",id(num))

num *= 3
print("Value of number after updating : ",num)