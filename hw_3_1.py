is_yes = "y"
result = None
tuple_operators = ("+", "-", "/", "*")

while is_yes == "y":

    number_1 = input("Введіть перше число: ")
    mathematical_operation = input("Введіть математичну дію (+, -, *, /): ")
    number_2 = input("Введіть друге число: ")
    is_digit = number_1.isdigit() and number_2.isdigit

    if mathematical_operation == tuple_operators[2] and float(number_2) == 0:
        result = "Ділення на нуль неможливе!"
    elif mathematical_operation == tuple_operators[0] and is_digit:
        result = float(number_1) + float(number_2)
    elif mathematical_operation == tuple_operators[1] and is_digit:
        result = float(number_1) - float(number_2)
    elif mathematical_operation == tuple_operators[2] and is_digit:
        result = float(number_1) / float(number_2)
    elif mathematical_operation == tuple_operators[3] and is_digit:
        result = float(number_1) * float(number_2)
    else:
        result = "Перевірте чи вірно Ви ввели дані"
    print(result)
    is_yes = input('Чи бажаєте Ви продовжити? Якщо так - натисніть "y". Якщо ні - введіть будья-який інший символ: ')
