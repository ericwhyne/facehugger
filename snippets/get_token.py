#!/usr/bin/python
# coding: utf-8
import facebook
import yaml
import argparse
import os

parser = argparse.ArgumentParser(description="")
parser.add_argument('-t', dest='token_file', default=os.path.expanduser("~") + "/.facehugger/default.yaml",
                    help='A configuration file with Facebook API access tokens. See example_token_file.yaml.')
args = parser.parse_args()

tokens = yaml.safe_load(open(args.token_file))
print tokens['FACEBOOK_APP_ID']
print tokens['FACEBOOK_APP_SECRET']
