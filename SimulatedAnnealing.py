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
Function: simulated_annealing()
Purpose: This satisfiable algorithm will find an answer to the clauses
Input: This function takes in an array of clauses 
Output: It will output if the cnf formula is satisfiable

Note: - The program will run for 1000 seconds as that is the timeout. If it is not found in
        1000 seconds then the formula is unsatisfiable
      - There are 100 random restarts in the loop. Every 10 seconds if a answer has not been found
        it will create a new formula to test, as the previous one has most likely his a local maximum
        
Structure: - Find a random formula (may or may not satisfy)
           - Find a neighbor formula by changing one bit of the random one
           - Check which one is better. Make the one that is better the new formula
           - Loop until you find an answer. Set a restart after 100 loops because the formula might get stuck
             at a local maximum. 
           - If no answer found, create new random formula. Do this whole process 100 times
"""
def simulated_annealing(clauses):

    randFormula = []
    answer = []
    numOfVars = clauses[0]
    numOfClauses = clauses[1]

    start = timer()

    # Start a loop of the number of variables (100 for the 100 var clauses)
    for m in range(0, numOfVars):

        # Create a random possible answer
        for i in range(0, numOfVars):
            randFormula.append(randint(0, 1))

        # Run another for loop to test the random answer
        for j in range(0, numOfVars):

            # Get the cost of the original formula and create a "neighbor"
            originalCost = Cost.get_cost(clauses, randFormula)[-1]
            neighbor = list(randFormula)

            # Loop through the neighbor and change 10% of the values. This way
            # the neighbor is close to the original formula but not exactly
            for k in range(0, int(numOfVars / 10) - 1):
                random_position = randint(0, numOfVars - 1)

                if randFormula[random_position] == 1:
                    neighbor[random_position] = 0
                else:
                    neighbor[random_position] = 1

            # Get the cost of the neighbor
            neighborCost = Cost.get_cost(clauses, neighbor)[-1]

            # If the cost of the neighbor satisfies all clauses, create answer array
            # with clauses satisfied and the cpu time and return it
            if neighborCost == numOfClauses:
                end = timer()
                answer.append(numOfClauses)
                answer.append(end - start)
                return answer

            # If the neighbor is better than the original, Make the original what the neigbor was and
            # then loop through again
            if neighborCost > originalCost:
                randFormula = list(neighbor)

    # If all loops are performed without reaching a satisfiable solution,
    # get the highest number of satisfied clauses and append it and the CPU time to answers
    end = timer()
    answer.append(Cost.get_cost(clauses, randFormula)[-1])
    answer.append(end - start)
    return answer
