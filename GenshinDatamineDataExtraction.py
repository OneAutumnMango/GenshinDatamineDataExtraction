import os

try:
    import yaml
except ModuleNotFoundError:
    print("""
        Error: ModuleNotFoundError

        Please install PyYAML before trying again.

        Enter "pip install PyYAML" into your command prompt
    """)
    input("\n\nPress Enter to Confirm and Exit")
    exit()

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


configFileName = "config.yaml"

configKeys = list(read_yaml(configFileName).keys()) #extracts the keys to the config dictionary
baseFileName = read_yaml(configFileName)[configKeys[0]]
parentDirKey = configKeys[1]
childeFileNameKey = configKeys[2]
#there should be a better way to do this ^


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import shutil # removes the folders this created from last time it ran, so you can update shit
shutil.rmtree(baseFileName, ignore_errors=True)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


def configDirSystem(configFile):
    directory = []
    for i in range(len(read_yaml(configFile)[parentDirKey])): #i wrote this 2 seconds ago and forgot how it works but it creates the directory system as a dictionary called directory
        directory.append(read_yaml(configFile)[parentDirKey][i])
    return(directory)


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
        os.mkdir("./" + baseFileName + "/" + dictionary[i])


createDirs(configDirSystem(configFileName))