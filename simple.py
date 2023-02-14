import time


def main():
    print('hi!')
    first_number = input('please enter a three-digit number: ')
    # if isinstance(first_number,int) and len(str(first_number)) == 3:
    # else:
    result = int(first_number) - 2 + 2000
    input(f'your result would be {result}. press enter key.')
    second_number = input(f'please another three-digit number: ')
    computer_second_number = 999 - int(second_number)
    input(f'my suggestion is {computer_second_number} press enter key.')
    three_number = input(f'please enter last tree-digit number: ')
    computer_three_number = 999 - int(three_number)
    input(f'my suggestion is {computer_three_number} press enter key.')
    input(f'sum all numbers and you see the result would be {result} press enter key.')
    print(f'  {int(first_number):03}')
    time.sleep(1)
    print(f'+ {int(second_number):03}')
    time.sleep(1)
    print(f'+ {int(computer_second_number):03}')
    time.sleep(1)
    print(f'+ {int(three_number):03}')
    time.sleep(1)
    print(f'+ {int(computer_three_number):03}')
    time.sleep(1)
    print(f'-----------')
    time.sleep(1)
    print(f'{result}')
