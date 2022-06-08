# The code has been Tested and debugged!
#Features:
# 1. Creating Multiple bank accounts as per wish
# 2. Credit Card and Debit card both are supported
# 3. Authentication using Machine generated Account Number and Custom PIN
# 4. Detailed Transaction Log
# 5. Login to access bank accounts using reference's to objects(bankAccounts)
import getpass
from datetime import datetime

# This dictionary contains {account numbers:bank accounts} and will be used for authentication purposes
accounts = {}


class genericBank:
    accountNumber = 1000

    def __init__(self, name, gender, phone, passport, balance, spentCredits, accNum, pin):
        self.pin = int(pin)
        self.name = name
        self.phone = int(phone)
        self.accNum = int(accNum)
        self.gender = gender
        self.balance = int(balance)
        self.initBalance = balance
        self.passport = passport
        self.initLimit = int(spentCredits)
        self.spentCredits = 0
        self.transactionHistory = ''

    @classmethod
    def createAccount(cls):
        details = input(
            'Enter Details in Format Name/Gender/PhoneNo/PassportNo/InitalBalance/CreditLimit  --> ')
        sec = getpass.getpass(
            'Set Pin (Pin is Hidden for Safety Purposes and Keep Pin Safe & Secure!) ->')
        string = details + '/' + str(cls.accountNumber) + '/' + sec
        print(
            f'Thankyou For Opening Bank Account.For Login use Account Number {cls.accountNumber} and PIN')
        cls.accountNumber += 1
        return cls(*string.split('/'))

    def addTransaction(self, acc, type, valid, amt):
        now = datetime.now()
        dt_string = now.strftime('%d/%m/%Y %H:%M:%S')
        if acc == 'credit':
            self.transactionHistory = dt_string + ' Credit Card: ' + type + \
                ' of ' + str(amt) + ' was ' + valid+'! ' + self.printCredit() + '\n' + \
                self.transactionHistory
        elif acc == 'saving':
            self.transactionHistory = dt_string + ' Saving Account: ' + type + \
                ' of ' + str(amt) + ' was ' + valid + '! ' + self.printDebit() + '\n' + \
                self.transactionHistory

    def printCredit(self):
        return f'Available Credit : {self.initLimit - self.spentCredits}'

    def printDebit(self):
        return f'Saving Account Balance : {self.balance}'

    def getCurrentCredit(self):
        return self.initLimit - self.spentCredits

    def creditAccount(self):
        while True:
            print('\n', self.printCredit())
            x = input(
                '\nEnter your Choice 1. Withdraw Credit  2. Repay Credit Card Bill  3. Show Credit Limit  4.Logout Current Account  ->')
            if x == '1':
                amt = int(input('Enter Amount to Withdraw:'))
                if amt <= self.getCurrentCredit():
                    self.spentCredits += amt
                    print('Successfull withdrawn')
                    self.addTransaction(
                        'credit', 'withdrawal', 'succesfull', amt)
                else:
                    print('Insufficient Credit ')
                    self.addTransaction(
                        'credit', 'withdrawal', 'unsucessfull', amt)
            elif x == '2':
                if self.getCurrentCredit() == self.initLimit:
                    print('No Bill due.')
                else:
                    print(f'Bill Generated : Due ₹{self.spentCredits}')
                    amt = 0
                    while not int(amt) in range(1, self.spentCredits + 1):
                        amt = int(input(
                            f'Pay in Full: {self.spentCredits} or Custom Ammount(less <=Total Limit) -> '))
                        break
                    self.spentCredits -= amt
                    self.addTransaction(
                        'credit', 'repayment', 'succesfull', amt)
                    print(
                        f'Paid: {amt}, Remaining Due: {self.spentCredits}, Available: {self.getCurrentCredit()} ')
            elif x == '3':
                print(
                    f'Credit info:- {self.getCurrentCredit()}/{self.initLimit}')
            elif x == '4':
                break

    def savingAccount(self):
        while True:
            print('\n', self.printDebit())
            x = input(
                '\nWelcome  1. Deposit Money  2. Withdraw Money  3. Show Balance  4. Logout Saving Account-> ')
            if x == '1':
                amt = int(input('Enter The amount you want to deposit-> '))
                self.balance += amt
                self.addTransaction(
                    'saving', 'deposition', 'succesfull', amt)
            elif x == '2':
                amt = int(input('Enter the Amount you want to withdraw-> '))
                if amt <= self.balance:
                    self.balance -= amt
                    self.addTransaction(
                        'saving', 'withdrawal', 'succesfull', amt)
                else:
                    print('Insufficient Balance')
                    self.addTransaction(
                        'saving', 'withdrawal', 'unsuccesfull', amt)
            elif x == '3':
                print(self.printDebit())
            elif x == '4':
                break

    def printDetails(self):
        print()
        print('Bank Account Details         : ')
        print('Customer Account Number is   : ', self.accNum)
        print('Customer Name is             : ', self.name)
        print('Customer Gender is           : ', self.gender)
        print('Customer Phone Number is     : ', self.phone)
        print('Customer Passport Number is  : ', self.passport)
        print('Customer Credit Card limit is : ', self.initLimit)
        print('Customer Saving Account balance is : ',self.initBalance, end='\n\n')


def addAccount(cls):
    accounts[cls.accNum] = cls


def login():
    acc = int(input('Enter Account Number-> '))
    pss = getpass.getpass('Enter Pin (Pin is not shown for safety reasons)-> ')
    if acc in accounts.keys():
        if accounts.get(acc).pin == int(pss):
            return accounts.get(acc)
    return False


if __name__ == '__main__':

    while True:
        x = input(
            '\nWelcome to Generic Bank\n  1.Login\n  2.Create Account\n  3.Exit\n--> ')
        if x == '1':
            referencePointer = login()
            if referencePointer:
                while True:
                    r = input(
                        f'\nWelcome {referencePointer.name}\n 1. Credit Account\n 2. Debit Account\n 3. Transaction History\n 4. Show Account Details\n 5.BackToLogin-->\n ')
                    if r == '1':
                        referencePointer.creditAccount()
                    elif r == '2':
                        referencePointer.savingAccount()
                    elif r == '3':
                        print(referencePointer.transactionHistory)
                    elif r == '4':
                        referencePointer.printDetails()
                    elif r == '5':
                        break
            else:
                print('Account Not Found\n')
        elif x == '2':
            referencePointer = genericBank.createAccount()
            addAccount(referencePointer)
        elif x == '3':
            break
# END
