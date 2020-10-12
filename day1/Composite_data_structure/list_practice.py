"""
序列是一种包含多项的数据结构，类型包括了字符串，列表和元组，分为可以变和不可以变
可变：列表
不可以变：元组和字符串


"""
# 创建列表
# list1=[1,3,5,7,100]
# tuple=(2,4,6,8)
# list1[-3]=9
# print(list1)


# 列表和元组中的数据项可以不同
# list2=[512,3,9,'p',(3,9),[3.9]]
# 列表中的可以包含字符，元组，列表

# 元组中可以包含字符，元组，列表
# tuple2=(512,3,9,'p',(3,9),[3.9])
# list2[3]=[1,2]


# 列表通用方法
#   1.通过索引访问
# list2=[512,3,9,'p',(3,9),[3.9]]
# print(list2[3])
# print(list2[4][0])



# 切片：就是通过索引来获取序列的某一段
# list3=[1,2,3,4,5,6,7,8,9]
# print(list3[3:7])
#
# list4=list3[:]
# print(list4)
#
# tuple3 = ('p','y','t','h','o','n')
# print(tuple3[1:5:2])
# print(tuple3[4:2:-1])

# pstr = "abcdba"
# if(pstr==pstr[::-1]):
#     print('pstr is a palindrom')
# else:
#     print('pstr is not a palindrom')
#
# print(pstr[::-1])
#
#
# list1 = [1,2,3]
# #append()函数可以接收一个元素也可以接收多个元素，但是多个元素时整体加入的，以列表的形式
# list1.append([4,5])
# list1.extend([4,5])
# list1.insert(1,9)
# print(list1)

# list1 = [1,2,3]
# list2 = list1.copy()
# list2[1] = 5
# print(list1)
# print(list2)



#列表中有列表等可变序列
import copy
# list1 = [1,2,3,[7,8,9]]
# list2 = list1.copy()
# list2 = list1[:]
#list2 = copy.copy(list1)
# list2[3][0]= 5
# list2[1] = 6
# print(list1)
# print(list2)
# print(id(list1[1]))
# print(id(list2[1]))
# print(id(list1[3][0]))
# print(id(list2[3][0]))



# import copy
# list1 = [1,2,3,[7,8,9]]
# list2 = copy.deepcopy(list1)
# list2[3][0]= 5
# list2[1] = 6
# print(list1)
# print(list2)
# print(id(list1[1]))
# print(id(list2[1]))
# print(id(list1[3][0]))
# print(id(list2[3][0]))



# alist=list(range(0,9,2))

tuple1 = ('p','y','t','h','o','n')
list2 = list(tuple1)
list2[0] = 'P'
tuple2 = tuple(list2)
tuple2




