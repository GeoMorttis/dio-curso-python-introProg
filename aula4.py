# Same code as in class 3 but using "while" instead of "if".
a = int(input('First quarter grade: '))
while a > 10:
    a = int(input('You entered an invalid note. Enter the first quarter grade again: '))
b = int(input('Second quarter grade: '))
while b > 10:
    b = int(input('You entered an invalid note. Enter the second quarter grade again: '))
c = int(input('Third quarter grade: '))
while c > 10:
    c = int(input('You entered an invalid note. Enter the third quarter grade again: '))
d = int(input('Fourth quarter grade: '))
while d > 10:
    d = int(input('You entered an invalid note. Enter the fourth quarter grade again: '))

media = (a + b + c + d) / 4
print('Average grade: {}'.format(media))

# nota = int(input('Enter the note: '))
# while nota > 10:
#     nota = int(input('Invalid note. Enter the correct note: '))
# print(nota)

# a = 0
# while a < 10:
#     print(a)
#     a += 1

# # Code to know the prime numbers up to a certain number.
# a = int(input('Do you want to know which are the prime numbers up to which value? '))
# for num in range(a + 1):
#     div = 0
#     for x in range(1, num + 1):
#         rest = num % x
#         #print(x, rest)
#         if rest == 0:
#             div += 1
#
#     if div == 2:
#         print(num)

# Code to know if number is prime or not.
# a = int(input('Enter a number: '))
#
# div = 0
# for x in range(1, a+1):
#     rest = a % x
#     print(a, rest)
#     if rest == 0:
#         div += 1
#
# if div == 2:
#     print('The numer {} is prime.'.format(a))
# else:
#     print('The number {} is not prime.'.format(a))

