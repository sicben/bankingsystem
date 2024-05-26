from bank import Bank
if __name__ == '__main__':
    # 创建一个银行对象
    bank = Bank("测试银行")

    # 参数： banking(原账户，操作类型[D,W,T],金额，目标账户（转账使用，其他状态可以为None或‘’）））
    bank.banking('001','D',10,'')   #deposit
    bank.banking('001','W',10,'')   #withdrawal
    bank.banking('001','T',10,'002')   #transfer

    # 当 金额为 小于等于0 时 ，
    bank.banking('001','D',0,'')   #deposit
    bank.banking('001','W',-10,'')   #withdrawal
    bank.banking('001','T',-10,'002')   #transfer

    # 提款转账 超过 余额时
    bank.banking('001', 'W', 100000, '')  # withdrawal
    bank.banking('001', 'T', 100000, '002')  # transfer

   # 当提款或转账没有 没有该账户时，提示没该账户
    bank.banking('009', 'T', 100000, '008')  # withdrawal/transfer
