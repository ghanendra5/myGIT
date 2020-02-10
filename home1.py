flag=0
def func(lists):
    global flag;
    for i in range(1,len(lists)):
        if(lists[i]<lists[i-1]):
            flag=1 
        else:
            flag=0
lists=[] 
print("enter the elements of lists")
n=5
for i in range (n):
    num=int(input())
    lists.append(num)
print("\n")
print(lists)
print("\n")
func(lists)
if(flag==0):
    print("true")
else:
    print("false")