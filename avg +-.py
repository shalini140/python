positive_sum=0
positive_count=0
negative_sum=0
negative_count=0
while True:
    num=int(input("enter the number:"))
    if num==-1:
        break
    elif num>0:
        positive_sum+=num
        positive_count+=1
    elif num<0:
        negative_sum+=num
        negative_count+=1
    if positive_count>0:
        print("the average of positive numbers is:",positive_sum/positive_count)
    if negative_count>0:
        print("the average of negative number is:",negative_sum/negative_count)
