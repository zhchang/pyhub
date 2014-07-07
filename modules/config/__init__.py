import os,logging
from objects import Config

def desc(*args, **argv):
    return "do configs"

def help(*args, **argv):
    print "usage: git hub config user <user> pass <pass> token <token>"

def show():
    map = _loadcfg();
    print "saved configurations:"
    for key,value in map.iteritems():
        print "%s : %s"%(key,value)

def get_config():
    map = _loadcfg()
    config = Config(map)
    return config

def process(*args):
    try:
        if len(args) % 2 == 0:
            param_map = dict(zip(args[0::2],args[1::2]))
            map = _loadcfg()
            for key in ('user','pass','token'):
                if key in param_map:
                    map[key] = param_map[key]
            _writecfg(map)
            print 'configuration changes saved'
    except:
        logging.exception("invalid args")

def _loadcfg():
    map = {}
    try:
        file = open ('%s/.pyhub'%(os.path.expanduser('~')),'r')
        for line in file:
            if line.find('#') != 0:
                parts = line.rstrip().split("=")
                if len(parts) == 2:
                    map[parts[0]] = parts[1]
        file.close()
    except:
        pass
    return map

def _writecfg(map):
    try:
        file = open ('%s/.pyhub'%(os.path.expanduser('~')),'w+')
        for key,value in map.iteritems():
            file.write('%s=%s\n'%(key,value))
        file.close()
    except:
        pass
