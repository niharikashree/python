#DELTE HEAD NODE IN SINGLY LINKED LIST
class node:
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
    newnode=node(ele)
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
    
def deleteheadnode(head):
    if head==None or head.next==None:
        return None
    head=head.next
    return head
n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=insertatend(head,ele)
printlefttoright(head)

head=deleteheadnode(head)

printlefttoright(head)
