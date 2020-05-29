#prims minimum spanning tree
n=int(input())
visited=[0]*n
mincost,l=0,[]
for i in range(n):
    l.append(list(map(lambda x: 999 if int(x)==0 else int(x),input().split())))
visited[0]=1
for z in range(n-1):
    m=999
    for i in range(n):
        if visited[i]==1:
            for j in range(n):
                if visited[j]==0:
                    if l[i][j]<m:
                        m,u,v=l[i][j],i,j
    visited[v]=1
    mincost+=m
    l[u][v]=l[v][u]=999
    print("Edges {}-{} cost:{}".format(u,v,m))
print("minimum cost :"+str(mincost))
        
