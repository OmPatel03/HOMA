
def MaximizeRevenue_function(listOfVariables):
    '''
        Returns the price of some item which maximizes the revenue based off the demand.
    '''

    #Unpack
    base_itemprice      = listOfVariables[0];
    delta_itemprice     = listOfVariables[1];
    base_personcount    = listOfVariables[2];
    delta_personcount   = listOfVariables[3];

    #From Calculations
    #X denotes the amount of dollar increases
    x = (base_itemprice*delta_personcount - delta_itemprice*base_personcount) / (2*delta_itemprice*delta_personcount)

    #Calculate max Item price
    max_rev_item_price = base_itemprice + x*delta_itemprice;

    #Return Value
    return max_rev_item_price;
