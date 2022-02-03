
from ortools.sat.python import cp_model


# def main():
#     pass

# Instantiate a cp model.
# costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]  # 1859
costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
# costs = [[10,20],[30,200],[400,50],[30,20]]

I = range(len(costs))

model = cp_model.CpModel()
x = []
total_cost = model.NewIntVar(0, 10000, 'total_cost')
for i in I:
    t = []
    for j in range(2):
        t.append(model.NewBoolVar('x[%i,%i]' % (i, j)))
    x.append(t)

# Constraints
# Each person must be assigned to at exact one city
[model.Add(sum(x[i][j] for j in range(2)) == 1) for i in I]
# equal number of person assigned to two cities
model.Add(sum(x[i][0] for i in I) == (len(I) // 2))

# Total cost
model.Add(total_cost == sum(x[i][0] * costs[i][0] + x[i][1] * costs[i][1] for i in I))
model.Minimize(total_cost)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    print('Total min cost = %i' % solver.ObjectiveValue())
    print()
    for i in I:
        for j in range(2):
            if solver.Value(x[i][j]) == 1:
                print('People ', i, ' assigned to city ', j, '  Cost = ', costs[i][j])

    print()

print('Statistics')
print('  - conflicts : %i' % solver.NumConflicts())
print('  - branches  : %i' % solver.NumBranches())
print('  - wall time : %f s' % solver.WallTime())


if __name__ == '__main__':
    main()
