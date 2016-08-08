1.解析http字符串

try:
    from urlparse import urlparse,urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin


2.实例
2.1 urlparse

>>> url = 'https://note.wiz.cn/web?dc=5c41cbd3-8f48-0438-1299-cce59eaaaa36&cmd=ca%2C%2Fffmpeg%2F&kb=2837fe6c-bb31-44f4-983f-530dc2f62b47'
>>> url
'https://note.wiz.cn/web?dc=5c41cbd3-8f48-0438-1299-cce59eaaaa36&cmd=ca%2C%2Fffmpeg%2F&kb=2837fe6c-bb31-44f4-983f-530dc2f62b47'
>>> u = urlparse(url)
>>> u
ParseResult(scheme='https', netloc='note.wiz.cn', path='/web', params='', query='dc=5c41cbd3-8f48-0438-1299-cce59eaaaa36&cmd=ca%2C%2Fffmpeg%2F&kb=2837fe6c-bb31-44f4-983f-530dc2f62b47', fragment='')
>>> u.hostname
'note.wiz.cn'

2.2 urljoin
>>>urljoin("http://tt.com", "ffff")
'http://tt.com/ffff'
>>> urljoin("http:", "ffff")
'http:///ffff'
>>> urljoin("http://", "ffff")
'http:///ffff'
>>> urljoin("http://t", "ffff")
'http://t/ffff'





