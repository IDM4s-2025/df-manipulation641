#------------------------------------------------------------------------------------------------------------------
#   Missionaries and cannibals problem
#------------------------------------------------------------------------------------------------------------------

from simpleai.search import SearchProblem, breadth_first

#------------------------------------------------------------------------------------------------------------------
#   Problem definition
#------------------------------------------------------------------------------------------------------------------

MAX_NUM: int = 3


class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm: int = missionaries # west bank missionaries
        self.wc: int = cannibals # west bank cannibals
        self.em: int = MAX_NUM - self.wm  # east bank missionaries
        self.ec: int = MAX_NUM - self.wc  # east bank cannibals
        self.boat: bool = boat
    
    def __eq__(self, value: 'MCState'):
        return self.wm == value.wm and self.wc == value.wc and self.boat == value.boat

    def __hash__(self):
        return hash((self.wm, self.wc, self.boat))
                    
    def __str__(self) -> str:
        return("On the west bank there are {} missionaries and {} cannibals.n" 
               "On the east bank there are {} missionaries and {} cannibals.n"
               "The boat is pn the {}bank")


    @property
    def   

class MissionariesAndCannibals(SearchProblem):
    """ Class that is used to define the missionaries and cannibals problem. 
        The states are represented by tuples (a, b, c, d, e), where a is the number of missionaries 
        on the left side, b is the number of cannibals on the left side, c is the number of 
        missionaries on the right side, d is the number of cannibals on the right side, 
        and e is the position of the raft (L or R).
    """

    def __init__(self):
        """ Class constructor. It initializes the problem with 3 missionaries and 3 cannibals
            at one side of the river. 
        """
        
        # Call base class constructor (the initial state is specified here).
        SearchProblem.__init__(self, MCState(3, 3, True))

    def actions(self, state: MCState):
        """ 
            This method returns a list with the possible actions that can be performed according to
            the specified state.

            state: The state to be evaluated.
        """
        act = []

        if state.boat:            
            # One missionary to the other side       
            if state.wm >= 1:
                if ((state.wm-1 >= state.wc) or state.wm-1 == 0) and (state.em+1 >= state.ec):
                    act.append('M1R')

            # Two missionaries to the other side       
            if state.wm >= 2:
                if ((state.wm-2 >= state.wc) or state.wm-2 == 0) and (state.em+2 >= state.ec):
                    act.append('M2R')

            # One cannibal to the other side       
            if state.wc >= 1:
                if (state.em >= state.ec+1) or (state.em == 0):
                    act.append('C1R')

            # Two cannibals to the other side       
            if state.wc >= 2:
                if (state.em >= state.ec+2) or (state.em == 0):
                    act.append('C2R')

            # One missionary and one cannibal to the other side       
            if state.wm >= 1 and state.wc >= 1:      
                if state.em+1 >= state.ec+1:
                    act.append('M1C1R')

        else:
            # One missionary to the other side       
            if state.em >= 1:
                if ((state.em-1 >= state.ec) or state.em-1 == 0) and (state.wm+1 >= state.wc):
                    act.append('M1L')

            # Two missionaries to the other side       
            if state.em >= 2:
                if ((state.em-2 >= state.ec) or state.em-2 == 0) and (state.wm+2 >= state.wc):
                    act.append('M2L')

            # One cannibal to the other side       
            if state.ec >= 1:
                if (state.wm >= state.wc+1) or (state.wm == 0):
                    act.append('C1L')

            # Two cannibals to the other side       
            if state.ec >= 2:
                if (state.wm >= state.wc+2) or (state.wm == 0):
                    act.append('C2L')

            # One missionary and one cannibal to the other side       
            if state.em >= 1 and state.ec >= 1:    
                if state.wm+1 >= state.wc+1:
                    act.append('M1C1L')

        return {a for a in act if self. result(state, a).is_legal

    def result(self, state: MCState, action):
        """ 
            This method returns the new state obtained after performing the specified action.

            state: The state to be modified.
            action: The action be perform on the specified state.
        """

        m1 = state.wm
        m2 = state.em    
        c1 = state.wc            
        c2 = state.ec
        r = state.boat

        if action == 'M1R':
            m1-=1;
            m2+=1;
            r='R';
        elif action == 'M2R':
            m1-=2;
            m2+=2;
            r='R';
        elif action == 'C1R':
            c1-=1;
            c2+=1;
            r='R';
        elif action == 'C2R':
            c1-=2;
            c2+=2;
            r='R';
        elif action == 'M1C1R':
            m1-=1;
            m2+=1;
            c1-=1;
            c2+=1;
            r='R';
        elif action == 'M1L':
            m1+=1;
            m2-=1;
            r='L';
        elif action == 'M2L':
            m1+=2;
            m2-=2;
            r='L';
        elif action == 'C1L':
            c1+=1;
            c2-=1;
            r='L';
        elif action == 'C2L':
            c1+=2;
            c2-=2;
            r='L';
        elif action == 'M1C1L':
            m1+=1;
            m2-=1;
            c1+=1;
            c2-=1;
            r='L';
        
        return MCState(m1, c1, r == 'L')

    def is_goal(self, state):
        """ 
            This method evaluates whether the specified state is the goal state.

            state: The state to be tested.
        """
        return state == MCState(0, 0, False)

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    # Solve problem
    result = breadth_first(MissionariesAndCannibals(), graph_search=False)

    # Print results
    for i, (action, state) in enumerate(result.path()):
        print()
        if action == None:
            print('Initial configuration')
        elif i == len(result.path()) - 1:
            print('After moving', action, 'Goal achieved!')
        else:
            print('After moving', action)

        print(state)

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------