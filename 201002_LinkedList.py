#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Linked List
#A node consists of its data and reference value for the next node


# In[19]:


#Define a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# In[22]:


class LinkedList:
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy
        
        self.current = None
        self.before = None
        self.num_of_data = 0
        
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.num_of_data +=1
    
    def delete(self):
        pop_data = self.current.data
        if self.current is self.tail:
            self.tail = self.before
        self.before.next= self.current.next
        self.current = self.before
        self.num_of_data -=1
        return pop_data
    
    def first(self):
        if self.num_of_data == 0:
            return None
        self.before = self.head
        self.current = self.head.next
        return self.current.data
    
    def next(self):
        if self.current.next == None:
            return None
        self.before = self.current
        self.current = self.current.next
        return self.current.data
    
    def size(self):
        return self.num_of_data


# In[30]:


if __name__ == '__main__':
    l_list = LinkedList()
    l_list.append(5)
    l_list.append(2)
    l_list.append(1)
    l_list.append(2)
    l_list.append(7)
    l_list.append(2)
    l_list.append(11)

    print('first :', l_list.first())      # first : 5
    print('next :', l_list.next())        # next : 2
    print('size :', l_list.size())        # size : 7
    print('delete :', l_list.delete())    # delete : 2
    print('size :', l_list.size())        # size : 6
    print('current:', l_list.current.data)# current: 5
    print('tail:', l_list.tail.data)      # tail: 11
    print('first :', l_list.first())      # first : 5
    print('next :', l_list.next())        # next : 1
    print('next :', l_list.next())        # next : 2
    print('next :', l_list.next())        # next : 7


  # 전체 노드 data 표시하기
    data = l_list.first()

    if data:
        print(data, end=' ')
        while True:
            data = l_list.next()
            if data:
                print(data, end= ' ')
            else:
                break
  # 5 1 2 7 2 11



  # 2만 삭제하기
    data = l_list.first()

    if data and data == 2:
        l_list.delete()
        print('deleted', end=' ')
    else:
        print(data, end= ' ')

    while True:
        data = l_list.next()
        if data == 2:
            l_list.delete()
            print('deleted', end=' ')
        elif data:
            print(data, end=' ')
        else:
            break


# In[ ]:




