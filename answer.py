from problem_functions import MaximizeRevenue_function
from problem_functions import Interest_function

def answer (var_list):

    if len(var_list) == 3:
        ans = Interest_function(var_list)
        
    elif len(var_list) == 4:
        ans = MaximizeRevenue_function(var_list)
        
    else:
        pass
    
    return ans
