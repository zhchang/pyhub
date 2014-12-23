from git import *
import git
import logging
from objects import GitHub
import requests
def git_hub(path):
    try:
        repo = Repo(path)
        origin = repo.remotes.origin
        return GitHub.from_url(origin.url)
    except:
        logging.exception("failed to get github url")
        pass
    return None

def http(*args,**argv):

