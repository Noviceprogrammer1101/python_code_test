#这个项目是我个人用于学习python记录的一些联系代码
## educoder_tesst
educoder_tesst是我在educoder练习闯关的代码,里面包含了: 
 
### Branching_structure.py
 英制单位英寸和公制单位厘米互换  
 百分制成绩转换为等级制成绩  
 幸运的基督徒
 
### day_day_up.py
计算1.001的365次方，0.999的365次方 
 
 
### list_tuple_dict
列表元组的联系
 
### variable_and_simple_type.py
简单变量的练习
### loop_structrue.py
循环结构的联系
### function_module.py
模块和函数的联系
### 面向对象基础
1.数字时钟  
2.两点之间的距离


### 面向对象进阶
里面是一个简易的工资结算系统


### 继承
继承1  
继承2  
继承3  

### 随堂测试-继承
这是我课堂上的关于继承的课堂上机练习


### 
#一些知识总结
##列表

###加法，乘法，in运算
1.两个列表相加就是包含两个列表元素的总和  
2.相乘就是列表重复n次
3.in 运算就是判断列表中是否存在该元素，返回是True或者False


###序列封包和解包
封包：把多个值赋给一个变量时，把这些值封装成元组

解包：将序列（列表或者元组）直接赋给多个变量时，序列中的元素依次赋给每个变量

###增加元素
append()函数：在尾部插入
insert()函数：在指定位置插入
extend()函数：将一个列表追加到列表的尾部


###删除元素
del()函数：根据所以删除列表中的一个元素或者一段
remove():根据列表中的元素删除列表中的某个元素
clear():清空列表所有的元素


###置逆和排序
reverse():将元素置逆
sort():将列表中的元素从小到大排序（默认是从小到大，需要添加参数reverse="true")

###弹出元素
pop():将列表作为栈，实现出栈操作（入栈可以用上面提到的方法append()
pop(0):将列表作为队列，实现出队操作（入队用append())
pop(i),将下标为i的元素删除


###浅拷贝和深拷贝
浅拷贝：list.copy()和copy.copy()
当列表中只有不可变序列的时候，复制的列表被修改了，原列表不会改变
例如：list[1,2,3]这种内含字符
当列表中有可变序列（元组或者列表），复制的列表被修改了，原列表的可变序列部分就会被修改

##元组
元组是不可变的序列

###元组的创建
未完成
###列表和元组的转换

###
###其他
dir()函数可以查看对象内所有的属性和方法

### 300_cases_of_python_programming
这个文件夹存放的是python的三百个例子