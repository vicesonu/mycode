# my calculator

def add(x, y) :
    return x + y

def subtract (x , y):
    return x-y

def multiply(x,y):
    return x * y

def divide (x,y):
    return x / y

print("Inputs.")
print("1.add")
print ("2.subtract")
print("3.multiply")
print("4.divide")

choice = input("Enter choice(1/2/3/4: ")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))

if choice == '2':
    print(num1, "-", num2, "=", subtract(num1,num2))

if choice == '3':
    print(num1,"*", num2, "=",multiply(num1,num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1,num2))


else:
    print("valid Input") 
