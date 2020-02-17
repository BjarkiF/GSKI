
def modulus(int, div):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    return mod(int, div, div)

def mod(goal, int, add):
    int += add
    if int > goal:
        int -= add
        rest = goal - int
        if rest < 0:
            return 0
        return rest
    elif int == goal:
        return 0
    else:
        return mod(goal, int, add)


def how_many(lis1, lis2):
    return how_many_rec(lis1, lis2, 0, 0, 0)

def how_many_rec(lis1, lis2, a, b, count):
    len1 = len(lis1)
    len2 = len(lis2)
    if lis1[a] == lis2[b]:
        count += 1
        a += 1
        if a >= len1:
            return count
        b = 0
        return how_many_rec(lis1, lis2, a, b, count)
    b += 1
    if b >= len2:
        b = 0
        a += 1
    if a >= len1:
        return count
    else:
        return how_many_rec(lis1, lis2, a, b, count)

# [0, 1, 2, 3, 4]
# [3, 1, 5, 3, 2]

# FEEL FREE TO EDIT THE TESTS AND MAKE THEM BETTER
# REMEMBER EDGE CASES!

def test_modulus(num1, num2):
    print("The modulus of " + str(num1) + " and " + str(num2) + " is " + str(modulus(num1, num2)))

def test_how_many(lis1, lis2):
    print(str(how_many(lis1, lis2)) + " of the items in " + str(lis1) + " are also in " + str(lis2))

def run_recursion_program():

    print("\nTESTING MODULUS:\n")

    test_modulus(8, 3)
    test_modulus(9, 3)
    test_modulus(10, 3)
    test_modulus(11, 3)
    test_modulus(8, 2)
    test_modulus(0, 7)
    test_modulus(15, 5)
    test_modulus(128, 16)
    test_modulus(128, 15)

    print("\nTESTING HOW MANY:\n")

    test_how_many(['a', 'f', 'd', 't'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['a', 'b', 'f', 'g', 'a', 't', 'c'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['f', 'g', 't'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['a', 'a'], ['a', 'a'])


if __name__ == "__main__":
    run_recursion_program()