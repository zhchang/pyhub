import os
import pyhub.libs.common as common
import config
import requests

def desc(*args, **argv):
    return "help pull request related operations"

def help(*args, **argv):
    print desc()

def list(*args, **argv):
    cwd = os.getcwd()
    github = common.getGithubUrl(cwd)
    if github is None:
        print 'Gimme a git-hub repo to start with'
        return;
    conf = config.get_config()
    if conf is not None:
        prurl = github.pr_url()
        r = requests.get(prurl,auth=(conf.username,conf.password),params={'state':'all'})
        for pr in r.json():
            print pr['url']

