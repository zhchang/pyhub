class GitHub:
    user = ''
    repo = ''
    def __init__(self,user,repo):
        self.user = user
        self.repo = repo

    def toGitUrl(self):
        return "git@github.com:%s/%s.git"%(self.user,self.repo)

    def toHttpUrl(self):
        return "https://github.com/%s/%s.git"%(self.user,self.repo)

    @staticmethod
    def fromUrl(url):
        user = None
        repo =None
        if url.find("github.com") and url[-4:] == ".git":
            try:
                url = url[:-4]
                if url.find("git@github.com:") == 0:
                    parts = url.split(":")
                    parts = parts[1].split("/")
                    print parts
                    (user,repo)=(pars[0],parts[1])
                elif url.find("https://github.com") == 0:
                    url = url[8:]
                    parts = url.split("/")
                    (user,repo)=(parts[1],parts[2])
            except:
                pass
            if user is not None and repo is not None:
                return GitHub(user,repo)

        else:
            return None
