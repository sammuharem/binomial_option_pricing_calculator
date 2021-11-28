def listPrint(lst):
    for row in lst:
        rowList = []
        for item in row:
            rowList.append(round(item, 4))
        print(rowList)
    print('\n')
    
def checkInputs(s, x, t, r, b, v, nat, typ, prnt, exercisePeriods):
    if min(s,x,t,b,v) <= 0:
        raise Exception('Inputs are Invalid: Use a positive value for s, x, t, b and v')
    
    if nat not in ['A', 'B', 'E']:
        raise Exception("Inputs are Invalid: Use 'A' for American Options, 'B' for Bermudan or 'E' for European")
    
    if typ not in ['C', 'P']:
        raise Exception("Inputs are Invalid: Use 'C' for Call Options or 'P' for Put Options")
        
    if type(prnt) != bool:
        raise Exception('Inputs are Invalid: Use True to print steps to console, False to Disable')

def valueOption(s, x, t, r, b, v, nat = 'A', typ = 'C', prnt = True, exercisePeriods = []):
    """
    Calculates the fair option price of a simple Option inputs are as follows:
    s: The current stock price
    x: The strike price of the option
    t: The time in years until maturity of the option
    r: The current risk-free rate
    b: The number of branches to use in the option pricing
    v: The volatility of the underlying asset's price
    nat: 'A' for American (default), 'B' for Bermudan, 'E' for European 
    typ: 'C' for Call (default) or 'P' for Put
    prnt: True (default) to print variables to console, False to disable
    exercisePeriods: If option is Bermudan enter branches it is exercisable as a list.
    """
    
    checkInputs(s, x, t, r, b, v, nat, typ, prnt, exercisePeriods)
    
    exp = 2.718281828459045
    dt = t / b
    u = exp ** (v * (dt ** 0.5))
    d = 1/u
    p = (exp ** (r * (dt)) - d) / (u - d)
    q = (1-p)
        
    priceTree = [[s], [s * d, s * u]]
    for row in range(1, b):
        newRow = []
        newRow = [priceTree[row][0] * d]
        for item in priceTree[row]:
            newRow.append(item * u) 
        priceTree.append(newRow)  
        
    IVTree =[]
    for row in priceTree:
        newRow = []
        for item in row:
            if typ == 'C':
                newRow.append(max(item-x,0))
            elif typ == 'P':
                newRow.append(max(x-item,0))         
        IVTree.append(newRow)
    
    answerTree = []
    for rowIndex in range(b):
        newRow = []
        for item in priceTree[rowIndex]:
            newRow.append(0)
        answerTree.append(newRow)
    
    tempList = []
    for item in IVTree[b]:
        tempList.append(item)
    answerTree.append(tempList)

    if nat == 'A':
        exercisePeriods = list(range(b+1))
    elif nat == 'E':
        exercisePeriods = []

    for rowIndex in range(b - 1, -1, -1):    
        if rowIndex in exercisePeriods:
            exercisible = True
        else:
            exercisible = False
        for item in range(len(answerTree[rowIndex])):
            intrinsicValue = IVTree[rowIndex][item]
            discountedValue = exp ** (-r * dt) * (p * answerTree[rowIndex + 1][item + 1] + q * answerTree[rowIndex + 1][item])

            if exercisible == False:
                answerTree[rowIndex][item] = discountedValue
            
            else: 
                if intrinsicValue > discountedValue:
                    answerTree[rowIndex][item] = intrinsicValue
                else:
                    answerTree[rowIndex][item] = discountedValue
    
    if prnt == True:
        print(f'The up-factor is {round(u, 4)} and the down-factor is {round(d, 4)}\n')
        print(f'The probability of an upward price movement is {round(p, 4)}\n')
        print('The stock price at each node is:')
        listPrint(priceTree)
        print('The option value at each node are:')
        listPrint(answerTree)
        print(f'The fair value of the {nat} {typ} Option is ${round(answerTree[0][0], 4)}')
    
    return answerTree[0][0], priceTree, answerTree
