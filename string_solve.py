from function_type import get_function_from_string
from setupvars import create_list
from answer import *
from loadjson import *


def compute_word_problem(problemString):

    #
    #
    problemDict = getProblemDictionary()

    #
    # Decide what type of function the string denotes
    try:
        functionType = get_function_from_string(problemString)
        print("Function type identified")

        #Unknown
        if (functionType == "I do not know what the problem is asking me to do"):
            return functionType

        #
        # Seperate the Speech Speach string into it's key variables based on the type of function
        variableList = create_list(functionType, problemString)
        print("Variable list created")

        #
        # Exectue the function using the variables
        problemScript = (getFromKeyDict(
            functionType, "functionName", problemDict))
        result = runScript(problemScript, variableList)
        print("Variable result calculated")

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

        #Collect Variables Into a Dictonary
        variableNames = list(getFromKeyDict(functionType, "variable_keywords", problemDict).keys())
        answerVarDict = answer_create_variable_name_dict(variableNames, variableList)

        finalResult = (formattedString, answerVarDict)
        return finalResult

<<<<<<< HEAD
    # Overrall Error Handeling
    except Exception:
        return "I cannot answer that type of question."


print(compute_word_problem("Maximize the revenue if the ticket price is $6 and the original number of 2000 people decrease by a 100 every increase of $1 in ticket price"))
=======
    #Overrall Error Handeling
    except Exception as e:
        return "I cannot answer that type of question."

test = "if for every 1 dollar increase there will be 10 less people that buy the porduct and if the product costs 5 dollars originally and 10 people buy it now, maximum revenue"
print(compute_word_problem(test))
>>>>>>> 8c2213d3c6ba44f6012f3df33408abef63d08016
