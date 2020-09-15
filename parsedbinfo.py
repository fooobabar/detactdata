from configparser import ConfigParser

class dbInfo(object):

    def __init__(self):
        config=ConfigParser()
        config.read("dbinfo.ini")
        self.dbinfo=config

    def listDbname(self):
        return self.dbinfo.sections()

    def getUsername(self,dbname:str):
        return self.dbinfo.get(dbname,"USERNAME")

    def getPassword(self,dbname:str):
        return self.dbinfo.get(dbname,"PASSWORD")

    def getEstns(self,dbname:str):
        return self.dbinfo.get(dbname,"ESTNS")
