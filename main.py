def main():
    nf = NumberFactory()
    result = nf.get_number()
    user_num = iter(result['user_numbers'])
    computer_num = iter(result['computer_numbers'])
    print(f'   {next(user_num)}')
    for i in range(2):
        print(f'+ {next(user_num):03}')
        print(f'+ {next(computer_num):03}')
    print('------')
    print(result['result'])

class NumberFactory:
    def __init__(self):
        self.result = 0
        self.number_len = 0
        self.user_numbers = []
        self.computer_numbers = []
    def get_number(self):
        self.number_len += 1
        if self.number_len == 4:
            print('hame adad ra jam konid va hasel ra bebinid')
            return {'result':self.result,'user_numbers':self.user_numbers,'computer_numbers':self.computer_numbers}
        number = input(f'adade {self.number_len} ravared konid: ')
        self.user_numbers.append(int(number))
        if self.result == 0:
            self.compute_result()
            return self.get_number()
        else:
            self.get_computer_number()
            return self.get_number()



    def compute_result(self):
        self.result = 2000 + self.user_numbers[0] - 2
        print(f'natije {self.result} khahad bood!')

    def get_computer_number(self):
        self.computer_numbers.append(999 - self.user_numbers[-1])
        print(f'adad man: {self.computer_numbers[-1]}')



if __name__ == '__main__':
    main()
