import itertools
po = (0, 2)
grib = (2, 5)
bs = (5, 2)
garden = (6, 6)
onlygreen = (8, 3)
m = po
b = [grib, bs, garden, onlygreen]
c = itertools.permutations(b)

for mn in c:
    i = m, mn, m
    print(i)

