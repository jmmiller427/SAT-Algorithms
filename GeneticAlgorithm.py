"""
Name: John Miller
Date: 18 October 2017
Class: CS 463 - 001
Project: SAT Algorithms
"""

import Cost
from random import randint
from timeit import default_timer as timer

"""
Function: genetic_alg()
Purpose: Finds a satisfiable formula to a cnf equation if it exists
Input: The clauses array with the cnf formula
Output: If the algorithm found a satisfiable formula 

Note: 

Structure: - Generate random formulas (may or may not satisfy)
           - Selection comes next. Randomly choose a certain amount of the population
             to survive or die. In this case the fittest may not survive. 
           - Crossover is mating. Randomly choose two chromosomes. Break them at a random point and combine
             the front of one with the back of the other and vice versa. Each two parents should create 
             two children. (Do it a few times)
           - Mutation. Choose a random chromosome, then a random bit and flip it
             to know how many chromosomes to mutate use formula:
             No. of mutation = (No. of cells in a chromosome * No. of chromosomes * mutation rate) / 100
"""
def genetic_alg(clauses):

    parents = []
    answer = []
    best = []
    numOfVars = clauses[0]
    numOfClauses = clauses[1]
    BLACK_PLAGUE = numOfVars * 50
    population = 10 * numOfVars

    start = timer()

    # Create a population of random arrays. These are called "parents"
    # For 100 variable cnf create 1000 parents initially
    for i in range(0, population):
        temp = []
        for j in range(0, numOfVars):
            temp.append(randint(0, 1))
        parents.append(temp)

    # Run a loop through 100 Generations
    for generations in range(0, 100):

        '''MATING 20%'''
        matingPop = int(len(parents) * .2)

        # Loop through the parents and mate a random 20% of them
        for j in range(0, matingPop):

            # Get parent 1 and 2 as random parents from the parents array
            parent1 = parents[randint(0, len(parents) - 1)]
            parent2 = parents[randint(0, len(parents) - 1)]

            # Get a random position that they will reproduce at
            placeToSwap = randint(0, numOfVars)

            # Create two children. The son has the first half of parent one and the second half of parent 2
            # The daughter has the opposite
            son = parent1[:placeToSwap] + parent2[placeToSwap:]
            daughter = parent2[:placeToSwap] + parent1[placeToSwap:]

            # Now add the son and daughter to the parents array
            parents.append(son)
            parents.append(daughter)

        '''MUTATING 2-3%'''
        mutatePop = int(len(parents) * .03)

        # Loop through the parents and mutate 3% of them
        for k in range(0, mutatePop):

            # Pick a random parent to mutate at a random position
            monster = parents[randint(0, len(parents) - 1)]
            placeToMutate = randint(0, numOfVars)

            # Swap the parents values at the position
            if monster[placeToMutate - 1] == 0:
                monster[placeToMutate - 1] = 1
            else:
                monster[placeToMutate - 1] = 0

        '''CHECK'''
        costOfParents = []

        # Loop through all the parents to find the costs of each one
        for l in range(0, len(parents)):

            # Get the cost
            singleCost = Cost.get_cost(clauses, parents[l])[-1]

            # If the cost of one of the parents satisfies all clauses, append the clauses satisfied
            # and the CPU time and return the answer
            if singleCost == numOfClauses:
                end = timer()
                answer.append(numOfClauses)
                answer.append(end - start)
                return answer

            # Else append the cost of that parent to the cost array
            else:
                costOfParents.append(singleCost)

        '''SURVIVAL OF THE FITTEST'''
        if BLACK_PLAGUE < len(parents):
            killNum = int(len(parents) * .75)
        else:
            killNum = int(len(parents) * .2)

        # Get the best cost and save it as best
        best = max(costOfParents)

        # Loop through the certain number to kill
        for m in range(0, killNum):

            # Get the index of the lowest cost, Then pop off that cost and its respective
            # parent
            minCostIndex = costOfParents.index(min(costOfParents))
            costOfParents.pop(minCostIndex)
            parents.pop(minCostIndex)

    # If no solution was found, Save the best and CPU time and return answer
    end = timer()
    answer.append(best)
    answer.append(end - start)
    return answer
