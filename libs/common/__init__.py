from git import *
import git
import logging
def getGithubUrl(path):
    try:
        repo = Repo(path)
        origin = repo.remotes.origin
        url = origin.url
        if url.find("github.com") != -1:
            return url
        else:
            return None
    except:
        logging.exception("failed to get github url")
        pass
    return None


