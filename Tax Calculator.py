#Programmer: Sachorra Douglas
#Date:11/13/2024
#Task:Create a Tax Calculator in Python

#Pseudocode
#Display "Tax Calculator" (message function).
#Prompt user to enter their name, number of dependents, and gross income (user_input fucntion)
#Calculate taxable income and income tax based on the following rules:
###Deduct $10,000 from gross income as a standard deduction
###Deduct an additional $2,000 for each dependent
###Taxable income = Gross income - (Standard deduction + Additional deduction)
###Income tax = Taxable income * 0.2
#Display name, taxable income, and income tax (cal_tax function)

def message():
    print("Tax Calculator")

def user_input():
    #Prompt the user for name, number of dependents & gross income
    name = input("Enter your name: ")
    dependents = int(input("Enter number of dependents: "))
    gross_income = float(input("Enter gross income: $"))
    return name, dependents, gross_income

def cal_tax(name, dependents, gross_income):
    #Constants for tax calculations
    standard_deductions = 10000
    dependent_deduction = 2000 * dependents
    total_deductions = standard_deductions + dependent_deduction #Total deductions for both dtandard and dependents
    taxable_income = gross_income - total_deductions
    tax_rate = 0.2
    income_tax = taxable_income * tax_rate

    #Display output messages in a clear format
    print(f"\nHello {name}") #Personalized greetung displayed right after the name input
    print(f"You have entered {dependents}")
    print(f"You have entered a gross income of: ${gross_income:.2f}")
    print(f"{name}, your taxable income is: ${taxable_income:.2f}")
    print(f"And your income tax is: ${income_tax:.2f}")

if __name__ == "__main__":
    #Call the functions in sequence
    message()
    name, dependents, gross_income = user_input()
    cal_tax(name, dependents, gross_income)
    
