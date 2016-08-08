#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys, os
import socket, json, binascii

import tornado.httpserver
import tornado.ioloop
import tornado.iostream
import tornado.web
import tornado.httpclient
import tornado.escape

__all__ = ['ProxyHandler', 'run_proxy']


class HttpArchive():
  """
  >>> a = HttpArchive("GET http://a.com HTTP/1.1", "Host: g1.163.com", "", "Content-Encoding: gzip", "")
  >>> a.request
  'GET http://a.com HTTP/1.1'
  >>> b = HttpArchive.parse(a.dumps())
  >>> a.__dict__ == b.__dict__
  >>> a == b
  True
  >>> a.request == b.request
  True
  >>> a.request_header == b.request_header
  True
  >>> a.response_header == b.response_header
  True
  >>> a.response_body == b.response_body
  True
  """

  def __init__(self, r, h1, b1, h2, b2):
    self.request = r
    self.request_header = h1
    self.request_body = b1
    self.response_header = h2
    self.response_body = b2

  def dumps(self):
    return json.dumps({
      "request":self.request,
      "reqeust_header": self.request_header,
      "reqeust_body": (self.request_body and binascii.hexlify(self.request_body) or ''),
      "response_header":  self.response_header,
      "response_body":  (self.response_body and binascii.hexlify(self.response_body) or ''),
      })

  @staticmethod
  def parse(s):
    try:
      j = json.loads(s)
      return HttpArchive(j['request'], 
        j['reqeust_header'], 
        binascii.unhexlify(j['reqeust_body']),
        j['response_header'],
        binascii.unhexlify(j['response_body']))
    except:
      return HttpArchive('', {}, '', {}, '')


