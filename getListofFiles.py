#!/usr/bin/python
import sys,zipfile,pdb,os,datetime,csv


class parseDir(object):
        def __init__(self,path):
                self.path = path

        def dirContent(self, path):
                id_dict = {}
                for cfile in os.listdir(path):
                        cfilePath = os.path.join(path,cfile)
                        if os.path.isdir(cfilePath):
                                self.dirContent(cfilePath)
                        else:
                                print(cfilePath)

if __name__ == "__main__":
        if len(sys.argv) > 1:
                parse = parseDir(sys.argv[1])
                parse.dirContent(sys.argv[1])
        else:
                print "Please Provide the directory name at run time"
