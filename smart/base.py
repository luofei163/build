'''
Created on 2013-7-25

@author: Luo Fei
'''
import ConfigParser


con = ConfigParser.ConfigParser()
con.read('smart.conf')
print con.get('build', 'auto')
print con.get('koji','hub')



def add_job():
    pass

def do_job():
    pass

def isbuilded():
    pass

