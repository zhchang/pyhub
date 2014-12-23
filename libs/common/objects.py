import logging
class GitHub:
    user = ''
    repo = ''
    def __init__(self,user,repo):
        self.user = user
        self.repo = repo

    def git_url(self):
        return "git@github.com:%s/%s.git"%(self.user,self.repo)

    def http_url(self):
        return "https://github.com/%s/%s.git"%(self.user,self.repo)
    def pr_list_url(self):
        return "https://api.github.com/repos/%s/%s/pulls"%(self.user,self.repo)
    def pr_update_url(self, index):
        return "https://api.github.com/repos/%s/%s/pulls/%s"%(self.user,self.repo,index)

    @staticmethod
    def from_url(url):
        user = None
        repo =None
        if url.find("github.com") and url[-4:] == ".git":
            try:
                url = url[:-4]
                if url.find("git@github.com:") == 0:
                    parts = url.split(":")
                    parts = parts[1].split("/")
                    (user,repo)=(parts[0],parts[1])
                elif url.find("https://github.com") == 0:
                    url = url[8:]
                    parts = url.split("/")
                    (user,repo)=(parts[1],parts[2])
            except:
                logging.exception('git hub from url')
                pass
            if user is not None and repo is not None:
                return GitHub(user,repo)

        else:
            return None
