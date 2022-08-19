a = int(input('First quarter grade: '))
if a > 10:
    a = int(input('You entered an invalid note. Enter the first quarter grade again: '))
b = int(input('Second quarter grade: '))
if b > 10:
    b = int(input('You entered an invalid note. Enter the second quarter grade again: '))
c = int(input('Third quarter grade: '))
if c > 10:
    c = int(input('You entered an invalid note. Enter the third quarter grade again: '))
d = int(input('Fourth quarter grade: '))
if d > 10:
    d = int(input('You entered an invalid note. Enter the fourth quarter grade again: '))

media = (a + b + c + d) / 4
print('Average grade: {}'.format(media))

# if a <= 10 and b<= 10 and c <= 10 and d <=10:
#     print('Average grade: {}'.format(media))
# else:
#     print('An invalid note was entered!')

# a = int(input('Enter the first value: '))
# b = int(input('Enter the second value: '))
# rest_a = a % 2
# rest_b = a % 2
#
# if rest_a == 0 or not rest_b > 0:
#     print('At least one even number has been entered!')
# else:
#     print('No even number has been entered!')


# a = int(input('First value: '))
# b = int(input('Second value: '))
# c = int(input('Third value: '))
#
# if a > b:
#     print('The biggest number is {}'.format(a))
# elif b > a and b > c:
#     print('The biggest number is {}'.format(b))
# else:
#     print('The biggest number is {}'.format(c))
#
# print('Finished program')
