import string
'''
end='lol'

def make_trie(*words):
    root=dict()
    for w in words:
        curr=root
        for i in w:
            curr=curr.setdefault(i,{})

        curr[end]=end
    return(root)

#a=make_trie('tanmay','tanya','cuddly','haha','hahaaa')
a=make_trie('')
print(a)

def insert(root ,word):
    curr=root
    for i in word :
        curr=curr.setdefault(i,{})
    curr[end]=end

def search(root,word):
    curr=root
    for i in word:
        curr=curr.get(i,None)
        if(curr is None):
            return(0)

    return(1)


insert(a,'tanmay')
insert(a,'tanya')
insert(a,'cuddly')
print(search(a,'cuddly'))
print(search(a,'Nope'))
print(a)
'''

al=list(string.ascii_lowercase)
d={} #for mapping
for i in range(26):
    d[al[i]]=i

print(d)

class node:
    count=0
    word=0
    def __init__(self):
        self.children=[0]*26
        self.val=None

    def increment(self):
        self.count=self.count+1

    def showcount(self):
        return(self.count)

    def setword(self):  #to know whether this node is the end of a word or not ,helps in some cases
        self.word=1

    def isword(self):
        return(self.word)



class trie:
    def __init__(self):
        self.root=node()

    def insert(self,word):
        t=self.root
        for i in word:

            if t.children[d[i]]!=0:
                print('traversing')
                t=t.children[d[i]]
                t.increment()
            else:
                #print('here')
                t.children[d[i]]=node()
                t.children[d[i]].val=i;
                print(t.children)
                t=t.children[d[i]]
                print(t.val)
                t.increment()
        t.setword()
        print(t.isword())





    def search(self,word):
        t=self.root
        for i in word:
            if t.children[d[i]]!=0:
                t=t.children[d[i]]
            else:
                return 0

        return(1)

    def count(self, word):
        t=self.root
        for i in word:
            if t.children[d[i]] != 0:
                t = t.children[d[i]]
            else:
                 return 0
        print(t.val)
        return(t.showcount())



t=trie()

t.insert('tanmay')
t.insert('tanya')
t.insert('cuddly')

print(t.search('tanmay'),t.search('tanya'),t.search('lol'))

print(t.count('tan'))



