from operator import itemgetter

with open('input.txt', 'r') as f:
    t, bs = f.readlines()
    t = int(t)
    bs = list(map(int, filter(lambda x: x != 'x', bs.split(','))))

earliest_bus_with_remainder = min(list(zip(bs, [- (t % b) + b for b in bs])), key=itemgetter(1))
print(earliest_bus_with_remainder[0] * earliest_bus_with_remainder[1])