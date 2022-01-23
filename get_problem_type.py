from loadjson import getProblemDictionary
import pprint


def get_problem(text):
    problemDict = getProblemDictionary()
    problems = {}
    for problem in problemDict:
        problems[problem] = []
        for keyword in problemDict[problem]:
            problems[problem].append(problemDict[problem].values())
    return problems


pprint.pprint(get_problem("ds"))
