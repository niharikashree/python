# DICTIONARY
store=dict()
print(store)
store['p']=29
store['sweety']=19
store['W']=90
store[98]=70
print(store)
allkeys=store.keys()
print(allkeys)
for ele in allkeys:
    print(ele,store[ele])
for i in "pythonbasic":
    print(i)
for val in [5,7,9,8,6,4,2,1]:
    print(val)


#ANOTHER EXAMPLE 
new=dict()
new['info']=3
new['data']=2
new['table']=1
print(new)
keys=new.keys()
print(keys)
for ec in keys:
    print(ec)
    print(ec,new[ec])

#EXAMPLE--2
store=dict()
print(store)
store['p']=29
store['ram']=19
store['Wind']=90
store[98]=70
print(store)
allkeys=store.keys()
print(allkeys)
for ele in allkeys:
    print(ele,store[ele])


for i in "niharika":
    print(i)
for val in [5,7,9,8,6,4,2,1]:
    print(val)


#TO CHECK WHETHER THE KEY IS ALREADY PRESENT IN DICT AND THEN ADD ITS VALUE BY 1
if ec in word:
        store[ec]=store[ec]+1
    else:
        store[ec]=1
        print(store)



#TO CHECK THE FREQUENCY OF A CHARACTER AND PRINT
reschar='#'
resfrequency=0

for ec in keys:
    if store[ec]>resfrequency:
        resfrequency=store[ec]
        reschar=ec
        print(reschar,resfrequency)

