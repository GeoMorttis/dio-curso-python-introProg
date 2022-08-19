a = int(input('Enter the first value: '))
b = int(input('Enter the second value: '))
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
rest = a % b

result = ('Addition: {addition} '
          '\nSubtraction: {subtraction} '
          '\nMultiplication: {multiplication} '
          '\nDivision: {division} '
          '\nRest: {rest}'.format(addition=addition,
                                  subtraction=subtraction,
                                  rest=rest,
                                  multiplication=multiplication,
                                  division=division))

print(result)
