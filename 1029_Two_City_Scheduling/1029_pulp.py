import pulp

# costs = [[10,20],[30,200],[400,50],[30,20]]  # 110
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]   # 1859


I = range(len(costs))

items=[i for i in I]
city_a = pulp.LpVariable.dicts('left', items, 0, 1, pulp.LpBinary)
city_b = pulp.LpVariable.dicts('right', items, 0, 1, pulp.LpBinary)

m = pulp.LpProblem("Two Cities", pulp.LpMinimize)

m += pulp.lpSum((costs[i][0] * city_a[i] + costs[i][1] * city_b[i]) for i in items)

# Constraints
# Each person must be assigned to at exact one city
for i in I:
    m += pulp.lpSum([city_a[i] + city_b[i]]) == 1
# create a binary variable to state that a table setting is used
m += pulp.lpSum(city_a[i] for i in I) == (len(I) // 2)

m.solve()

total = 0
for i in I:
    if city_a[i].value() == 1.0:
        total += costs[i][0]
    else:
        total += costs[i][1]

print("Total cost {}".format(total))
