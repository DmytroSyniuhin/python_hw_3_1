number_1 = float(input("Введіть перше число: "))
mathematical_operation = input("Введіть математичну дію (+, -, *, /): ")
number_2 = float(input("Введіть друге число: "))

if mathematical_operation == "/" and number_2 == 0:
    print("Ділення на нуль неможливе!")
elif mathematical_operation == "+":
    print(number_1 + number_2)
elif mathematical_operation == "-":
    print(number_1 - number_2)
elif mathematical_operation == "*":
    print(number_1 * number_2)
elif mathematical_operation == "/":
    print(number_1 / number_2)
else:
    print("Перевірте чи вірно Ви ввели дані")
