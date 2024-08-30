harf = input('harf kiriting: ') *5
print(harf)

number1 = int(input('Son kiritng: '))
number2 = int(input('Son kiritng: '))

print(f'{number1} - {number2} = {number1 - number2}')
print(f'{number1} + {number2} = {number1 + number2}')
print(f'{number1} / {number2} = {number1 / number2}')
print(f'{number1} * {number2} = {number1 * number2}')
print(f'{number1} // {number2} = {number1 // number2}')
print(f'{number1} ** {number2} = {number1 ** number2}')

number3 = int(input('Katta son kiritng: '))
number4  = int(input('Kichik son kiritng: '))

bolish = number3 / number4

print(f"Ceil:{bolish.__ceil__()}")
print(f"Floor:{bolish.__floor__()}")







