
#USING FUNCTIONS IN PYTHON 
(MAX OF ALL NUMBERS IN LIST)
def occurances(listofnum):
    n=len(listofnum)
    for i in range(n-1):
        if listofnum[i]>=listofnum[i+1]:
            temp=listofnum[i+1]
            listofnum[i+1]=listofnum[i]
            listofnum[i]=temp
    print(listofnum[n-1])

   

listofnum=[1,2,3,44,66,78,98,96,95,94,92,90]
result=occurances(listofnum)

#ANOTHER WAY OF SOLVING MAX NUMBERS IN LIST


listofnum=[1,2,3,44,66,78,98,96,95,94,92,90]

def max(list1):
    n=len(list1)
    res=0
    for i in range(n-1):
        if list1[i]>res:
            res=list1[i]
    return res

result=max(listofnum)
print(result)

OR USE KEYWORD max() AND min() TO FIN MAX AND MIN OF LIST
