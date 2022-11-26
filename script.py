import os
import json
import shutil
import sys

pattern="test"

# function that gives back a list of directory paths that contains the given pattern in it 
def find_pattern_dir_path(source_path):
    pattern_paths=[]

    for _,dirs,_ in os.walk(source_path): #os.walk gives back root,directorys,files in the path that was passed to it
        for directory in dirs:
            if pattern in directory.lower(): #checking directorys that matches with the pattern if so add its path to patter_paths
                path = os.path.join(source_path,directory) #adding together source_path/directory
                pattern_paths.append(path)
        break

    return pattern_paths

# function that gives back the name of directory from its path and strip off the words that we dont need in the name
def get_name_from_paths(paths,strip_off):
    new_names=[]
    for path in paths:
        _,dir_name =os.path.split(path) #to get the directory name from the path,os.splite gives back the string before the last \ and the string after it
        new_dir_name= dir_name.replace(strip_off,"") #to stip off word from the directory name
        new_names.append(new_dir_name)

    return new_names

#function that make new directory in the given path
def create_dir(path):
    if not os.path.exists(path): #making sure that the directory doesnt already exists
        os.mkdir(path)

#function that copy the directory and all of its insides into the new directory   
def copy(source,dest):
    if os.path.exists(dest): #checking if the directory exists to recursively deleting it
        shutil.rmtree(dest)
    
    shutil.copytree(source,dest) #recursively copying the directory into the new directory

#making json file that contains some data about the directory names and its number
def make_json_data_file(json_path,pattern_dirs):
    data={
        "{}DirectoryNames".format(pattern.capitalize()):pattern_dirs,
        "NumberOf{}Directorys".format(pattern.capitalize()):len(pattern_dirs)
    }
    with open(json_path,"w") as f: #open json file
        json.dump(data,f) #save data into the json file

def main(source,target):
    cwd=os.getcwd() #geting the current working directory
    source_path=os.path.join(cwd,source) #getting source path by adding cwd and source directory name
    target_path=os.path.join(cwd,target) #getting target path by adding cwd and destination(target) directory name

    pattern_path= find_pattern_dir_path(source_path) #list of directory paths
    new_pattern_dirs=get_name_from_paths(pattern_path,"_test") #list of driectory names

    create_dir(target_path)

    for src,dest in zip(pattern_path,new_pattern_dirs): #zip gives back a tuple that compine each element of pattern_path with the corresponding new_pattern_dirs
        dest_path=os.path.join(target_path,dest)
        copy(src,dest_path) #copy directorys from source path to inside the target path 

    json_path=os.path.join(target_path,"data.json")
    make_json_data_file(json_path,new_pattern_dirs)

if __name__ == "__main__":
    args=sys.argv #to deal arguments 
    if len(args) != 3: # making sure only 2 arguments are passed
        raise Exception("You must enter source and target directory -only 2 arguments, source first then target")
    
    source, target=args[1:] # saveing the arguments value into source and target
    main(source,target)
