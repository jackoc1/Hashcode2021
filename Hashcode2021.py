'''



cat d.txt | python3 hash.py > a.out


0, 1, 2, 3, 4, ....

[
# Node 0 goes to
[(0.5, 2, "rue-de-whatever"),(0.76,4,"name"),() ... ],
# Node 1 goes to
[],
# Node 2 goes to
[],
]

dict['rue-de-londres'] -> (0,1)

min -> 1 second
max -> max

range = max - min
scaled_x = (x-min)/range  ---> x~[0,1]

final_x = (((x-min)/(max - min))) * (new_max-1)) + 1


[road1, road2, road3]
road1_time = 1 (this can be varied at the end)
road2_time = road1_time * (road2 appearances / c)
road3_time = road1_time * (road3 appearances / c)

'''

# PROCESS INPUT
D, I, S, V, F = map(int, input().split())
adj_mat = [[] for _ in range(I)]
adj_back = [[] for _ in range(I)]

dict = {}
street_uid = {}

for i in range(S):
    B, E, name, L = map(str, input().split())
    B = int(B)
    E = int(E)
    L = int(L)
    dict[name] = (B,E)
    street_uid[name] = i
    adj_mat[B].append((L, E, name))
    adj_back[E].append((L, B, name))

# ALGORITHM
street_appearances = [0 for i in range(S)]

routes = []
for i in range(V):
    things = input().split() # List of number of streets followed by streetnames
    n = int(things[0]) # 3 street1 street2 rue4
    route = [n]+things[1:]
    routes.append(route)
    for j in range(1,n+1):
        name = things[j]
        street_appearances[street_uid[name]] += 1



# OUTPUT
res = ""
intersections = 0
try:
    popular_streets = sorted(street_appearances)[-len(street_appearances)//20]
    really_popular_streets = sorted(street_appearances)[-len(street_appearances)//50]
    super_popular_streets = sorted(street_appearances)[-len(street_appearances)//100]
except:
    popular_streets = street_appearances[0]

for i in range(I):
    B = (len(adj_back[i])) # B = no. of incoming roads to current intersection
    #print(B)
    ans = ""
    c = 0
    mn = 99999999999
    mx = 0
    mx2 = 0
    all = []
    for j in range(B):
        current_street = street_appearances[street_uid[adj_back[i][j][2]]]
        if 0!=(current_street):
            c+=1
            if current_street < mn:
                mn = current_street
            elif current_street > mx:
                mx = current_street
                mx2=mx
            elif current_street>mx2:
                mx2 = current_street
            all.append(current_street)
    all.sort()
    fc=0
    for j in range(B):
        current_street = street_appearances[street_uid[adj_back[i][j][2]]]
        if 0!= (current_street):
            if current_street > super_popular_streets:
                cnt=7
                fc+=1
            elif current_street > really_popular_streets:
                cnt=5
                fc+=1
            elif current_street > popular_streets:
                cnt=3
                fc+=1
            elif current_street>=all[-1*(int(c//(15)) + 1)]:
                cnt=2
                fc+=1
                #ans+=(adj_back[i][j][2]+f' {cnt}\n')

            else:
                fc+=1
                cnt = 1
                #cnt = int((((((current_street-mn)/(mx - mn))) * (mx-1)) + 1))
            ans+=(adj_back[i][j][2]+f' {cnt}\n')
            #weight = max(1, current_street // c)

    if fc!=0:
        res+=str(i)+'\n'
        intersections += 1
        res+=str(c)+'\n'
        res+=(ans)
print(intersections)
print(res)
