list=[]

list.append(input("Enter element 1:"))
list.append(input("Enter element 2:"))
list.append(input("Enter element 3:"))
print(list)

copy_list=list.copy()
copy_list.reverse()
print(copy_list)

if (list==copy_list):
    print("this is a palindrome")
else:
    print("this is not palinndrome")