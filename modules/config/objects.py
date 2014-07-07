class Config:
    username=''
    password=''
    token=''
    def __init__(self,map):
        if 'user' in map:
            self.username = map['user']
        if 'pass' in map:
            self.password = map['pass']
        if 'token' in map:
            self.token = map['token']


    def __str__(self):
        print "%s|%s|%s"%(self.username,self.password,self.token)



