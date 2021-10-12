# 入力受け取り
a, b, x = map(int,input().split())
# 引数に与えられた整数が購入できるかどうかの判定
def is_able_to_buy_target(target):
    return a * target + b * len(str(target)) <= x

def binary_search(left, right):
    # your code here!!

print(binary_search(0, 1 + 10**9))