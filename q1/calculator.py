class MyCalculator:
    def __init__(self, numberOne, numberTwo):
        self.Uno = numberOne
        self.Dos = numberTwo

    def addition(self):
        total = self.Uno + self.Dos
        print(f"The sum between {self.Uno} and {self.Dos} is {total}.")

    def subtraction(self):
        total = self.Uno - self.Dos
        print(f"The difference between {self.Uno} and {self.Dos} is {total}.")

    def multiplication(self):
        total = self.Uno*self.Dos
        print(f"The product between {self.Uno} and {self.Dos} is {total}.")

    def division(self):
        total = self.Uno/self.Dos
        print(f"The quotient between {self.Uno} and {self.Dos} is {total}.")

nOne = int(input("Enter a number: "))
nTwo = int(input("Enter another number: "))

MC = MyCalculator(nOne, nTwo)

MC.addition()
MC.subtraction()
MC.multiplication()
MC.division()