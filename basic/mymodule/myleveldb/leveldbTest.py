# -*- coding: utf-8 -*-
import leveldb

# https://code.google.com/p/py-leveldb/
#

db = leveldb.LevelDB('./db')

# single put
db.Put('hello', 'world')
print db.Get('hello')

# single delete
db.Delete('hello')
print db.Get('hello')


# multiple put/delete applied atomically, and committed to disk
batch = leveldb.WriteBatch()
batch.Put('hello', 'world1')
batch.Put('hello again', 'world')
batch.Delete('hello')

db.Write(batch, sync=True)





