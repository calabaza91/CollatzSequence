#Collatz Sequence with exception handler


def collatz(num):
    if num % 2 == 0:
        even = num // 2
        print(even)
        return even
    if num % 2 == 1:
        odd = 3 * num + 1;
        print(odd)
        return odd

try:
    startNum = int(input('Enter number:\n'))
except ValueError:
    print('Please enter a valid integer.')

while startNum != 1:
   startNum = collatz(int(startNum))
