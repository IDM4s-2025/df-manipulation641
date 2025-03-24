#------------------------------------------------------------------------------------------------------------------
#   Region coloring problem
#
#   This code is an adaptation of the region coloring problem solver described in:
#   Artificial intelligence with Python. Alberto Artasanchez and Prateek Joshi. 2nd edition, 2020, 
#   editorial Pack. Chapter 10.
#
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------
from simpleai.search import CspProblem, backtrack

#------------------------------------------------------------------------------------------------------------------
#   Constraint functions
#------------------------------------------------------------------------------------------------------------------
def constraint_func(names, values):
    """ This constraint indicates that two colors must not be the same. """
    return values[0] != values[1]  

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------
# Define problem variables
names = ['Mark', 'Julia', 'Steve', 'Amanda', 'Brian', 
        'Joanne', 'Derek', 'Allan', 'Michelle', 'Kelly']

# Define variable domains
colors = dict((name, ['red', 'green', 'blue', 'gray']) for name in names)

# Define problem constraints 
constraints = [
    (('Mark', 'Julia'), constraint_func),
    (('Mark', 'Steve'), constraint_func),
    (('Julia', 'Steve'), constraint_func),
    (('Julia', 'Amanda'), constraint_func),
    (('Julia', 'Derek'), constraint_func),
    (('Julia', 'Brian'), constraint_func),
    (('Steve', 'Amanda'), constraint_func),
    (('Steve', 'Allan'), constraint_func),
    (('Steve', 'Michelle'), constraint_func),
    (('Amanda', 'Michelle'), constraint_func),
    (('Amanda', 'Joanne'), constraint_func),
    (('Amanda', 'Derek'), constraint_func),
    (('Brian', 'Derek'), constraint_func),
    (('Brian', 'Kelly'), constraint_func),
    (('Joanne', 'Michelle'), constraint_func),
    (('Joanne', 'Amanda'), constraint_func),
    (('Joanne', 'Derek'), constraint_func),
    (('Joanne', 'Kelly'), constraint_func),
    (('Derek', 'Kelly'), constraint_func),
]

# Solve the problem
problem = CspProblem(names, colors, constraints)
solution = backtrack(problem)

# Print the solution
print('\nColor mapping:\n')
for k, v in solution.items():
    print(k, '==>', v)

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------
