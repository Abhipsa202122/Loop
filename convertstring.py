l=[41,500,76,87]
d={}
for i in l:
    j=i
    str = " "
    #for j in l:
    while j>=0:
        mod = j%10
        if mod == 0:
            str = str + "zero"
            print(str)
        if mod == 1:
            str = str + "one"
            print(str)
        if mod == 2:
           str = str + "two"
           print(str)
        if mod == 3:
           str = str + "three"
           print(str)
        if mod == 4:
           str = str + "four"
           print(str)
        if mod == 5:
           str = str + "five"
           print(str)
        if mod == 6:
           str = str + "six"           
        if mod == 7:
           str = str + "seven"
           print(str)
                 
            
        j = j//10
        
#print(str)
            
        
#print(d)    
    
