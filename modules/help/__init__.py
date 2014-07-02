import os

def desc(*args, **argv):
    return "get all help"

def help(*args, **argv):
    path = os.path.dirname(os.path.dirname(__file__))
    print 'available modules:'
    
    for subdir, dirs, files in os.walk(path):
        for dir in dirs:
            try:
                module = __import__(dir)
                try:
                    print "[%s] - %s"%(dir,module.desc())
                except:
                    pass
            except:
                pass
