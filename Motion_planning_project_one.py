import numpy as np
import sys

" Defining the Node class"
class Node():
    
    " Initialize method for the Node class"
    def __init__(self, nodeState, parentNode, actions):
        
        self.nodeState = nodeState # State of our current node
        self.parentNode = parentNode # State of the previous node(parent node)
        self.actions = actions # Move Up, Down, Left or right
        
        "Defining the children node objects, left, right, up or down "
        self.up = None
        self.down = None
        self.left = None
        self.right = None
    
    def ActionMoveLeft(self):
        
        empty_tile = [node[0] for node in np.where(self.nodeState == 0)]
        if empty_tile[1] == 0: # This condition signifies that if my empty_tile is in column 0 it cannot move left
            return np.array([])
        else:
            "Finding the position of the left tile relative to the current tile"
            left_tile = self.nodeState[empty_tile[0],empty_tile[1]-1]
            
            "Create a copy of the parent node so as to generate the new child nodes"
            new_node_state = self.nodeState.copy() 
            
            "Swap the left value with the empty tile"
            new_node_state[empty_tile[0],empty_tile[1]] = left_tile
            new_node_state[empty_tile[0],empty_tile[1]-1] = 0
            return new_node_state
        
    def ActionMoveRight(self):
        
        empty_tile = [node[0] for node in np.where(self.nodeState == 0)]
        if empty_tile[1] == 2: # This condition signifies that if my empty tile is in the second column it cannot move right 
            return np.array([])
        else:
            "Finding the position of the right tile relative to the current tile"
            right_tile = self.nodeState[empty_tile[0],empty_tile[1]+1]
            
            "Creating a copy of the parent Node so as to generate the new child nodes"
            new_node_state = self.nodeState.copy()
            
            "Swap the right tile with the empty tile"
            new_node_state[empty_tile[0],empty_tile[1]] = right_tile
            new_node_state[empty_tile[0],empty_tile[1]+1] = 0
            return new_node_state
        
    def ActionMoveUp(self):
        
        empty_tile = [node[0] for node in np.where(self.nodeState == 0)]
        if empty_tile[0] == 0: # This condition signifies that if my empty tile is in the 0th row it cannot move up
            return np.array([])
        else:
            "Finding the position of the Upper tile relative to the current tile"
            up_tile = self.nodeState[empty_tile[0]-1,empty_tile[1]]
            
            "Creating a copy of the parent Node so as to generate the new child nodes"
            new_node_state = self.nodeState.copy()
            
            "Swap the up tile with the empty tile"
            new_node_state[empty_tile[0],empty_tile[1]] = up_tile
            new_node_state[empty_tile[0]-1,empty_tile[1]] = 0
            return new_node_state
        
    def ActionMoveDown(self):
        
        empty_tile = [node[0] for node in np.where(self.nodeState == 0)]
        if empty_tile[0] == 2: # This condition signifies that if my empty tile is in the 2nd row it cannot move down
            return np.array([])
        else:
            "Finding the position of the Down tile relative to the current tile"
            down_tile = self.nodeState[empty_tile[0]+1,empty_tile[1]]
            
            "Creating a copy of the parent Node"
            new_node_state = self.nodeState.copy()
            
            "Swap the down tile with the empty tile"
            new_node_state[empty_tile[0],empty_tile[1]] = down_tile
            new_node_state[empty_tile[0]+1,empty_tile[1]] = 0
            return new_node_state
                
    def Backtrack(self):
        
        counter = 0
        
        nodeState_Backtrack = [] # List to store the nodestates for backtracking
        action_Backtrack = [] # List ot store the actions performed to achieve a goal state
        
        Nodes = open('nodePath.txt',"w")
        # Backtrack to gain node information 
        while self.parentNode:
            
            " Initialize self with the parent nofr"
            self = self.parentNode 
            
            "Determine the parent node state and append it our list"
            nodeState_Backtrack.append(self.nodeState)
            
            "Append the actions into our list"
            action_Backtrack.append(self.actions)
        
        # PRINTING THE PATH TO ACHIEVE THE GOAL 
        while nodeState_Backtrack:
            writetxt = " "
            #print(f'step: {counter} \nNodeState: {nodeState_Backtrack.pop()} \nactions:{action_Backtrack.pop()}')
            currentNode =  nodeState_Backtrack.pop()
            for column in range(currentNode.shape[1]):
                for row in range(currentNode.shape[0]):
                    writetxt = writetxt + str(currentNode[row][column])       
            writetxt = writetxt + "\n"
            Nodes.write(writetxt)
            print(currentNode)
            counter+=1
        
    def Breadth_First_Search(self,goal_State):
        
        frontier = [self] # Frontier is basically the nodes that have to be explored
        explored =set() # Explored is a set that stores all the visited nodes
        
        while(len(frontier) > 0):
            
            #print ("process started")
            
            current_node_state = frontier.pop(0) # Remove the first node in the queue
            # Reshaping the node to store as a string. Avoids the error of unhashable type (np.ndarray)
            explored.add(str(current_node_state.nodeState)) 
             
            if np.array_equal(current_node_state.nodeState,goal_State):
                
                print("Printing Backtracking")
                current_node_state.Backtrack() # Print out the the path that was employed to achieve the goal state
                
                return True
            
            else:
                
                if len(current_node_state.ActionMoveRight()) > 0:
                   
                    new_node_state = current_node_state.ActionMoveRight()
                    
                    if str(new_node_state) not in explored:
                        # Create a new child node that was created due to the right action
                        
                        right = Node(nodeState=new_node_state,parentNode=current_node_state,actions="right")
                        
                        frontier.append(right)
                    
                if len(current_node_state.ActionMoveLeft()) > 0:
                    
                    new_node_state = current_node_state.ActionMoveLeft()
                           
                    if str(new_node_state) not in explored:
                        # Create a child node that was created due to the left action 
                            
                        left = Node(nodeState=new_node_state,parentNode=current_node_state,actions='left')
                            
                        frontier.append(left)
                            
                if len(current_node_state.ActionMoveUp()) > 0:
                    new_node_state = current_node_state.ActionMoveUp()
                        
                    if str(new_node_state) not in explored:
                        # Create a child node that was created due to the left action 
                            
                        up = Node(nodeState=new_node_state,parentNode=current_node_state,actions='up')
                            
                        frontier.append(up)
                    
                if len(current_node_state.ActionMoveDown()) > 0:
                    
                    new_node_state = current_node_state.ActionMoveDown()
                        
                    if str(new_node_state) not in explored:
                        # Create a child node that was created due to the left action 
                            
                        down = Node(nodeState=new_node_state,parentNode=current_node_state,actions='down')
                            
                        frontier.append(down)  
                        
        print("process ended")

def main():

	# Hardcore the Initial State for prototyping purpose
	# Defining the goal state that the solver wants to achieve

	inputMatrix = sys.argv[1]
	goal_state = np.array([1,2,3,4,5,6,7,8,0]).reshape(3,3)
	initial_state = np.array([[0,0,0],[0,0,0],[0,0,0]])
	initial_state[0][0] = int(inputMatrix[0])
	initial_state[0][1] = int(inputMatrix[1])
	initial_state[0][2] = int(inputMatrix[2])
	initial_state[1][0] = int(inputMatrix[3])
	initial_state[1][1] = int(inputMatrix[4])
	initial_state[1][2] = int(inputMatrix[5])
	initial_state[2][0] = int(inputMatrix[6])
	initial_state[2][1] = int(inputMatrix[7])
	initial_state[2][2] = int(inputMatrix[8])
	print(initial_state)
	root_node = Node(nodeState=initial_state,actions=None,parentNode=None)
	root_node.Breadth_First_Search(goal_state)


if __name__ == "__main__":

	main()

