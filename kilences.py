def kilences(b_meret):
    for i in range(1, b_meret + 1):
        for j in range(1, b_meret + 1):
            print(f"{i * j:4}", end=' ')
        print()

kilences(10)
