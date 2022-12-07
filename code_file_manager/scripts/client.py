#!/usr/bin/env python
from __future__ import print_function

import sys
import rospy
from code_file_manager.srv import codeFileManager,codeFileManagerResponse

def codeFileManager_client(opCode,fileName="",code=""):
    rospy.wait_for_service("code_file_manager")
    try:
        code_file_manager = rospy.ServiceProxy("code_file_manager",codeFileManager)
        resp1 = code_file_manager(opCode,fileName,code)
        return resp1.rsp
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s  [opCode] [fileName] [code]"%sys.argv[0]

if __name__ == "__main__":
    
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print(usage())
        sys.exit(1)
    elif len(sys.argv) == 2:
        if sys.argv[1] == "help":
            print("arguments -> [opCode] [fileName] [code]\nopCode -> save | delete | getFile | getFiles\nfileName -> optional, file name\ncode -> required with save, your code")
        else:
            opCode = sys.argv[1]
            print("rsp:\n",codeFileManager_client(opCode),sep="")
    elif len(sys.argv) == 3:
        opCode = sys.argv[1]
        fileName = sys.argv[2]+".py"
        print("rsp:\n",codeFileManager_client(opCode,fileName),sep="")
    else:
        opCode = sys.argv[1]
        fileName = sys.argv[2]+".py"
        code = sys.argv[3]
        print("rsp:\n",codeFileManager_client(opCode,fileName,code),sep="")
    
    