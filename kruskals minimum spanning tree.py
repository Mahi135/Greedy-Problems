#kruskals minimum spanning tree
n=int(input())
parent=[0]*n
mincost,ne,l=0,1,[]
for i in range(n):
    l.append(list(map(lambda x: 999 if int(x)==0 else int(x),input().split())))
while(ne<n):
        m=999
    for i in range(n):
        if min(l[i])<m:
            m=min(l[i])
            u,v=i,l[i].index(m)
        
    while(parent[u]!=0):
        u=parent[u]
    while(parent[v]!=0):
        v=parent[v]

    if(v!=u):
        ne+=1
        print("cost"+str(m))
        mincost+=m
        parent[v]=u
    l[u][v]=l[v][u]=999
       
print("minimum cost :"+str(mincost))
        
