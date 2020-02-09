print("The sheet of daily expenses")
print("enter the amounts spends on vegetables  by me:")
lists1=[]
lists2=[]
for i in range (0,4):
    ele=int(input())
    lists1.append(ele)
print("Education by ghanendra \r")
for i in range(0,4):
    els=int(input())
    lists2.append(els)
print("\r")
print("Enter the amount spends on vegetables by sandip:")
lists3=[]
lists4=[]
for i in range(0,4):
    s=int(input())
    lists3.append(s)
print("For education by sandip")
for i in range(0,4):
        f=int(input())
        lists4.append(f)
print("\r")
datahouse={"Ghanendra":{"vegetables":lists1,
                          "education":lists2,
                          },
          "sandip":{"vegetables":lists3,
                      "education":lists4
                  }
          }
print("+++++++MEANU+++++")
print("1.display")
print("2.total expenditure\r")
print("3.total expenses  by a single person")
choice=int(input("your choice\r"))
def display(choice):
    print("enter 1 to display ghanendra and 2 to dispaly sandip details\r")
    x=int(input("number: "))
    if x == 1:
        print("detail of ghanendra: ")
        print(datahouse.get("Ghanendra"))
    elif x==2:
        print("detail of sandip: ")
        print(datahouse.get("sandip"))
    else:
        print("wrong choice\r")
def total_expenses(datahouse):
    result=sum(lists1+lists2+lists3+lists4)
    return result
def average():
    a=sum(lists1+lists2)
    b=sum(lists3+lists4)
    print("total money spend by ghanendra: ",a)
    print("total money spend by sandip:",b)
while(choice <4):
    if choice == 1:
        display(choice)
        break
    elif (choice == 2):
        print(total_expenses())
        break
    elif (choice == 3):
        average()
        break
