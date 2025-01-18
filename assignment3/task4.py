#Task 4: Sum and Average Calculator

def sum_n_average():
    numbers=list(map(int,input("space separator and negative number to stop:").split()))
    sum=0
    for i in numbers:
        if(i<0):
            break
        sum+=i 
        
    avg=sum/(len(numbers)-1)
    print("Sum:",sum)
    print("Average:",avg)
    
sum_n_average()