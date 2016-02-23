import argparse
import errno
import requests
import os, datetime
import time,json
import re
requests.packages.urllib3.disable_warnings()

def logger(msg):
        print '[%s][LOG] %s'%(datetime.datetime.now(),msg)

def get_repo_metas(urls, output_dir='repositories', overwrite=False, log=logger, delay=2):
    log('Creating directory %s' % output_dir)
    try:
        os.mkdir(output_dir, 0o700)
    except OSError as error:
        if error.errno == errno.EEXIST:
            log('Directory already exists')
        else:
            # This is the top level, and we have nothing else to do if we failed
            raise
    os.chdir(output_dir)

    downloaded = []
    usernames = []

    for e in urls:
        url = e

        urlparts = url.split('/')
        username = urlparts[3]
        
        if username not in usernames:
            usernames.append(username)

        reponame = urlparts[4]

        filename = username + '___'

        if not reponame is None:
            filename += reponame
        else:
            print '[ERROR] Could not find repo part of URL %s; skipping' % (url)
            continue

        # Trim the filename if it's too long. 255 bytes is the limit on many filesystems.
        total_length = len(filename + '.html')
        
        if len(filename + '.html') > 255:
            filename = filename[:(255 - len(filename + '.html'))]
            log('Filename was truncated to 255 characters.')
        
        filename += '.html'
        log('Filename: %s' % filename)
        # If overwrite is enabled or the repo doesn't exist
        if overwrite or not os.path.isfile(filename):
            # Fetch the URL to find the repo
            log('Downloading answer from URL %s' % url)
            try:
                page_html = requests.get(url,verify=False).content
                with open(filename, 'wb') as f:
                    f.write(page_html)
            except error:
                print '[ERROR] Failed to download answer from URL %s (%s)' % (url, error.reason)
                continue
            except IOError as error:
                print '[ERROR] Failed to save answer to file %s (%s)' % (filename, error.strerror)

            downloaded.append(filename)

            time.sleep(delay)
        else:
            log('Answer File : %s Already Exists. Skipping' % filename)

    return downloaded,usernames