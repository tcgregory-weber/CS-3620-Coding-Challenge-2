# Part 1
# create function to calculate BMI
def calculate_bmi():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in m: "))
    bmi = weight / (height ** 2)
    print("Your BMI is: ", bmi)

# Part 2
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Divide by zero")
    else:
        print("Result is: ", result)


# Part 3
# Open file
def readFile():
    file = open("demo.txt", "w")
    file.write("Hello World!\n")
    file.close()
    file = open("demo.txt", "r")
    print(file.read())
    file.close()
    file = open("demo.txt", "a")
    file.write("This is a new line!")
    file.close()
    file = open("demo.txt", "r")
    print(file.read())
    file.close()

# Part 4
# Create a dictionary of 5 key-value pairs
dictionary = {
    'Book': 5.00,
    'Pen': 1.00,
    'Pencil': 0.50,
    'Eraser': 0.25,
    'Ruler': 1.50
}
def fetchPrice():
    item = input("Enter item name: ")
    if item in dictionary:
        print(dictionary[item])
    else:
        print("Item not found")


# Part 5
# For loop to print all odd numbers from 1 to 100
def oddNumbers():
    for i in range(1, 100):
        if i % 2 != 0:
            print(i)

calculate_bmi()
divide(5, 0)
readFile()
fetchPrice()
oddNumbers()