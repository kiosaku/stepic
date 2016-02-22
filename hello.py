import urlparse

def app(environ, start_response):
  response_body = ''
  a = environ['QUERY_STRING']
  response_body = a.replace('&','\r\n')
#  d = urlparse.parse_qs(environ['QUERY_STRING'])
#  for key, value in sorted(d.iteritems()):
#    value_join = ''.join(value)
#    response_body += key + '=' + str(value) + '\n'
#    response_body += key + '=' + value_join + '\n'
  start_response('200 OK', [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))])
  return[response_body]

