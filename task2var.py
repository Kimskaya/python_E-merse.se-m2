from fractions import Fraction

# aункция для получения наибольшего общего делителя для сокращения дроби
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

fraction_str1 = input("Введите первую дробь в ввиде a/b: ")
fraction_str2 = input("Введите вторую дробь в ввиде a/b: ")

# разделение строки на числитель и знаменатель
numerator1, denominator1 = map(int, fraction_str1.split("/"))
numerator2, denominator2 = map(int, fraction_str2.split("/"))

# сумма
sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
sum_denominator = denominator1 * denominator2
# наибольший общеий делитель для сокращения дробей
gcd_sum = gcd(sum_numerator, sum_denominator)

# произведение
product_numerator = numerator1 * numerator2
product_denominator = denominator1 * denominator2
# наибольший общеий делитель для сокращения дробей
gcd_product = gcd(product_numerator, product_denominator)

# cокращение дроби
sum_numerator_result = sum_numerator // gcd_sum
sum_denominator_result = sum_denominator // gcd_sum 

product_numerator_result = product_numerator // gcd_product
product_denominator_result = product_denominator // gcd_product

# проверка- если знаменатль равен 1, в результате выдает не дробь а целое число
if sum_denominator_result == 1:
    print(f"Сумма дробей: {sum_numerator_result}")
else:
    print(f"Сумма дробей: {sum_numerator_result}/{sum_denominator_result}")

if product_denominator_result == 1:
    print(f"Произведение дробей: {product_numerator_result}")
else:
    print(f"Произведение дробей: {product_numerator_result}/{product_denominator_result}")


#  вычисления суммы и произведения дробей с помощью функции Fraction
myfraction1 = Fraction(numerator1,denominator1)
myfraction2 = Fraction(numerator2,denominator2)

sum_fract = myfraction1 + myfraction2
print(f"Сумма дробей, с использованием функции Fraction: {sum_fract}")

product_fract = myfraction1 * myfraction2
print(f"Произведение дробей, с использованием функции Fraction: {product_fract}")