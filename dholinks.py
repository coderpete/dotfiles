#!/usr/bin/env/python

'''
Prints shareable links for a "folder"
'''

import urllib2
import boto
import boto.s3.connection
import sys

from os.path import expanduser

prefix = sys.argv[1]

# configuration
# create a `.dho_access` file in your home dir
# paste the access key on the first line
# paste the secret key on the second line
# paste the bucket name on the third line
f = open('%s/.dho_access' % expanduser("~"), 'r')
# required
dho_access = f.readline().strip()
dho_secret = f.readline().strip()
dho_bucket = f.readline().strip()


print 'Connecting to DreamObjects...'
connection = boto.connect_s3(
    aws_access_key_id=dho_access,
    aws_secret_access_key=dho_secret,
    host='objects-us-east-1.dream.io'
)

print 'Getting bucket %s...' % dho_bucket
bucket = connection.get_bucket(dho_bucket)

print 'Getting objects prefixed "%s"' % prefix
key_iter = bucket.list(prefix=prefix)

for key in key_iter:
    print key
    signed_url = key.generate_url(
        expires_in=60*60*24*14,
        query_auth=True,
        force_http=True
    )
    print signed_url
