#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
import socket
import fcntl
import struct

# DNSQuery class from http://code.activestate.com/recipes/491264-mini-fake-dns-server/
class DNSQuery:
  def __init__(self, data):
    self.data=data
    self.domain=''

    tipo = (ord(data[2]) >> 3) & 15   # Opcode bits
    if tipo == 0:                     # Standard query
      ini=12
      lon=ord(data[ini])
      while lon != 0:
        self.domain+=data[ini+1:ini+lon+1]+'.'
        ini+=lon+1
        lon=ord(data[ini])

  def respuesta(self, ip):
    packet=''
    if self.domain:
      packet+=self.data[:2] + "\x81\x80"
      packet+=self.data[4:6] + self.data[4:6] + '\x00\x00\x00\x00'   # Questions and Answers Counts
      packet+=self.data[12:]                                         # Original Domain Name Question
      packet+='\xc0\x0c'                                             # Pointer to domain name
      packet+='\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04'             # Response type, ttl and resource data length -> 4 bytes
      packet+=str.join('',map(lambda x: chr(int(x)), ip.split('.'))) # 4bytes of IP
    return packet



# get_ip_address code from http://code.activestate.com/recipes/439094-get-the-ip-address-associated-with-a-network-inter/
def get_ip_address(ifname):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  try:
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
  except:
    return None


def usage():
  print ""
  print '''使用办法：配置hosts文件，比如reader.xx.com 192.168.11.11;直接运行python minidns'''
  print ""

  sys.exit(1)


if __name__ == '__main__':

  if sys.argv[-1] == '-h' or sys.argv[-1] == '--help':
      usage()
  try:
    udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udps.bind(('',53))
  except Exception, e:
    print "Failed to create socket on UDP port 53:", e
    sys.exit(1)

  hosts = file('/etc/hosts').readlines()
  h = [l.strip().split() for l in hosts if l[0] in '123456789']
  ipdict = {}
  for item in h:
      for host in item[1:]:
          ipdict[host] = item[0]
  try:
    while 1:
      data, addr = udps.recvfrom(1024)
      print data,addr
      p=DNSQuery(data)
      print p.domain
      try:
        realip = ipdict.get(p.domain[:-1], socket.getaddrinfo(p.domain[:-1], 80)[0][4][0])
      except:
          pass
      udps.sendto(p.respuesta(realip), addr)

      print 'Request: %s -> %s' % (p.domain, realip)
  except KeyboardInterrupt:
    print '\nBye!'
    udps.close()
