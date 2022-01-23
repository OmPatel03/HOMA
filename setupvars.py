from loadjson import getProblemDictionary;
import string

#Custom Error
class DimentionError(Exception):
    pass

def create_list(typeKey, problem_string, problem_dict = getProblemDictionary()):

    #Grab Sub Dictionary From Dict
    typeDict = problem_dict.get(typeKey, "")
    if (type(typeDict) != dict):
        raise TypeError
    variableDict = typeDict["variable_keywords"]
    variableIdentifierWords = list(variableDict.values());

    #
    #Split String by numbers
    variablesAsAssignment = split_by_numbers(problem_string)
    print("\tFound {} variables in string".format(len(variablesAsAssignment)))

    #Count
    variableAmount = len(variableIdentifierWords);
    variableAmountRange = range(variableAmount);
    #if (len(variablesAsAssignment) != variableAmount):
        #raise DimentionError
    
    #
    #
    #Check + Assign Variables

    #Create Empty Lists
    isVariableSet = [False for i in variableAmountRange] 
    variableList = [1 for i in variableAmountRange] 
    print(variableList);

    #Loop Through
    for variableInformation in variablesAsAssignment:

        #Unpack Data From String
        variableWordsFromString = variableInformation[0];
        variableValue = variableInformation[1];

        #Save Which This String Portion Matches Best To the variable
        varInfoMatchInfo = [0 for i in variableAmountRange]

        #
        #Loop Through Variables From Index; Find Best Match
        for i in variableAmountRange:
            
            #Ignore If Set; No overriding
            if not isVariableSet[i]:
            
                #Get Key Word List
                identifiers = variableIdentifierWords[i];

                #Check Matches
                for variableWord in variableWordsFromString:
                    if (variableWord in identifiers):

                        #Save Any Matches
                        #print("match for value {} found in the {}th variable using word '{}'".format(variableValue, (i+1), variableWord))
                        varInfoMatchInfo[i] = varInfoMatchInfo[i]+1;

        #End

        #Check for which the variable matched most with
        print("Variable Value {} matches x words with {}".format(variableValue, varInfoMatchInfo))

        bestMatch = -1;
        biggestMatchAmount = 0;
        for j in variableAmountRange:
            if varInfoMatchInfo[j] > biggestMatchAmount:
                biggestMatchAmount = varInfoMatchInfo[j];
                bestMatch = j;
        
        #Variable Did not match with anything; Variable Error
        if bestMatch == -1:
            raise IndexError

        #Save as Best Match
        variableList[bestMatch] = variableValue
        isVariableSet[bestMatch] = True

    #Get
    print(variableList)
    return variableList;


def split_by_numbers(problem_string):
    '''
        Loops through a string and seperates it into streaks of words, followed by numbers.
        These numbers are used as the variables.

        Eg. "apple bottom jeans 100$. please buy for 130.fair deal yes?'
            >> [("apple bottom jeans", 100), ("please buy for", 130) ]

    '''

    #Remove Punctuation
    for punct in string.punctuation:
        problem_string = problem_string.replace(punct, " ")

    #Get Words
    words = problem_string.lower().split(" ");

    #Streak To Save
    returnList = []
    currentStringStreak = [];

    #Figure out where values lie
    valuesAtIndex = []
    wordNum = 0
    for word in words:
        if (word.isnumeric()):
            valuesAtIndex.append(wordNum)
        wordNum += 1

    #Get words surrounding each value
    valueCount = len(valuesAtIndex)
    for i in range(valueCount):

        wordAtPos = valuesAtIndex[i];

        wordRange = 4;

        startRange = max(0, wordAtPos-wordRange)
        endRange = min(len(words)-1, wordAtPos+wordRange)

        #Add to the streak
        wordListStreak = words[startRange:endRange]
        valuePos = valuesAtIndex[i]

        appendTuple = (wordListStreak, float(words[valuePos]))
        returnList.append(appendTuple)

    #Return List
    print(returnList)
    return returnList