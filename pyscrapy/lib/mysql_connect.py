
import MySQLdb

class MySQL():
    def db(self):
        yield MySQLdb.connect("mobile.idc.com", "root", "123456", "mobile")