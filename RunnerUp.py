n =len(list1) 
for i in range(2,n):  
    if list1[i]>mx:  
        secondmax=mx 
        mx=list1[i]  
    elif list1[i]>secondmax and mx != list1[i]:  
        secondmax=list1[i] 
    else: 
        if secondmax == mx: 
            secondmax = list1[i] 
