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


# configuration
f = open('.dho_access', 'r')
# required
dho_access_key = f.readline().strip()
dho_secret_key = f.readline().strip()
dho_screenshots_bucket = f.readline().strip()
# optional
cname = f.readline().strip()

# other variables
now = datetime.now()
this_month = datetime.strftime(now, '%Y%m')
tstamp = datetime.strftime(datetime.now(), '%d%H%M%S')

filename = this_month + '/' + tstamp + '_' + str(uuid4())[-4:] + '.png'

# start interactive screen capture
print 'Capturing screenshot...'
if not os.path.exists('/tmp/' + this_month):
    os.mkdir('/tmp/' + this_month)
subprocess.call(['screencapture', '-i', '/tmp/%s' % filename])

print 'Connecting to DreamObjects...'
connection = boto.connect_s3(
    aws_access_key_id=dho_access_key,
    aws_secret_access_key=dho_secret_key,
    host='objects.dreamhost.com'
)

print 'Getting target bucket...'
bucket = connection.get_bucket(dho_screenshots_bucket)
key = bucket.new_key(filename)
print 'Uploading to DreamObjects...'
key.set_contents_from_file(open('/tmp/%s' % filename, 'rb'))
key.set_canned_acl('public-read')

public_url = ''
if cname == '':
    public_url = key.generate_url(0, query_auth=False, force_http=True)
else:
    public_url = 'http://' + cname + '/' + filename

print 'Screenshot available at:'
print '\t', public_url

print 'Copying url to clipboard...'
os.system('echo "%s" | pbcopy' % public_url)
print 'Opening in browser...'
webbrowser.open_new_tab(public_url)
