#DELETE TAIL NODE IN SINGLY LINKED LIST
class Box:
    def __init__(self,data):
        self.data=data
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
    return head

def printlefttoright(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()
    
def deletetailnode(head):
    if head==None or head.next==None:
        return None
    prev=None
    curr=head
    while curr.next!=None:
        prev=curr
        curr=curr.next
    prev.next=None
    return head

n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=insertatend(head,ele)
    
printlefttoright(head)

head=deletetailnode(head)

printlefttoright(head)
