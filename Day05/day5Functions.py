def front(f, b):
    nf, nb = int(f), int(f + (int(b) - (int(f) + 1)) / 2)
    return int(nf), int(nb)


def back(f, b):
    nf, nb = int(f + (int(b) - (int(f) - 1)) / 2), int(b)
    return int(nf), int(nb)
