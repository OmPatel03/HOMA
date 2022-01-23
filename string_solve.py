from function_type import get_function_from_string
from setupvars import create_list
from answer import runScript
from answer import formatStringFromVars
from loadjson import *


def compute_word_problem(problemString):

    #
    #
    problemDict = getProblemDictionary()

    #
    # Decide what type of function the string denotes
    functionType = get_function_from_string(problemString)

    #
    # Seperate the Speech Speach string into it's key variables based on the type of function
    variableList = create_list(functionType, problemString)

    #
    # Exectue the function using the variables
    problemScript = (getFromKeyDict(functionType, "functionName", problemDict))
    result = runScript(problemScript, variableList)

    #
    # Create a stringified version to send back to the person.
    problemFormatString = getFromKeyDict(
        functionType, "formattedString", problemDict)
    problemVariablesToFill = getFromKeyDict(
        functionType, "formattedVariables", problemDict)
    problemVariableFormats = getFromKeyDict(
        functionType, "variableFormats", problemDict)
    formattedString = formatStringFromVars(
        problemFormatString, problemVariablesToFill, problemVariableFormats, result)

    print(formattedString)
    return formattedString


inputtedString = "Find the final amount if the principal amount is 2000 if the interest rate is 3% and is for 5 years. "
compute_word_problem(inputtedString)
