import argparse
import errno
import requests
import os, datetime
import time,json
import re
requests.packages.urllib3.disable_warnings()

# URL = "https://api.github.com/search/users?q=followers:%3E{MIN_FOLLOWERS}+sort:followers&per_page=100" "&page={page}"


def logger(msg):
        print '[%s][LOG] %s'%(datetime.datetime.now(),msg)

def collect_profiles(input_file,overwrite=False,log=logger,delay=2):
    downloaded = []

    output_dir = input_file.replace('.json', ' ')
    logger('Creating directory %s' % output_dir)
    try:
        os.mkdir(output_dir, 0o700)
    except OSError as error:
        if error.errno == errno.EEXIST:
            logger('Directory already exists')
        else:
            # This is the top level, and we have nothing else to do if we failed
            raise
    os.chdir(output_dir)

    count = 0 


    with open("../../"+input_file, 'r') as input_file:
        inputFile = json.load(input_file)
        total_count = inputFile['total_count'] 
        profiles = inputFile["items"]

    profiles = profiles[:10] 

    for p in profiles:
        profile_url = p['html_url']
        username = p['login']
        filename = username + ''

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
            log('[%d]/[%d]Downloading profile from URL %s' % (total_count-count,count,profile_url))
            try:
                page_html = requests.get(profile_url, verify=False).content
                with open(filename, 'wb') as f:
                    f.write(page_html)
                count += 1
            except error:
                print '[ERROR] Failed to download profile from URL %s (%s)' % (profile_url, error.reason)
                continue
            except IOError as error:
                print '[ERROR] Failed to save profile to file %s (%s)' % (filename, error.strerror)

            downloaded.append(username)
            time.sleep(delay)
        else:
            log('File : %s Already Exists. Skipping' % filename)
            count += 1

    return downloaded
