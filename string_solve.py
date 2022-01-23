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
    try:
        functionType = get_function_from_string(problemString)

        #
        # Seperate the Speech Speach string into it's key variables based on the type of function
        variableList = create_list(functionType, problemString)

        #
        # Exectue the function using the variables
        problemScript = (getFromKeyDict(
            functionType, "functionName", problemDict))
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

    # Overrall Error Handeling
    except Exception:
        return "I cannot answer that type of question."


print(compute_word_problem("Maximize the revenue if the ticket price is $6 and the original number of 2000 people decrease by a 100 every increase of $1 in ticket price"))
