# program is written by Prasanna Sahera

from time import sleep

class console_calc:

    def __init__(self):
        result = 0

    def add(self, x, y):
        print(f"The sum of the given numbers {x} + {y} are : ", x + y)

    def sub(self, x, y):
        print(f"The difference of the given numbers {x} - {y} are :", x - y)

    def multiply(self, x, y):
        print(f"The Multiplication of the given numbers {x} * {y} are :", x * y)

    def divide(self, x, y):
        print(f"The Quotient of the given numbers {x} - {y} are:", x / y)

    def calc_start(self):
        print(" Hello, Welcome to the KAPSEM's Console Calculator")

        while True:
            print(" \n Press '1' for Addition")
            print(" Press '2' for Subtraction")
            print(" Press '3' for Multiplication")
            print(" Press '4' for Division")
            print(" Press '5' for Exiting out of the ATM")

            choose = int(input("\n Please, choose which operation do you want to perform: "))
            if choose == 1:
                num1 = int(input(" Please enter first number: "))
                num2 = int(input(" Please enter second number: "))
                print(" Please wait we are performing the operation... ")
                sleep(2)
                self.add(num1, num2)
            elif choose == 2:
                num1 = int(input(" Please enter first number: "))
                num2 = int(input(" Please enter second number: "))
                print(" Please wait we are performing the operation... ")
                sleep(2)
                self.sub(num1, num2)
            elif choose == 3:
                num1 = int(input(" Please enter first number: "))
                num2 = int(input(" Please enter second number: "))
                print(" Please wait we are performing the operation... ")
                sleep(2)
                self.multiply(num1, num2)
            elif choose == 4:
                num1 = int(input(" Please enter first number: "))
                num2 = int(input(" Please enter second number: "))
                print(" Please wait we are performing the operation... ")
                sleep(2)
                self.divide(num1, num2)
            elif choose == 5:
                print(" \n Thanks for using the KAPSEM's Console Calculator, hope you have a good day!!")
                break


calc = console_calc()
calc.calc_start()
