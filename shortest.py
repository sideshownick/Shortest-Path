#!python 

docstring="""
\nFind shortest path, using Dijkstra's algorithm

Usage: 
python shortest.py exmouth-links.dat ORIG DEST
ORIG = origin string from input csv file (e.g. J1053)
DEST = destination string from input csv file (e.g. J1037)

The format of the file is (without the header line):
startNode  		endNode  		distance
A          		B        		2
B          		C        		4
"""

import sys

def find_route(args=None):
    
    if args==None:
        #take commandline arguments
        try: 
            fname = sys.argv[1]
            origin = sys.argv[2]
            destin = sys.argv[3]
        #print howto and exit if not correcly called
        except IndexError: 
            return(docstring)
    #for use as an imported function      
    else: fname,origin,destin = args
    
    if origin==destin: 
        return("\nOrigin {} same as destination {}".format(origin,destin))

    try: 
        filehandle = open(fname, "r")             
    except Exception as e:
        return("\n"+str(e))
        #return('File "{}" not found'.format(fname))
        
    try: 
        data=[]
        for line in filehandle.readlines():
            n1, n2, d = line.strip().split(" ")
            data.append([n1,n2,int(d)])
    except: sys.exit("\nFile not in correct format." + docstring)
    
    dist,prev = Dijkstra(data, origin, destin) 
    result = reroute(prev, destin)
    return(result)



     
def Dijkstra(data, orig, dest):
    
    #create vertex set Q
    Q=dict()
    for d in data:
        Q[d[0]] = {} #initiate dictionary of neighbour links
        Q[d[1]] = {} #ensure destination nodes are all in Q for searches
        
    #check origin and destination exist, raise if not named in file    
    if orig not in Q: sys.exit("\nOrigin key {} not found".format(orig))
    if dest not in Q: sys.exit("\nDestination {} key not found".format(dest))
        
    #populate dictionary: {out1={in1:d1. in2:d2, ...}, out2={...}, ...}
    for d in data:
        Q[d[0]][d[1]]=int(d[2]) # neigbours all a dictionary of distances
    dist={n:1e42 for n in Q} # set initial distances to origin from nodes to far away
    prev={n:None for n in Q} # all nodes intially have no previous node on min route
        
    u = orig
    dist[u] = 0                        

    while len(Q)>0:
        #u = vertex in Q with min dist[u]
        distQ = {n:dist[n] for n in dist if n in Q} # new dist dict containing only nodes still in Q
        u = min(distQ, key=distQ.get) # find the next min, but keep old dist dict for lookups of dist[v] below

        #remove u from Q
        neis = Q.pop(u) 
        
        #search each neighbour v of u
        for v in neis:                
            alt = dist[u] + neis[v] #distance to u plus link distance length(u,v)
            #if the total distance from orig to v is shorter than previously searched
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u #record u as the preceding node to v
    return dist, prev

def reroute(prev, u):   
    S=[] #list for forward route
    if prev[u]!=None: #check a route exists
        while u!=None:
            S.insert(0,u)
            u = prev[u]
        return("\n".join(S))
    else: 
        return("No Route Found")   
 

if __name__=="__main__":
    result = find_route()
    print(result)

else: #test case
    import time

    t = time.time()
    find_route(args=("exmouth-links.dat", "X1046", "X1039"))
    print(time.time()-t)


