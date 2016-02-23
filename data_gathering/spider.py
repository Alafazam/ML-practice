import argparse
import errno
import requests
import os, datetime
import time,json
import re

from fetch_user import *
from fetch_repo_metadata import *
from collect_profiles import *

_basedir = os.path.abspath(os.path.dirname(__file__))

def log_if_v(msg):
    if args.verbose:
        print '[DEBUG] %s'%(msg)
    else:
        print '[LOG] %s'%(msg)

print 'strarted at',datetime.datetime.now()

parser = argparse.ArgumentParser(description = 'Download Profile and Repo details from github')

parser.add_argument('input_file',default='users.json', help='file containing JSON-encoded list of URLs to download')

parser.add_argument('-t', '--type_of_action', default='collect_list', help='Type of action to perform')

parser.add_argument('-q', '--output_dir', nargs='?', default='./crawled', help='where to store the downloaded profiles and repo metadata')
parser.add_argument('-d', '--delay', default=2, type=float, help='Time to sleep between requests, in seconds')
parser.add_argument('-v', '--verbose', default=False,action='store_true', help='enable debug messages')
parser.add_argument('-o', '--overwrite', default=False, action='store_true', help='Overwrite existing repo data')

global args
args = parser.parse_args()

log_if_v('Creating directory %s' % args.output_dir)
try:
    os.mkdir(args.output_dir, 0o700)
except OSError as error:
    if error.errno == errno.EEXIST:
        log_if_v('Directory already exists')
    else:
        # This is the top level, and we have nothing else to do if we failed
        raise
os.chdir(args.output_dir)

# Load the list of URLs from the input file.
if args.type_of_action == 'simple':
    log_if_v('Loading input file %s' % args.input_file)
    with open(args.input_file, 'r') as input_file:
        inputFile = json.load(input_file)
        profiles = inputFile["users"]
        repos =  inputFile["repositories"]
    print 'Found %d profiles and %d repos' % (len(profiles),len(repos))
    downloaded = get_users(profiles)
    # profiles = profiles[:10]
    # downloaded,users = get_repo_metas(repos)
    print downloaded

elif args.type_of_action == 'collect_list':
    log_if_v('Collecting profiles from API made json file')
    collect_profiles(input_file=args.input_file)


