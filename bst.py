class node:
    def __init__(self):
        self.key=None
        self.left=None
        self.right=None
    def setkey(self,k):
        self.key=k
    def getkey(self):
        return(self.key)


class bst:
    def __init__(self,n):
        self.root=n
        self.temp=n
    def insert(self,k):
        if self.temp.key is None:
            self.root.key=k
            print("work1")
        else:
            t=self.root
            while t.key is not None:
                if t.key<k:
                    print(t.key)
                    if t.right is None:
                        t.right=node()
                        print("rightcccc")
                    t=t.right
                    print("right")

                elif t.key>=k:
                    if t.left is None:
                        t.left=node()
                        print("leftccccc")
                    t=t.left
                    print("left")
            t.setkey(k)
    def find(self,r,k):
        t=r
        if r is None:
            print("lol not found")
            return
        elif r.getkey() is None:
            print("nope lol", t.key, k)

        elif t.getkey()==k:
            print("Found")
            return
        else:
            while t is not None:
                if t.getkey() < k:
                    self.find(t.right,k)
                elif t.getkey() >=k:
                    self.find(t.right,k)
                else:
                    print("not found")
                    return




lol=node()

b=bst(lol)

for i in range(5,10):
    print(i)
    b.insert(i)

print(1)
b.insert(1)

print(4)
b.insert(4)

print(11)
b.insert(11)

print(10)
b.insert(10)

b.find(lol,4)


