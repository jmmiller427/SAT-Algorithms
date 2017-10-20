"""
Name: John Miller
Date: 17 October 2017
Class: CS 463 - 001
Project: SAT Algorithms
"""

import Cost
from random import randint
from timeit import default_timer as timer

"""
Function: gsat()
Purpose: Finds a satisfiable (or best) formula to the cnf clauses
Input: The clauses array consisting of n cnf clauses 
Output: If there is a satisfiable or best formula it will output it

Note:

Structure: - Start by generating a random formula
           - Get the cost of that array and check if it is satisfiable
           - *** If not, find the value that if changed will have the biggest impact on satisfying 
             clauses. Ex: If 3 clauses are not satisfied and two of them have a same number
             make those same numbers satisfy in the formula by flipping its bit. Now hopefully only one clause will 
             not be satisfied. ***
           - If this new formula is better than the original, make it the original and run again
"""
def gsat(clauses):

    numOfVars = clauses[0]
    numOfClauses = clauses[1]
    best = []
    answer = []
    start = timer()

    # Loop through the number of variables (In this case 100)
    for i in range(0, numOfVars):

        # Get a random formula
        randFormula = []
        for j in range(0, numOfVars):
            randFormula.append(randint(0, 1))

        # Find the cost array of that formula (Including each unsatisfied clause)
        costArray = Cost.get_cost(clauses, randFormula)

        # Loop through the number of variables again (100)
        for j in range(0, numOfVars):

            # Get the cost of the random formula
            randArrayCost = costArray[-1]

            # Check if that cost satisfies the clauses, If it does append the clauses and cpu time
            # to the answer array and return it
            if randArrayCost == numOfClauses:
                end = timer()
                answer.append(numOfClauses)
                answer.append(end - start)
                return answer

            """***FIND MAX NUM UNSATISFIED***"""
            # Create a dictionary to count number of variables
            varCount = {}

            # Find out which variable occurs most often from non satisfying clauses
            # add the variable to a dictionary with the number of times it occurs
            for var in range(0, len(costArray) - 1):
                variables = costArray[var].split(" ")
                for m in range(0, len(variables)):
                    xVar = int(variables[m])
                    if xVar in varCount:
                        varCount[xVar] += 1
                    else:
                        varCount[xVar] = 1

            # Loop through the dictionary
            while varCount:

                # Get the max value from the dictionary
                maximum = max(varCount, key=varCount.get)
                temp = list(randFormula)
                flag = False

                # If the max value is a negative flip it
                if maximum < 0:
                    maximum = -maximum
                    flag = True

                # Switch the max values index in the array to satisfy it
                if randFormula[maximum - 1] == 1:
                    temp[maximum - 1] = 0
                else:
                    temp[maximum - 1] = 1

                # If it was previously a negative, make it negative again
                if flag:
                    maximum = -maximum

                # Find the cost of the new array
                tempCost = Cost.get_cost(clauses, temp)[-1]

                # If the new array cost is better than the random array cost
                # Set random array cost as the new array and exit the while loop
                if tempCost > randArrayCost:
                    randFormula = list(temp)
                    best = list(temp)
                    break

                # If the new array cost is not better, then pop that variable value off the dictionary and
                # Loop again
                else:
                    varCount.pop(maximum)

    # If no solution is found add the best cost and cpu time to the answer array and return it
    end = timer()
    answer.append(Cost.get_cost(clauses, best)[-1])
    answer.append(end - start)
    return answer
