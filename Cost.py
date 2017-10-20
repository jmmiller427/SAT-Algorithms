"""
Name: John Miller
Date: 17 October 2017
Class: CS 463 - 001
Project: SAT Algorithms
"""

"""
Function: get_cost()
Purpose: The get cost function will find the number of clauses that are satisfied
         based on the formula and clauses given
Input: Clauses array, formula of 1's and 0's representing true and false for the clauses
Output: The get cost function returns the total number of satisfied clauses

Note: - The clauses are positive and negative numbers. A positive value would indicate a 1 is true and
        a 0 is false. A negative number is a negation (not) so this would indicate that a 0 is true 
        and a 1 is false
      - Since the clauses are in cnf once a satisfying variable is found in one clause, the whole 
        clause is satisfied so you can move onto the next clause 
        
Structure: - Take in the clauses and formula to check the cost those clauses
           - Loop through the clauses, split the clause into the three variables
           - Loop through the variables, If it is a negative, then flip the value
           - Follow the notes above for what to do with a positive or negative when it is found
           - Once a clause is satisfied, move onto the next. If it isn't then add it to the array to return 
             unsatisfied clauses and the total cost
           - Cost is calculated as the number of satisfied clauses
"""
def get_cost(clauses, formula):

    # Set clauses satisfied to 0
    clauseSatisfied = 0
    satArray = []

    # Loop through the clauses array, skip the first two values
    # as those are the number of variables and clauses
    for i in range(2, len(clauses)):

        satisfied = False

        # Split each clause at a space to get three numbers
        variables = clauses[i].split(" ")

        # Loop through each individual clause
        for j in range(0, len(variables)):

            # Set the variable to an int
            xVar = int(variables[j])

            # If the variable is less than zero it is negative
            # so make it positive to find it through the formula
            if xVar < 0:
                xVar = -xVar

                # If the formula at the position of the variable is a zero
                # then it should be inverted, so a 0 will actually be true so add to clause satisfied
                # and exit out of the loop so you don't check any more variables in this clause
                if formula[xVar - 1] == 0:
                    clauseSatisfied += 1
                    satisfied = True
                    break

            # If the variable is positive then a 1 satisfies the whole clause
            # so add to clauses satisfied and go to the next clause
            elif xVar > 0:
                if formula[xVar - 1] == 1:
                    clauseSatisfied += 1
                    satisfied = True
                    break

        if not satisfied:
            satArray.append(clauses[i])

    satArray.append(clauseSatisfied)

    return satArray
