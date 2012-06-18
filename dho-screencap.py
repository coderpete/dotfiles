#!/usr/bin/env python

'''
Integrates Mac OS X's screenshot utility with DreamObjects for easy sharing.
'''

from datetime import datetime

import os
import subprocess
import webbrowser

import boto
import boto.s3.connection


# configuration
dho_access_key = 'PASTE_YOUR_S3_PUBLIC_KEY'
dho_secret_key = 'PASTE_YOUR_S3_SECRET_KEY'
dho_screenshots_bucket = 'screencapture'

# other variables
filename = datetime.strftime(datetime.now(), '%m-%d-%Y-%H-%M-%S') + '.png'

# start interactive screen capture
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

public_url = key.generate_url(0, query_auth=False, force_http=True)

print 'Screenshot available at:'
print '\t', public_url

os.system('echo "%s" | pbcopy' % public_url)
webbrowser.open_new_tab(public_url)
