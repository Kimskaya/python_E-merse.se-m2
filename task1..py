def convert_to_hex(number: int, base: int) -> str:
    if number == 0:
        return '0'
    
    digits = '0123456789abcdef'  # Символы для представления шестнадцатеричных цифр
    result = ''

    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number = number // base

    return result

number = int(input("Введите целое число: "))

hexadecimal = convert_to_hex(number, 16)

print(f"Шестнадцатеричное представление числа {number}: {hexadecimal}")

# конвертирование числа с помощью функции fex
hex_number = hex(number)
print(f"Шестнадцатеричное представление числа {number} при помощи функции hex: {hex_number}")

# Проверка идентичны лирезультаты, при помощью функции hex
print(hexadecimal == hex_number[2:])