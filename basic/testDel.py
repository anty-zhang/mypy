
import copy

l = [1, 2, 3, 4]
tl = copy.deepcopy(l)
print 'tl: ', tl
for i, d in enumerate(l):
    print i, d
    del l[i]