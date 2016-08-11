import os
import sys

def get_file_list(dir_path):
    file_list = []
    cmd = "adb shell ls -al %s"%dir_path 
    fp = os.popen(cmd)
    info_list = fp.readlines()
    fp.close()
    for list in info_list:
        list = list.strip().split(" ")
        flag = list[0]
        fname = list[-1]
        fullname = "%s/%s"%(dir_path,fname)
        if fname == "." or fname == "..":
            continue
        if flag[0] == 'd':
            file_list += get_file_list(fullname)
        elif flag[0] == '-':
            print fullname
            file_list.append(fullname)
        else:
            continue
    return file_list
def check_path(fpath):
    if not os.path.exists(fpath):
        os.makedirs(fpath)
    


def get_file(src_path,dst_path):
    file_list = get_file_list(src_path)
    for f in file_list:
        fpath = os.path.dirname(f)
        fullpath = dst_path+fpath
        check_path(fullpath)
        cmd = "adb pull %s %s "%(f,fullpath)
        print cmd
        os.system(cmd)

def usage():
    print "Usage: python adb_pull_files.py src_path dest_path"
        
# we use this tool to get the files in the throught adb    
if __name__ == "__main__":
    #we get the file list
    if len(sys.argv)  == 3:
        #first we get the file list
        src_path = sys.argv[1]
        dst_path = sys.argv[2]
        get_file(src_path,dst_path)
    else:
        usage()
