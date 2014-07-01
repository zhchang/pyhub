import os
import pyhub.libs.common as pcommon

def list():
    cwd = os.getcwd()
    url = pcommon.getGithubUrl(cwd)
    if url is not None:
        print "grabbing information from %s"%(url)

