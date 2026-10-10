import sys


def main():
    n, m, k = map(int, sys.stdin.read().split())

    # Сетка календаря: день d стоит в позиции p = d - 1 + (k - 1)
    rows = (n + k - 2) // m + 1
    filled = [[False] * m for _ in range(rows)]
    for d in range(1, n + 1):
        p = d - 1 + (k - 1)
        filled[p // m][p % m] = True

    # Перебор всех прямоугольников, целиком состоящих из заполненных клеток
    best = 0
    for r1 in range(rows):
        for c1 in range(m):
            if not filled[r1][c1]:
                continue
            for r2 in range(r1, rows):
                for c2 in range(c1, m):
                    ok = True
                    for r in range(r1, r2 + 1):
                        for c in range(c1, c2 + 1):
                            if not filled[r][c]:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        area = (r2 - r1 + 1) * (c2 - c1 + 1)
                        if area > best:
                            best = area
    print(best)


if __name__ == "__main__":
    main()
