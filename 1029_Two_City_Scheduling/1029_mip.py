
from mip import Model, xsum, maximize, BINARY, minimize

costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]   # 1859
# costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
# costs = [[10,20],[30,200],[400,50],[30,20]]

I = range(len(costs))

m = Model("knapsack")

x = [[m.add_var(var_type=BINARY) for j in range(2)] for i in I]

m.objective = minimize(xsum(costs[i][j] * x[i][j] for i in I for j in range(2)))

m += xsum(x[i][0] for i in I) == (len(I)//2)
for i in I:
    m += xsum(x[i][j] for j in range(2)) == 1

m.optimize()

print(x)

# selected = [i for i in I if x[i][0].x >= 0.99]
# print("selected items: {}".format(selected))
#
# total = 0
# for i in I:
#     if i in selected:
#         total += costs[i][0]
#     else:
#         total += costs[i][1]
# print('++++ sum is {}'.format(total))