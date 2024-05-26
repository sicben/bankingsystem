from bank import Bank
if __name__ == '__main__':
    # 创建一个银行对象
    bank = Bank("测试银行")
    bank.banking('001','T',10,'002')   #参数： banking(原账户，操作类型[D,W,T],金额，目标账户（转账使用，其他状态可以为None或‘’）））
