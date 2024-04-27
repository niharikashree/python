#DELETE AT SPECIFIC POSITION IN SLL
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
    
def deleteatspecific(head,position):
    currind=1
    curr=head
    prev=None
    while currind!=position:
        currind+=1
        prev=curr
        curr=curr.next
    if prev==None:
        head=head.next
        head.prev=None
        return head
    prev.next=curr.next
    return head

n=int(input())
l=list(map(int,input().split()))
position=int(input())

head=None
for ele in l:
    head=insertatend(head,ele)
    
printlefttoright(head)

head=deleteatspecific(head,position)

printlefttoright(head)
