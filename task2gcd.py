'''Напишите программу, которая принимает две строки вида "a/b" -
дробь с числителем и знаменателем. Программа должна возвращать
сумму и произведение* дробей. Для проверки своего кода используйте
модуль fractions.'''

from fractions import Fraction
from math import gcd

#Для нахождения НОД используем функцию gcd из модуля math

def SokrDr(x,y):
    '''Функция для сокращения дроби'''
    return x//gcd(x,y), y//gcd(x,y)

    
a,b = [int(x) for x in input("Введите первую дробь в виде a/b:  ").split('/')] #числитель и знаменатель дроби a/b
c,d = [int(x) for x in input("Введите вторую дробь в виде a/b:  ").split('/')] #числитель и знаменатель дроби c/d

sum_chisl,sum_znam = SokrDr(a*d+b*c,b*d) #числитель и знаменатель суммы дробей

pr_chisl,pr_znam = SokrDr(a*c,b*d)       #числитель и знаменатель произведения дробей
print('Вычисление без использования модуля fractions:')
print(f'{a}/{b} + {c}/{d} = {sum_chisl}/{sum_znam}')
print(f'{a}/{b} * {c}/{d} = {pr_chisl}/{pr_znam}')

print('Вычисление с использованием модуля fractions:')
print(f'{a}/{b} + {c}/{d} = {Fraction(a,b)+Fraction(c,d)}')
print(f'{a}/{b} * {c}/{d} = {Fraction(a,b)*Fraction(c,d)}')