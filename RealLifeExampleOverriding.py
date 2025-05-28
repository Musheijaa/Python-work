class BankAccount:
    def withdraw(self, amount):
        print(f"Withdrawing {amount} from account")

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print(f"Checking overdraft... Cannot withdraw {amount} if funds are insufficient.")

sa = SavingsAccount()
sa.withdraw(100)
