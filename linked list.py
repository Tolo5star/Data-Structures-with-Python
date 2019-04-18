class node:
    def __init__(self):
        self.data=None
        self.next=None
    def setdata(self,d):
        self.data=d
    def setnext(self,n):
        self.next=n
    def disp(self):
        return self.data

'''
s=node()
s1=node()
s2=node()

s.setdata(5)
s1.setdata(2)
s2.setdata(0)

s.setnext(s1)
s1.setnext(s2)



head=s
while head is not None :
    print(head.disp())
    head=head.next

'''
class linked_list:
    def __init__(self,n):
        self.root=n
        self.temp=n
    def insert(self,data):
        if self.root.next is None:
            self.temp.setdata(data)
            self.root.next=self.temp
            print('here')
        else:
            self.temp.next=node()
            self.temp = self.temp.next
            self.temp.setdata(data)

    def traverse(self):
        t=self.root
        while t is not None:
            print(t.disp())
            t=t.next


head=node()

l=linked_list(head)
for i in range(10):
    l.insert(i)

l.traverse()




