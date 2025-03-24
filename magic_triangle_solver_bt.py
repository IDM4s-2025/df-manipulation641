#------------------------------------------------------------------------------------------------------------------
#   Magic triangle puzzle solver using the backtracking algorithm
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------
from simpleai.search import CspProblem, backtrack

#------------------------------------------------------------------------------------------------------------------
#   Constraint functions
#-----------------------------------------------------------------------------------------------------------------
def sum_10(names, values):
    """ This constraint indicates that the sum of 3 elements of one edge must be 10. """
    return sum(values) == 10

def different(names, values):
    """ This constraint indicates that all variables must be different. """
    return len(values) == len(set(values))

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------
# Define problem variables
variables = ['a', 'b', 'c', 'd', 'e', 'f']

# Define variable domains
domains = dict((var, [1, 2, 3, 4, 5, 6]) for var in variables)

# Define problem constraints 
constraints = [
    (('a', 'c', 'f'), sum_10),
    (('a', 'b', 'd'), sum_10),
    (('d', 'e', 'f'), sum_10),
    (('a', 'b', 'c', 'd', 'e', 'f'), different),
]

# Solve the problem
problem = CspProblem(variables, domains, constraints)
solution = backtrack(problem)

# Print the solution
print('-----Solution-----')
print("  {}".format(solution['a']))
print(" {} {}".format(solution['b'], solution['c']))
print("{} {} {}".format(solution['d'], solution['e'], solution['f']))

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------
