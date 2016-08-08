import tempfile
import urllib2
import time
import os
import shutil

def get_tmp_file(prefix='img_', suffix='.jpg', dir='/tmp'):
    tmp = tempfile.NamedTemporaryFile(prefix=prefix, suffix=suffix, dir=dir, delete=False)
    return tmp.name


def url2tmp(url):
    assert url
    img_data = urllib2.urlopen(url)
    tmp_file = get_tmp_file()
    with open(tmp_file, 'wb') as f:
        f.write(img_data.read())
    return tmp_file


def copy2file(file, prefix="/mnt/mfs"):
    now = time.strftime("%Y/%m%d")
    dir = os.path.join(prefix, "ms/%s" % now)
    dir = get_tmp_file('ms', '', dir)
    if not dir:
        os.makedirs(dir)
    dest_file = os.path.join(dir, os.path.basename(file))
    shutil.copy(file, dest_file)
    if os.path.exists(file):
        os.remove(file)
    return dest_file.replace(prefix, "")


if __name__ == '__main__':
    f = url2tmp()