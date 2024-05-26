import csv
from account import Account
# 银行类
class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}
    # 新增账户
    def add_account(self, account):
        self.accounts[account.account_id] = account
        print(f'新增用户:{account.account_id}')
    # 取已有账户
    def get_account(self,account_id):
        print(f"get_account :{self.accounts.get(account_id)}")
        return self.accounts.get(account_id)
    # 状态保存到文件
    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['account_id', 'balance']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for account in self.accounts.values():
                writer.writerow(account.to_dict())

    def load_from_csv(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:

                account_id = row['account_id']
                balance = float(row['balance'])
                account = Account(account_id, balance)
                self.add_account(account)


    def banking(self, account_id, type, amount,target_account):
        self.load_from_csv('account_book.csv')
        account = self.get_account(account_id)
        if account is None:
            account = Account(account_id)
            self.add_account(account)
        if type == 'D': # deposit
            account.deposit(amount)
        elif type == 'W': # withdraw
            account.withdraw(amount)
        elif type =='T': # transfer
            if self.get_account(target_account)==None:
                print(f"没有该账户{target_account}")
                return
            account.transfer(self.get_account(target_account),amount)
        self.save_to_csv('account_book.csv')