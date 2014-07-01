def help():
    return "help pull request related operations"
def process(argv):
    if len(argv) >= 1:
        if argv[0] == "list":
            import list
            list.list()
    else:
        print help()
