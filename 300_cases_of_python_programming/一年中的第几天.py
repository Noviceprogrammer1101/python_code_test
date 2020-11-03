def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    #        请在此处添加代码       #
    # *************begin************#
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True  # 整百年能被400整除的是闰年
            else:
                return False
        else:
            return True  # 非整百年能被4整除的为闰年
    else:
        return False
        # **************end*************#


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    #        请在此处添加代码       #
    # *************begin************#
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

    days = days_of_month[is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days[index]
    return total + date
    # 1800301532韦柳栌
    # **************end*************#


print(which_day(1981, 12, 31))