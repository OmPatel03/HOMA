import json
import os

def getProblemDictionary():

    #Initialize
    problemDict = {};

    #Get The Current Folder Path + Find the Dictonary
    directory_path = os.getcwd()
    jsonFileLocation = directory_path + "\problemdict.json";

    #Open File + Load
    with open(jsonFileLocation, "r") as f:
        problemDict = json.load(f);

    #Return Dictonary
    return problemDict;