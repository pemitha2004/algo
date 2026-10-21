numbers=[10,20,30,40,50,60,70,80,90,100]
search=int(input("enter the element"))

for i in range (len(numbers)):
    if numbers[i]==search:
        print("element is at",i)
        no=True
        break
if no==False:
        print("elementnot found")
