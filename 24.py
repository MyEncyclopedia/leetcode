from itertools import combinations, combinations_with_replacement, permutations

mul = lambda x, y: x * y
plus = lambda x, y: x + y
div = lambda x, y: x / y
minus = lambda x, y: x - y

def run(op1, op2, op3, a, b, c, d):
    yield op1(op2(a, b), op3(c, d))
    yield op1(a, op2(op3(b, c), d))
    yield op1(op2(op3(a, b), c), d)
    yield op1(op2(op3(a, b), c), d)
    yield op1(a, op2(b, op3(c, d)))
    yield op1(op2(a, op3(b, c)), d)


if __name__ == '__main__':
    op_lst = [plus, minus, mul, div]
    val_lst = [1, 2, 4, 6]

    for ops in combinations_with_replacement(op_lst, 3):
        for val in permutations(val_lst):
            for aa in run(ops[0], ops[1], ops[2], val[0], val[1], val[2], val[3]):
                print(aa)

