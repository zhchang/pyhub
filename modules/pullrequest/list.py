import os
import pyhub.libs.common as common

def list():
    cwd = os.getcwd()
    github = common.getGithubUrl(cwd)
    if github is not None:
        print "user: %s, repo:%s"%(github.user,github.repo)

