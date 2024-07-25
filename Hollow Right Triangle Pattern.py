def hollow_right_triangle_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == 1 or j == i or i == n:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

hollow_right_triangle_pattern(5)
