#Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь.
import math
from fractions import Fraction

a = 5
b = 7

c = math.sqrt((a**2)+(b**2))
print(c)

#упрощенный вариант
after_review_c = ((a**2)+(b**2))**0.5
print(after_review_c)


i = Fraction(1, 2)
s = i * a * b #можно упростить -> s = ( a * b ) / 2
print(float(s)) #можно и int-овое если не важно значение после запятой


#максимально простой вариант :)
after_review_s = (a * b) / 2
print(after_review_s)
