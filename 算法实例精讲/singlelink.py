class Node:
    def __init__(self,data):
        self.data=data
        self.next=Node
        return
    def has_value(self,value):
        if self.data==value:
            return True
        else:
            return False

class singlelink:
    def __init__(self):
        self.head=Node
        self.tail=None
        self.length=0
        return

# 判断是否为空
def isempty(self):
    return self.length==0

# 向尾部添加节点
def add_node(self,item):
    if not isinstance(item,Node):
        item=Node(item)
    if self.head==None:
        self.head=item
    else:
        self.tail.next=item
        self.tail=item
    self.length+=1
    return

# 在链表中添加节点
def insert_node(self,index,data):
    if isempty():
        print('this link is empty')
        return
    if index<0 or index>=self.length:
        print("error: link out of ")
        return
    item=Node(data)
    if index==0:
        item.next=self.head
        self.head=item
        self.length+=1
        return
    j=0
    # 申请一个头节点和尾节点
    node=self.head
    prev=self.head
    # 移动前节点和后节点到目的地
    while node.next and j<index:
        prev=node
        node=node.next
        j+=1
    # 插入节点
    if j==index:
        item._next=node
        prev._next=item
        self.length+=1


# 删除节点
def delete_node_byid(self,item_id):
    id=1
    current_node=self.head
    previous_node=None
    while current_node is not None:
        if id==item_id:
            #未完
            pass