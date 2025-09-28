# 1.定义字符串变量name，输出 我的名字是小明，请多关照。
name = "大xiao明"
print("我的名字叫%s，请多多关照" % name)
# 2.定义整数变量 student_no, 输出 我的学号是000001
student_no = 20321311
print("我的学号是%06d" % student_no)
# 3.定义小数price,weight,money,
# 输出 苹果单价9.00元/斤，购买了5.00斤，需要支付45元。
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价%.2f元/斤，购买了%.3f斤，需要支付 %.2f 元" % (price, weight, money))
# 4.定义一个小数scale,输出数据比例是10.00%
scale = 0.88
print("输出数据比例是%.2f%%" % (scale * 100))