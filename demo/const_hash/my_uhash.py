from uhashring import HashRing

# create a consistent hash ring of 3 nodes of weight 1
hr = HashRing(nodes=['node1', 'node2', 'node3', 'node4', 'node5', 'node6'])


print hr.get_nodes()


# get the node name for the 'coconut' key
target_node = hr.get_node('zzz')
print target_node


hr.add_node('node10')
print hr.get_nodes()

target_node = hr.get_node('zzz')
print target_node

hr.add_node('node11')
print hr.get_nodes()

#
# hr.remove_node('node4')
# target_node = hr.get_node('zzz')
# print target_node
#
#
#
# hr.remove_node('node5')
# target_node = hr.get_node('zzz')
# print target_node
#
#
# hr.remove_node('node2')
# target_node = hr.get_node('zzz')
# print target_node

