# Solve the Tower of Hanoi problem.
def TowerOfHanoi(n, original, next, temp):
    if n == 1:
        print("move disk one from the original pole", original, "to the next", next)
        return
    TowerOfHanoi(n-1, original, temp, next)
    print("move disk", n, "from the original pole", original, "to the next", next)
    TowerOfHanoi(n-1, temp, next, original)

n = 3
TowerOfHanoi(n, 'a', 'b', 'c')