__author__ = 'andy'


l = [['push_switch', 1]]
uid = 10
c = [( uid, name, value) for name, value in l]

print c[0]

l1 = [5, [1, 5, 6]]

def test(*args):
    print args
test(*l1)