# 1. 输入苹果的单价
from hm_05超市买苹果 import money

price_str = input("苹果的单价")

# 2.输入苹果的重量
weight_str = input("苹果的重量")

# 3.计算总金额
money = (price_str) * (weight_str)
# 1> 将价格转换成小数
price = float(price_str)

# 2> 将重量转换成小数
weight = float(weight_str)
money = price * weight
print(money)