#------------------------------------------------------------------------------------------------------------------
#   n-queen problem solver using the backtracking algorithm
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------
from simpleai.search import CspProblem, backtrack

#------------------------------------------------------------------------------------------------------------------
#   Constraint functions
#-----------------------------------------------------------------------------------------------------------------
def safe(names, values):
    """ This constraint indicates whether the queens are safe. """
    n = len(names)
    
    for i in range(n):
        queen = values[i]
        safe = True
        for j in range(n):
            if i == j:
                continue
            other_queen = values[j]
            if (queen[0] == other_queen[0]):
                # The queens are on the same row
                safe = False
            elif (queen[1] == other_queen[1]):
                # The queens are on the same column
                safe = False
            elif abs(queen[0]-other_queen[0]) == abs(queen[1]-other_queen[1]):
                # The queens are on the same diagonal
                safe = False
        if not safe:
            return False
    return True

def different(names, values):
    """ This constraint indicates whether the queens are placed in different places. """
    return len(values) == len(set(values))

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------
# Define problem variables
n = 5
variables = ['Q' + str(i+1) for i in range(n)]

# Define variable domains
var_domain = []
for i in range(n):
    for j in range(n):
        var_domain.append((i, j))

domains = dict((var, var_domain) for var in variables)

# Define problem constraints 
constraints = [
    (variables, different),
    (variables, safe),
]

# Solve the problem
problem = CspProblem(variables, domains, constraints)
solution = backtrack(problem)

# Print the solution
print('-----Solution-----')
for row in range(n):
    for col in range(n):
        if (row, col) in list(solution.values()):
            print (' Q ', end = '')
        else:
            print (' - ', end = '')
    print('')
print('')
#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------
