#fractional knapsack
value =list(map(int,input().split()))
weight=list(map(int,input().split()))
w=int(input())
wperv=[round(value[i]/weight[i],2) for i in range(len(value))]
sd=sorted(wperv,reverse=True)
totv=totw=0.0
for i in sd:
    indi=wperv.index(i)
    totw+=weight[indi]
    totv+=value[indi]
    if totw>w:
        totv-=(abs(totw-w)*value[indi])/weight[indi]
        totw-=abs(totw-w)
        break
    elif totw==w:
        break
    weight.pop(indi)
    value.pop(indi)
    wperv.pop(indi)
print(totv)

        
        

        
    

    
    
    
