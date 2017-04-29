#!/usr/bin/env python2.7

import uuid

import imhere


host = '0.0.0.0'
port = 4156

print 'running on %s:%d' % (host, port)
imhere.app.secret_key = str(uuid.uuid4())
imhere.app.run(host=host, port=port)
