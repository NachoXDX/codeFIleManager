#!/usr/bin/env python

from __future__ import print_function
from code_file_manager.srv import codeFileManager,codeFileManagerResponse
import rospy
import os, errno
def handle_code_file_manager(req):
        absoluteCodeFilesFolderPath = "/home/niryo/rutinasProgTextual/"
        req.opCode = req.opCode.lower()
        if req.opCode == "save":

            path = absoluteCodeFilesFolderPath + req.fileName
            try:
                with open(path,"w") as file:
                    file.write(req.code)
            except:
                print("Error")
                return codeFileManagerResponse("error")
            else:
                print("Code:\n",req.code,sep="")
                return codeFileManagerResponse("saved")

        elif req.opCode == "delete":

            try: 
                os.remove(absoluteCodeFilesFolderPath + req.fileName)
            except OSError as e:
                    if e.errno == errno.ENOENT:
                        print("File not found!")
                        return codeFileManagerResponse("file not found")
                    else:
                        print("Error!")
                        return codeFileManagerResponse("error")
            else:
                print("Deleted!")
                return codeFileManagerResponse("deleted")

        elif req.opCode == "getfiles":
            try:
                files = "|".join((os.listdir(absoluteCodeFilesFolderPath)))   #str de los archivos separados por |
            except OSError as e:
                if e.errno == errno.ENOENT:
                    print("File not found!")
                    return codeFileManagerResponse("file not found")
                else:
                    print("Error!")
                    return codeFileManagerResponse("error") 
            else:
                print(files)
                return codeFileManagerResponse(files) 

        elif req.opCode == "getfile":

            path = absoluteCodeFilesFolderPath + req.fileName
            code = ""
            try:
                with open(path) as file:
                    for line in file:
                        code += line
            except OSError as e:
                if e.errno == errno.ENOENT:
                    print("File not found")
                    return codeFileManagerResponse("file not found")
                else:
                    print("Error!")
                    return codeFileManagerResponse("error")
            else:
                print("code:\n",code,sep="")
                return codeFileManagerResponse(code)
        else:
            print("invalid opCode")
            return codeFileManagerResponse("invalid opCode")

def code_file_manager_server():
    rospy.init_node("code_file_manager_server")
    s = rospy.Service("code_file_manager", codeFileManager, handle_code_file_manager)
    print("Code File Manager node Ready!")
    rospy.spin()

if __name__ == "__main__":
    code_file_manager_server()