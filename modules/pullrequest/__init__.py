import os
import pyhub.libs.common as common
import config
import requests

def desc(*args, **argv):
    return "help pull request related operations"

def help(*args, **argv):
    print desc()

def list(*args, **argv):
    state='open'
    if len(args) > 0:
        state = args[0]
    if state not in ['all','open','closed']:
        print 'invalid arg[%s] for list'%(state)

    cwd = os.getcwd()
    github = common.getGithubUrl(cwd)
    if github is None:
        print 'Gimme a git-hub repo to start with'
        return;
    conf = config.get_config()
    if conf is not None and (len(conf.username) > 0 or len(conf.token) > 0):
        prurl = github.pr_url()
        r = requests.get(prurl,auth=(conf.username,conf.password),params={'state':state})
        if r.status_code == 200:
            for pr in r.json():
                print pr['url']
        elif r.status_code == 401:
            print 'authentication error. try git hub config'
    else:
        print 'please config authentication first'
