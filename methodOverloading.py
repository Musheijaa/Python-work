class Calculator:
    def add(self, a, b=0, c=0):
        print("Sum:", a + b + c)

# Example
calc = Calculator()
calc.add(2, 3)       # Sum: 5
calc.add(2, 3, 4)    # Sum: 9
