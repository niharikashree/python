
#DOUBLY LINKED LIST
class Box:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
def findtail(head):
    if head==None:
        return None
    tail=head
    while tail.next!=None:
        tail=tail.next
    return tail
def insertatend(head,ele):
    newnode=Box(ele)
    if head==None:
        return newnode
    tail=findtail(head)
    tail.next=newnode
    newnode.prev=tail
    return head

def printlefttoright(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()
    
def printrighttoleft(head):
    tail=findtail(head)
    while tail!=None:
        print(tail.data,end=" ")
        tail=tail.prev
    print()
    
n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=insertatend(head,ele)
printlefttoright(head)
printrighttoleft(head)
