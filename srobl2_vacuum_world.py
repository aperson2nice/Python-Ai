# Sheila Robles
# June 27, 2017
# Python 2.7.1
# Vacuum world 2x2 implementation
from __future__ import print_function

# Initialize dirt and agent states and Description of actions
agent_position = [0,0] 
dirt = [1,1],[1,1]
initial_dirt = str(dirt)
possible_actions = ["Suck","Move North","Move East","Move South","Move West"]
cost, num_of_actions = [0,0]
status = ""

# Transition Model
def to_move(action):
    # checks whether or not to move based on information
    global num_of_actions
    num_of_actions += 1
    if dirt[agent_position[0]][agent_position[1]] == 0 and action == "Move West":
        print("No action taken, agent skipped " + action+"-- Dirt state: " + str(dirt))
        return 0
    else:
        return move_action(action)
def move_action(action_string):
    ''' move the vacuum agent based on the next action in the list
    '''
    global num_of_actions, cost
#    num_of_actions += 1
    if action_string == "Suck" and dirt[agent_position[0]][agent_position[1]] == 1:
        dirt[agent_position[0]][agent_position[1]] = 0
        agents_action = "Agent cleaned dirt"
        cost += 1
    elif action_string == "Move North" and agent_position[1] == 0:
        agent_position[1] = 1
        agents_action = "Action taken: Agent moved North"
    elif action_string == "Move East" and agent_position[0] == 0:
        agent_position[0] = 1
        agents_action = "Action taken: Agent moved East"
    elif action_string == "Move South" and agent_position[1] == 1:
        agent_position[1] = 0
        agents_action = "Action Taken: Agent moved South"
    elif action_string == "Move West" and agent_position[0] == 1:
        agent_position[0] = 0
        agents_action = "Action Taken: Agent moved West"
    else:
        agents_action = "No action taken, could not " + action_string
        print(agents_action+"-- Dirt state: " + str(dirt))
        return 0 # no action was taken
    print(agents_action+"-- Dirt state: " + str(dirt))
    return 1 # returning the cost to move

# test to see if dirt is at goal state    
def goal_test():
    for x_coordinate in range(len(dirt)):
        for y_coordinate in dirt[x_coordinate]: 
            if dirt[x_coordinate][y_coordinate] != 0:
                return False
    return True
    
def print_status():
    print('{:-<50}'.format(" "))
    print('{: <49}'.format("| Status: "+status),"|")    
    print('{: <49}'.format("| Number of Actions: "+str(num_of_actions)),"|")
    print('{: <49}'.format("| Total cost of solution: "+str(cost)),"|")    
    print('{: <49}'.format("| Initial Dirt Environment: "+initial_dirt),"|")
    print('{: <49}'.format("| Final Dirt Environment: "+str(dirt)),"|")
    print('{:-<50}'.format(" "),"\n")
    
def solution():
    return "Solution found"

def cutoff():
    return "Ran out of tries, limit reached"

def failure():
    return "Failed to find"
    
def recursive_search(agent_state, poss_actions, limit):
    global cost
    if goal_test():
        return solution()
    elif limit == 0:
        return cutoff()
    else:
        cutoff_occurred = False
        for action in poss_actions:
            child = poss_actions[poss_actions.index(action)]
            result = recursive_search(child, poss_actions, limit-1)
            cost += to_move(child)
            if result == cutoff():
                cutoff_occurred = True
            elif result != failure():
                return result
        if cutoff_occurred:
            return cutoff()
        else:
            return failure()

status = recursive_search(agent_position, possible_actions, 10)
print_status()