class ProxyHandler(tornado.web.RequestHandler):
    SUPPORTED_METHODS = ['GET', 'POST', 'CONNECT']
    HISTORY = []
    NEXTID = 1

    @staticmethod
    def nextid():
      ProxyHandler.NEXTID += 1
      return ProxyHandler.NEXTID

    @staticmethod
    def log(uri, headers, body):
      i = ProxyHandler.nextid()

      if True:#request.uri.startswith('http://mp.weixin.qq.com'):
          ProxyHandler.HISTORY.append((uri, i))
          if len(ProxyHandler.HISTORY) > 1000:
            ProxyHandler.HISTORY.pop()
          with open("raw/%06d" % i, "wb") as f:
            for k,v in headers.iteritems():
              f.write('%s: %s\n' % (k,v))

            f.write('\n')
            f.write(body)

      if len(ProxyHandler.HISTORY) > 200:
        ProxyHandler.HISTORY = ProxyHandler.HISTORY[:100]

    @staticmethod
    def log2(request, response):
      i = ProxyHandler.nextid()

      if True:#request.uri.startswith('http://mp.weixin.qq.com'):
          ProxyHandler.HISTORY.append((request.uri, i))
          with open("raw/%06d" % i, "wb") as f:
            a = HttpArchive("%s %s" % (request.method, request.uri),
                request.headers,
                request.body,
                response.headers,
                response.body)
            f.write(a.dumps())

    @tornado.web.asynchronous
    def get(self):
        if not self.request.uri.startswith('/'):
          print self.request.method, self.request.uri

        # list
        if self.request.uri == '/' or self.request.uri == '/index.html':
          for k,v in reversed(ProxyHandler.HISTORY):
            self.write('<li><a href="/p/%06d/%s">%s</a>\n' % (v, k, k))
          self.finish()
          return
        # item => /p/{id}/{url}
        elif self.request.uri.startswith('/p/'):
          i = int(self.request.uri.split('/')[2])
          har = HttpArchive.parse(open("raw/%06d" % i, 'r').read())
          
          content_type = har.response_header.get('Content-Type', 'text/html;charset=utf-8')

          if content_type.find('text/html') != -1:
            self.set_header("Content-Type", content_type)
          else:
            self.set_header("Content-Type", "text/html;charset=utf-8")

          self.write('%s<br /><br />' % har.request)

          for k,v in har.request_header.iteritems():
            self.write('%s: %s<br />\n' % (k, v))

          self.write('<br />\n')
          self.write(tornado.escape.xhtml_escape(har.request_body))

          self.write('<hr />')

          for k,v in har.response_header.iteritems():
            self.write('%s: %s<br />\n' % (k, v))
          
          if content_type.find('image') != -1:
            self.write('<img src="/raw/%06d" />' % i)
          elif content_type.find('binary') != -1:
            pass
          else:
            self.write('<br />\n')
            self.write(tornado.escape.xhtml_escape(har.response_body))
          self.finish()
          return
        # raw, response_body
        elif self.request.uri.startswith('/raw/'):
          i = int(self.request.uri.split('/')[2])
          har = HttpArchive.parse(open("raw/%06d" % i, 'r').read())
          self.set_header("Content-Type", har.response_header['Content-Type'])
          self.write(har.response_body)
          self.finish()
          return
        # raw, request_body
        elif self.request.uri.startswith('/rraw/'):
          i = int(self.request.uri.split('/')[2])
          har = HttpArchive.parse(open("raw/%06d" % i, 'r').read())
          # self.set_header("Content-Type", har.request_header['Content-Type'])
          self.write(har.request_body)
          self.finish()
          return

        def handle_response(response):
            if response.error and not isinstance(response.error,
                    tornado.httpclient.HTTPError):
                self.set_status(500)
                self.write('Internal server error:\n' + str(response.error))
                self.finish()
            else:
                self.log2(self.request, response)
                if response.code == 599:
                  self.set_status(500)
                else:
                  self.set_status(response.code)
                for header in ('Date', 'Cache-Control', 'Server',
                        'Content-Type', 'Location'):
                    v = response.headers.get(header)
                    if v:
                        self.set_header(header, v)
                if response.body:
                    self.write(response.body)
                self.finish()

        req = tornado.httpclient.HTTPRequest(url=self.request.uri,
            method=self.request.method, body=self.request.body,
            headers=self.request.headers, follow_redirects=False,
            allow_nonstandard_methods=True)

        client = tornado.httpclient.AsyncHTTPClient()
        try:
            client.fetch(req, handle_response)
        except tornado.httpclient.HTTPError as e:
            if hasattr(e, 'response') and e.response:
                handle_response(e.response)
            else:
                self.set_status(500)
                self.write('Internal server error:\n' + str(e))
                self.finish()

    @tornado.web.asynchronous
    def post(self):
        return self.get()

    @tornado.web.asynchronous
    def connect(self):
        host, port = self.request.uri.split(':')
        client = self.request.connection.stream

        def read_from_client(data):
            upstream.write(data)

        def read_from_upstream(data):
            client.write(data)

        def client_close(data=None):
            if upstream.closed():
                return
            if data:
                upstream.write(data)
            upstream.close()

        def upstream_close(data=None):
            if client.closed():
                return
            if data:
                client.write(data)
            client.close()

        def start_tunnel():
            client.read_until_close(client_close, read_from_client)
            upstream.read_until_close(upstream_close, read_from_upstream)
            client.write(b'HTTP/1.0 200 Connection established\r\n\r\n')

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        upstream = tornado.iostream.IOStream(s)


        upstream.connect((host, int(port)), start_tunnel)


def run_proxy(port, start_ioloop=True):
    """
    Run proxy on the specified port. If start_ioloop is True (default),
    the tornado IOLoop will be started immediately.
    """
    settings = dict(
      # cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
      # login_url="/auth/login",
      template_path=os.path.join(os.path.dirname(__file__), "templates"),
      # static_path=os.path.join(os.path.dirname(__file__), "static"),
      # xsrf_cookies=True,
      debug=False,
      gzip=True,
      # autoescape=None,
    )

    if not os.path.exists('raw'):
      os.mkdir('raw')

    app = tornado.web.Application([
        (r'.*', ProxyHandler),
    ], **settings)
    app.listen(port)
    if start_ioloop:
      ioloop = tornado.ioloop.IOLoop.instance()
      ioloop.start()

if __name__ == '__main__':
    port = 8888
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    print ("Starting HTTP proxy on port %d" % port)
    run_proxy(port)
