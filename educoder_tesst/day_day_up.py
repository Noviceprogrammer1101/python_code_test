# 计算1.001的365次方，0.999的365次方
day=0.001
dayup = pow(1+day, 365)
daydown = pow(1-day, 365)
print("向上：{:.2f},向下：{:.2f}".format(dayup, daydown))