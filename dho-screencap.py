#!/usr/bin/env python

'''
Integrates Mac OS X's screenshot utility with DreamObjects for easy sharing.
'''

from datetime import datetime
from uuid import uuid4

import os
import subprocess
import webbrowser

import boto
import boto.s3.connection

cname = 'snap.coderpete.net'

# configuration
f = open('.dho_access', 'r')
dho_access = f.readlines
[
    dho_access_key,
    dho_secret_key,
    dho_screenshots_bucket
] = [
    l.strip() for l in f.readlines()
]

# other variables
now = datetime.now()
this_month = datetime.strftime(now, '%Y%m')
tstamp = datetime.strftime(datetime.now(), '%d%H%M%S')

filename = this_month + '/' + tstamp + '_' + str(uuid4())[-4:] + '.png'

# start interactive screen capture
if not os.path.exists('/tmp/' + this_month):
    os.mkdir('/tmp/' + this_month)
subprocess.call(['screencapture', '-i', '/tmp/%s' % filename])

print 'Screenshot captured! Copying to DreamObjects...'

connection = boto.connect_s3(
    aws_access_key_id=dho_access_key,
    aws_secret_access_key=dho_secret_key,
    host='objects.dreamhost.com'
)

bucket = connection.get_bucket(dho_screenshots_bucket)
key = bucket.new_key(filename)
key.set_contents_from_file(open('/tmp/%s' % filename, 'rb'))
key.set_canned_acl('public-read')

public_url = cname + '/' + filename
# or if you don't have a cname
#public_url = key.generate_url(0, query_auth=False, force_http=True)

print 'Screenshot available at:'
print '\t', public_url

os.system('echo "http://%s" | pbcopy' % public_url)
webbrowser.open_new_tab('http://' + public_url)
