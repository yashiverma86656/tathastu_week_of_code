def robbery(list):
      
      h1 = 0
      h2 = 0
      for i in range(0,len(list)):
         temp = h1
         h1 = max(h2+list[i],h1)
         h2 = temp
      return h1
n=int(input("enter the no. of houses: "))
list1=[]
for x in range(n):
    list1.append(int(input("Enter the value in the Houses one by one " )))
print("user entered following list: ",list1)

print("maximum amount robbed",robbery(list1))
