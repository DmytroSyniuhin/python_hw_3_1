number_1 = input("Введіть перше число: ")
mathematical_operation = input("Введіть математичну дію (+, -, *, /): ")
number_2 = input("Введіть друге число: ")

if mathematical_operation == "/" and number_2 == "0":
    print("Ділення на нуль неможливе!")
elif mathematical_operation == "+":
    print(float(number_1) + float(number_2))
elif mathematical_operation == "-":
    print(float(number_1) - float(number_2))
elif mathematical_operation == "*":
    print(float(number_1) * float(number_2))
elif mathematical_operation == "/":
    print(float(number_1) / float(number_2))
