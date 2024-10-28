import argparse
from tool import *

loginDdx = 0
loginMax = 5

class Login(BaseScript):
    def __init__(self):
        super().__init__()

    def loginout(self):
        print("run")
        self.login()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OF Generate')
    parser.add_argument('-ir', '--idxArray', required=False, default='0', type=str)
    args = parser.parse_args()
    indexArr = args.idxArray.split(',')

    def func(idx):
        DaTi(idx=idx).do()

    if len(indexArr) != 1:
        for each in indexArr:
            func(int(each))
    else:
        func(int(indexArr[0]))


def login():
    print("login")