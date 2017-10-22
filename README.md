# SAT-Algorithms
Three satisfying algorithm implementations. 

These algorithms take in conjunctive normal form equations and each try to find a satisfying solution for each one. There are two files of .cnf files. One has ten files with 40-48 clauses of ten variables. The other has three hundred files with 410-460 clauses of 100 variables. The clauses are 1-10 and its negatives. The negatives represent negations of the posititve numbers. 

A formula is generated to try and satisfy these the clauses. The formula is 1's and 0's representing true and false. If a variable in a clause is positive a 1 represents a truth statement. If it is negative a 0 would represent a truth statement. 

After each algorithm was ran, graphs were made using matplotlib to display the CPU time each algorithm took for each formula and a graph to show the total number of clauses satisfied. 

Simulated Annealing: The simulating annealing algorithm starts out by creating a random formula to try and satisfy
                     the clauses. Then a neighbor is created that is close to the original. The cost of each one
                     is found and then compared. If the neighbor satisfies more than the original then it is now
                     taken as the main formula. This is looped 100 times in order to try and find an answer. If
                     one is not found a "random restart" is performed and a new random array is generated. The best
                     cost of all of these is saved and returned. It will not always find a satisfying solution.

GSAT: The GSAT algorithm starts out by generating a random formula like simulated annealing. It then finds the
      cost of that formula and checks if it is a satisfying cost. If it isn't then the algorithm finds all the
      clauses that are not satisfied. Out of these clauses the variable that occurs the most is found and then
      changed. A new cost is calculated to see if the cost is better, if it isn't that specific variable is deleted
      and it is looped again. If it is a better cost it loops again to see if it satisfies or generates a new
      temp with unsatisfied clauses. It will not always find a satisfying solution.

Genetic Algorithm: The genetic algorithm starts by taking a population of random formulas that I called parents.
                   The parents are sent into a loop that makes new generations each time. A new generation
                   starts out by choosing a random 20% of the parents to mate. They mate by choosing a random
                   position to switch at and then combing the front of one parent with the back of the other and
                   vice versa. Then there is a mutation. 3% of the population is mutated by choosing a random bit
                   of a formula and swapping its value. Once the population is mutated, then perform natural
                   selection by killing 20% of the population. Kill the ones with the lowest costs as they are not
                   fit to survive. If the population reaches a tipping point, Kill off a huge portion (all of the
                   worst costs).

Cost Function: My cost function takes in a file of clauses and parses through each one. It finds out if a clause is
               satisfied by testing if a 1 or a 0 is in the clause. If there is one true statement in a clause, the
               whole clause is true. Run through and keep a count of all satisfied clauses and record which clauses
               are not satisfied so it can be used for GSAT.

SAT (main): The SAT file has a main function. The main function opens a file from a directory. The whole directory
            is ran through and then each function is ran with each file 10 times. It is ran 10 times and then the
            average CPU and clauses satisfied are calculated and then each of those is sent to a plot function. The
            plot function then plots each file with its average clauses satisfied and its average CPU.
            
