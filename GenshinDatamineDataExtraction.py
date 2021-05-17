import os
import yaml

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

baseFileName = "processedGenshinDatamine"
configFileName = "config.yaml"

configKeys = list(read_yaml(configFileName).keys()) #extracts the keys to the config dictionary
parentDirKey = configKeys[0]
childeDirKey = configKeys[1]
childeFileNameKey = configKeys[2]
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import shutil # removes the folders this created from last time it ran just for ease while testing
shutil.rmtree(baseFileName, ignore_errors=True)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


def configDirSystem(configFile):
    directory = {}
    for i in range(len(read_yaml(configFile)[parentDirKey])): #i wrote this 2 seconds ago and forgot how it works but it creates the directory system as a dictionary called directory
        parentDir = read_yaml(configFile)[parentDirKey][i]
        subDirectory = []
        for j in range(len(read_yaml(configFile)[childeDirKey][read_yaml(configFile)[parentDirKey][i]])):
            subDirectory.append(read_yaml(configFile)[childeDirKey][read_yaml(configFile)[parentDirKey][i]][j])
        directory[parentDir] = subDirectory
    return(directory)
#NOTE TO FUTURE ME: either create lists from this dictionary or alter your code createDirs slightly
#this can be used to customise file names as well? (would have to change childDir to childFileNames)

def configFileSystem(configFile):
    directory = {}
    for i in range(len(read_yaml(configFile)[parentDirKey])): #creates the file system as a dictionary called directory
        parentDir = read_yaml(configFile)[parentDirKey][i]
        subDirectory = []
        for j in range(len(read_yaml(configFile)[childeFileNameKey][read_yaml(configFile)[parentDirKey][i]])):
            subDirectory.append(read_yaml(configFile)[childeFileNameKey][read_yaml(configFile)[parentDirKey][i]][j])
        directory[parentDir] = subDirectory
    return(directory)


def createDirs(dictionary):
    os.mkdir("./" + baseFileName)
    for i in range(len(dictionary)):
        os.mkdir("./" + baseFileName + "/" + list(dictionary.keys())[i])


#print(configFileSystem(configFileName))

createDirs(configDirSystem(configFileName))