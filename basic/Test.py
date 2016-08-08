__author__ = 'andy'


def test1():
    li = [{'name': 'push_switch', 'value': 0}, {'name': 'push_swith', 'value': 1}]
    push_flag = True
    for row in li:
        if row['name'] == 'push_swith' and row['value'] != 1:
            push_flag = False
            break

        if row['name'] == 'push_switch' and row['value'] != 1:
            push_flag = False
            continue

    print row['name']
    print row['value']


def test2():
    gl = "123"

    test3(gl)

    print "gl: ", gl


def test3(gl):
    print "test3 enter gl: ", gl
    gl = "456"
    print "test3 end gl: ", gl

if __name__ == '__main__':
    test2()