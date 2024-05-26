

# 创建账户
class Account:
    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance
    # 存款
    def deposit(self, amount):
        if amount<=0:
            print("金额要大于0")
            return
        self.balance += amount
        print(f"存入:{amount}，余额:{self.balance}")
        return self.balance
    # 取款
    def withdraw(self, amount):
        if amount <= 0:
            print("金额要大于0")
            return
        if amount > self.balance:
            print("余额不足")
            return
        self.balance -= amount
        print(f"提款:{amount} ，余额:{self.balance}")
        return self.balance
    # 转账
    def transfer(self, target_account, amount):
        if amount <= 0:
            print("金额要大于0")
            return
        if amount > self.balance:
            print("余额不足")
            return
        self.balance -= amount
        target_account.balance += amount
        print(f'{self.balance} 转账成功:{amount}')
        return self.balance, target_account.balance
    # 保存格式
    def to_dict(self):
        return {
            'account_id': self.account_id,
            'balance': self.balance,
        }



