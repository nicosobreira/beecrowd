while True:
    D, N = input().split()

    if D == N == "0":
        break

    new = N.replace(D, "")

    # Como retirar esse if?

    """
    if len(new) == 0:
        print("0")
    else:
        print(int(new))
    """

    print(int(new or "0"))
