from problem_functions import *

def runScript (scriptname, params):
    return eval(scriptname)(params);


def formatStringFromVars(problemFormatString, problemVariablesToFill, problemVariableFormats, answer):
    '''
    Recurrsivly Formats the string based on the string + variables from the problem json
    '''

    #Get Length
    length = len(problemVariablesToFill);
    print(problemVariablesToFill)

    #Need to update
    if (length > 0):
        head = problemVariablesToFill[0]
        tail = problemVariablesToFill[1:length]

        #Update to be answer
        if (head < 0):
            head = answer[-head-1]

        #Format from the string
        headStr = problemVariableFormats[0].format(head)

        formatString = problemFormatString.replace("{}", headStr, 1)
        return formatStringFromVars(formatString, tail, problemVariableFormats[1:length], answer)

    #Done; Base Case
    else:
        return problemFormatString


def answer_create_variable_name_dict(variableNames, variableList):
    '''
    Create a dictionary containing the variable's name and the value used in the calculation
    '''
    answerVarDict = {}
    for i in range(len(variableList)):
        answerVarDict[variableNames[i]] = variableList[i];
    return answerVarDict