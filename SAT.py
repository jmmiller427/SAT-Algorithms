"""
Name: John Miller
Date: 14 October 2017
Class: CS 463 - 001
Project: SAT Algorithms
"""

import SimulatedAnnealing
import GSAT
import GeneticAlgorithm
import matplotlib.pyplot as plt
import numpy as np
import os
import glob


"""
Function: parsefile()
Purpose: Parse through a .cnf file to get the clauses 
Input: Lines - These lines are each line of clauses from the .cnf files
Output: Return the sanitized data

Note: Clauses is a list of variables. They are in conjunctive normal form (cnf)

Structure: - Loop through all the lines given from a file
           - If the line starts with a p save its variable and clauses values
           - If it starts with a blank, it is a clause. Sanatize the clause to be just the three numbers
           - Else it is a comment so skip it
"""
def parsefile(lines):
    # Create a empty clauses list, first element of file is number of variables
    clauses = []

    # Loop through all the lines in the file
    for i in range(0, len(lines)):

        # If the first element in the line is a p,
        # find the number of clauses and the number of variables
        if lines[i][0] == "p":

            # Split the line and save index 2 to number of variables
            # and index 3 to number of clauses
            pLine = lines[i].split(" ")
            numOfVars = int(pLine[2])
            numOfClauses = int(pLine[3])

            clauses.append(numOfVars)
            clauses.append(numOfClauses)

        # If the first element in the line is a blank,
        # then it is a clause
        elif lines[i][0] == " ":

            # Split the line and take just the number elements
            singleClause = lines[i].split("\n")
            singleClause = singleClause[0][1:-2]

            # append the single clause to clauses
            clauses.append(singleClause)

        # Else it is a comment so skip it
        else:
            pass

    return clauses


"""
Function: plot()
Purpose: This function plots the average clauses satisfied for each formula
Input: The average points for each formula and an array with each formula name
Output: A bar graph for each formula
"""
def plotclauses(plotPoints, algs):

    y_pos = np.arange(len(algs))
    performance = []

    # get each average point to plot
    for i in range(0, len(plotPoints)):
        performance.append(plotPoints[i])

    # Plot all points and set labels
    plt.bar(y_pos, performance, align='center')
    plt.xticks(y_pos, algs)
    plt.ylabel('Clauses Satisfied')
    plt.title('Genetic Algorithm')
    plt.show()


"""
Function: plotcpu()
Purpose: This function plots the average cpu time each algorithm takes
Input: The average cpu and each formula name
Output: A graph of the average CPU times
"""
def plotcpu(plotPoints, algs):

    y_pos = np.arange(len(algs))
    performance = []

    for i in range(0, len(plotPoints)):
        performance.append(plotPoints[i])

    plt.bar(y_pos, performance, align='center')
    plt.xticks(y_pos, algs)
    plt.ylabel('CPU Time')
    plt.title('Genetic Algorithm')
    plt.show()


"""
Function: main()
Purpose: Gets user input for a .cnf file or directory of .cnf files
         Parses the file to get number of variables and the clauses formula
         Calls three SAT algorithms to process each file
Input: N/A
Output: N/A

Structure: - Get a directory of all cnf files
           - Loop through each file, running each algorithm on each formula and saving the data
           - Plot the data
"""
def main():

    # Get the file or directory the user enters
    answer = input("Which file or directory would you like to use?\n"
                   "F/D: ")

    algs = []
    cla = []
    cpu = []

    # If the input is a directory
    if answer == "tests" or answer == "3cnf_100atoms":

        # Open the directory then run each file in the directory
        # in the file that ends in .cnf
        os.chdir(answer)
        for filename in glob.glob("*.cnf"):

            print(filename)

            # Open the file and call parse file to make a clauses array
            open_file = open(filename, "r")
            lines = open_file.readlines()
            open_file.close()
            clauses = parsefile(lines)

            # Append the current filename to list
            algs.append(filename)

            ClausesFound = 0
            CPUTime = 0

            # Run each algorithm 10 times on a single formula since they use randomness
            # Get the clauses and cpu each time
            for i in range(0, 10):
                Answer = GeneticAlgorithm.genetic_alg(clauses)
                # Answer = SimulatedAnnealing.simulated_annealing(clauses)
                # Answer = GSAT.gsat(clauses)

                ClausesFound += Answer[0]
                CPUTime += Answer[1]

            # Find the average clauses and cpu time and append those for each file
            avgClauses = ClausesFound / 10
            avgCPU = CPUTime / 10

            cla.append(avgClauses)
            cpu.append(avgCPU)

        # Once all files have been ran, plot the Clauses satisfied and the CPU time
        plotclauses(cla, algs)
        plotcpu(cpu, algs)


main()
