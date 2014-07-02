import os
import pyhub.libs.common as common

def desc(*args, **argv):
    return "help pull request related operations"

def help(*args, **argv):
    print desc()

def list(*args, **argv):
    print args
    print "Here list all pull request"
    cwd = os.getcwd()
    github = common.getGithubUrl(cwd)
    if github is not None:
        print "user: %s, repo:%s"%(github.user,github.repo)
