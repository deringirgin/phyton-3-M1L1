def solve_riddle():
    for candies in range(1, 100):
        if candies % 2 == 1 and candies % 3 == 1:
            return candies
    return -1


result = solve_riddle()
print(f"Cüce'nin {result} tane şekeri var")
