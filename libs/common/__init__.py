from git import *
import git
import logging
from objects import GitHub
def getGithubUrl(path):
    try:
        repo = Repo(path)
        origin = repo.remotes.origin
        return GitHub.from_url(origin.url)
    except:
        logging.exception("failed to get github url")
        pass
    return None
