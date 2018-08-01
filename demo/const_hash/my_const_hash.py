from hash_ring import *


memcache_servers = ['192.168.0.246:11212', '192.168.0.247:11212', '192.168.0.249:11212']

ring = HashRing(memcache_servers)

