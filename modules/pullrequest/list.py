import os
import git

def list():
    cwd = os.getcwd()
    repo = git.Repo(cwd)
