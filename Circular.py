class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CL:
    def __init__(self):
        self.head=None
    def add(self,data):
        a=Node(data)
        if self.head==None:
            self.head=a
            a.next=self.head
        else:
            c=self.head
            while c.next!=self.head:
                c=c.next
            c.next=a
            a.next=self.head
    def P(self):
        q=self.head
        if self.head==None:
            print("None")
        else:
            while q:
                if q.next==self.head:
                    print(q.data,"->",end="")
                    print(q.next.data,"->",end="")
                    break
                else:
                    print(q.data,"->",end="")
                    q=q.next
cl=CL()
cl.add(10)
cl.add(9)
cl.add(11)
cl.P()
# Output: 10 -> 9 -> 11 -> 10 ->