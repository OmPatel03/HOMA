import json
import os

def getProblemDictionary():

    #Initialize
    problemDict = {};

    #Get The Current Folder Path + Find the Dictonary
    directoryPath = os.getcwd()
    jsonFileLocation = directoryPath + "\problemdict.json";

    #Open File + Load
    with open(jsonFileLocation, "r") as f:
        problemDict = json.load(f);

    #Return Dictonary
    return problemDict;

def getFromKeyDict(key, subkey, dictt = getProblemDictionary()):
    result = dictt[key][subkey];
    return result;