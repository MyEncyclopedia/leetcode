import pulp

# costs = [[10,20],[30,200],[400,50],[30,20]]  # 110
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]   # 1859


I = range(len(costs))

items=[i for i in I]
left = pulp.LpVariable.dicts('left',items,0,1, pulp.LpBinary)
right = pulp.LpVariable.dicts('right',items,0,1, pulp.LpBinary)
# create a binary variable to state that a table setting is used

m = pulp.LpProblem("Two Cities", pulp.LpMinimize)

m += pulp.lpSum((costs[i][0] * left[i] + costs[i][1] * right[i]) for i in items)

# specify the maximum number of tables
for i in I:
    m += pulp.lpSum([left[i] + right[i]]) == 1

m += pulp.lpSum(left[i] for i in I) == (len(I) // 2)

m.solve()

total = 0
for i in I:
    if left[i].value() == 1.0:
        total += costs[i][0]
        print('left\n')
    else:
        total += costs[i][1]
        print('right\n')

print("Total cost {}".format(total))
