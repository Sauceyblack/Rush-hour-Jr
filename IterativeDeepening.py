#Thomas Braun
#I pledge my honor that I have abided by the Stevens honor system
import heapq
class node(object):
    """
    Each node is a board state, children of a node are each potential move
    """
    def __init__(self, gscore, boardstate):
        self.gscore = gscore
        self.boardstate = boardstate

    def __lt__(self, other):
        if self.gscore < other.gscore:
            return True
        elif self.gscore >= other.gscore:
            return False
      

#initialstate = list of n tuples
# easy1 =  [("I",  "H", "C", 3) , ( "C", "V", "A", 3), ("B", "H", "B", 4), ("C", "V", "C", 5), ("C", "V", "E", 5)];
# easy5 = [("I", "H", "C", 4) , ("C", "V", "A", 4), ("B", "V", "A", 6), ("C", "V", "D", 4), ("C", "H", "E", 5)];
# easy9 = [("I", "H", "C", 4), ("B", "H", "D", 1), ("C", "V", "E", 3), ("B", "H", "F", 4), ("C", "V", "D", 5), ("B", "V", "C", 6)];
def dls(initialboardstate, depth) :
    """
    Depth limited search implementation
    """
    visitednodes = None
    #Base case checks whether car is at exit
    if initialboardstate[0][3] == 5:
        return initialboardstate

    elif depth > 0:
        children = generatemoves(initialboardstate, initializeboard(initialboardstate))
        for child in children:
            visitednodes =  dls(child, depth - 1)
            if visitednodes != None:
                return visitednodes
    return None

def initializeboard(boardinput):
    """
    Takes in a list of string tuples and initializes the 6 by 6 array with the given vehicles
    """
    car_array = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        
    for car in list(range(len(boardinput))):
            if boardinput[car][0] == 'C' or 'I':
                if boardinput[car][1] == "H":
                    if boardinput[car][2] == "A":
                        car_array[0][(boardinput[car][3]) - 1] = 1
                        car_array[0][(boardinput[car][3])] = 1
                    if boardinput[car][2] == "B":
                        car_array[1][(boardinput[car][3]) - 1] = 1
                        car_array[1][(boardinput[car][3])] = 1
                    if boardinput[car][2] == "C":
                        car_array[2][(boardinput[car][3]) - 1] = 1
                        car_array[2][(boardinput[car][3])] = 1
                    if boardinput[car][2] == "D":
                        car_array[3][(boardinput[car][3]) - 1] = 1
                        car_array[3][(boardinput[car][3])] = 1
                    if boardinput[car][2] == "E":
                        car_array[4][(boardinput[car][3]) - 1] = 1
                        car_array[4][(boardinput[car][3])] = 1
                    if boardinput[car][2] == "F":
                        car_array[5][(boardinput[car][3]) - 1] = 1
                        car_array[5][(boardinput[car][3])] = 1
                if boardinput[car][1] == "V":
                    if boardinput[car][2] == "A":
                        car_array[0][(boardinput[car][3]) - 1] = 1
                        car_array[1][(boardinput[car][3]) - 1] = 1
                    if boardinput[car][2] == "B":
                        car_array[1][(boardinput[car][3]) - 1] = 1
                        car_array[2][(boardinput[car][3]) - 1] = 1
                    if boardinput[car][2] == "C":
                        car_array[2][(boardinput[car][3]) - 1] = 1
                        car_array[3][(boardinput[car][3]) - 1] = 1
                    if boardinput[car][2] == "D":
                        car_array[3][(boardinput[car][3]) - 1] = 1
                        car_array[4][(boardinput[car][3]) - 1] = 1
                    if boardinput[car][2] == "E":
                        car_array[4][(boardinput[car][3]) - 1] = 1
                        car_array[5][(boardinput[car][3]) - 1] = 1
 #                  if boardinput[car][2] == "F":
 #                      car_array[6][(boardinput[car][3]) - 1] = 1
            if boardinput[car][0] == "B":
                if boardinput[car][1] == "H":
                    if boardinput[car][2] == "A":
                        car_array[0][(boardinput[car][3]) - 1] = 1
                        car_array[0][(boardinput[car][3])] = 1
                        car_array[0][(boardinput[car][3]) + 1] = 1
                    if boardinput[car][2] == "B":
                        car_array[1][(boardinput[car][3]) - 1] = 1
                        car_array[1][(boardinput[car][3])] = 1
                        car_array[1][(boardinput[car][3]) + 1] = 1
                    if boardinput[car][2] == "C":
                        car_array[2][(boardinput[car][3]) - 1] = 1
                        car_array[2][(boardinput[car][3])] = 1
                        car_array[2][(boardinput[car][3]) + 1] = 1
                    if boardinput[car][2] == "D":
                        car_array[3][(boardinput[car][3]) - 1] = 1
                        car_array[3][(boardinput[car][3])] = 1
                        car_array[3][(boardinput[car][3]) + 1] = 1
                    if boardinput[car][2] == "E":
                        car_array[4][(boardinput[car][3]) - 1] = 1
                        car_array[4][(boardinput[car][3])] = 1
                        car_array[4][(boardinput[car][3]) + 1] = 1
                    if boardinput[car][2] == "F":
                        car_array[5][(boardinput[car][3]) - 1] = 1
                        car_array[5][(boardinput[car][3])] = 1
                        car_array[5][(boardinput[car][3]) + 1] = 1
                if boardinput[car][1] == "V":
                    if boardinput[car][2] == "A":
                        car_array[0][(boardinput[car][3]) - 1] = 1
                        car_array[1][(boardinput[car][3]) - 1] = 1
                        car_array[2][(boardinput[car][3]) - 1] = 1
                    if boardinput[car][2] == "B":
                        car_array[1][(boardinput[car][3]) - 1] = 1
                        car_array[2][(boardinput[car][3]) - 1] = 1
                        car_array[3][(boardinput[car][3]) - 1] = 1
                    if boardinput[car][2] == "C":
                        car_array[2][(boardinput[car][3]) - 1] = 1
                        car_array[3][(boardinput[car][3]) - 1] = 1
                        car_array[4][(boardinput[car][3]) - 1] = 1
                    if boardinput[car][2] == "D":
                        car_array[3][(boardinput[car][3]) - 1] = 1
                        car_array[4][(boardinput[car][3]) - 1] = 1
                        car_array[5][(boardinput[car][3]) - 1] = 1
   #                 if boardinput[car][2] == "E":
  #                      car_array[5][(boardinput[car][3])] = 1
    #                if boardinput[car][2] == "F":
     #                   car_array[6][(boardinput[car][3])] = 1

    return car_array

      
        
def generatemoves(boardstate, car_array):
    """
    Analyses a given board state represented with an array, and generates all potential children of that state
    """
    children = []
        
    newboardstate = []
    
    for car in boardstate:
        newboardstate.append(list(car))
    
    for i in range(len(boardstate)):
        
        carrow = ord(boardstate[i][2]) - 65
        carcol = boardstate[i][3] - 1
        
        if boardstate[i][0] == 'C' or 'I': 
            if boardstate[i][1] == 'V':  
                if (boardstate[i][2] != 'A'): 
                    if car_array[carrow - 1][carcol] == 0:
                            newboardstate[i][2] = chr(ord(newboardstate[i][2]) - 1)
                            children = children + [newboardstate]
                            newboardstate = []
                            for car in boardstate:
                                newboardstate.append(list(car))                                                             
                if (boardstate[i][2] != 'E'):
                    if car_array[carrow + 2][carcol] == 0:
                            newboardstate[i][2] = chr(ord(newboardstate[i][2]) + 1)
                            children = children + [newboardstate]
                            newboardstate = []
                            for car in boardstate:
                                    newboardstate.append(list(car))
            if boardstate[i][1] == 'H':
                if (boardstate[i][3] != 1):  
                    if car_array[carrow][carcol - 1] == 0:
                            newboardstate[i][3] = newboardstate[i][3] - 1
                            children = children + [newboardstate]
                            newboardstate = []
                            for car in boardstate:
                                newboardstate.append(list(car))
                if (boardstate[i][3] != 5):
                    if car_array[carrow][carcol + 2] == 0:
                            newboardstate[i][3] = newboardstate[i][3] + 1
                            children = children + [newboardstate]
                            newboardstate = []
                            for car in boardstate:
                                newboardstate.append(list(car))
        if boardstate[i][0] == 'B': 
            if boardstate[i][1] == 'V': 
                if (boardstate[i][2] != 'A'):
                    if car_array[carrow - 1][carcol] == 0:
                            newboardstate[i][2] = chr(ord(newboardstate[i][2]) - 1)
                            children = children + [newboardstate]
                            newboardstate = []
                            for car in boardstate:
                                newboardstate.append(list(car))                                                             
                if (boardstate[i][2] != 'D'):
                    if car_array[carrow + 3][carcol] == 0:
                            newboardstate[i][2] = chr(ord(newboardstate[i][2]) + 1)
                            children = children + [newboardstate]
                            newboardstate = []
                            for car in boardstate:
                                        newboardstate.append(list(car))                                       
            if boardstate[i][1] == 'H':
                if (boardstate[i][3] != 4):
                    if car_array[carrow][carcol + 3] == 0:
                            newboardstate[i][3] = newboardstate[i][3] + 1
                            children = children + [newboardstate]
                            newboardstate = []
                            for car in boardstate:
                                newboardstate.append(list(car))
                if (boardstate[i][3] != 1):
                    if car_array[carrow][carcol - 1] == 0:
                            newboardstate[i][3] = newboardstate[i][3] - 1
                            children = children + [newboardstate]
                            newboardstate = []
                            for car in boardstate:
                                newboardstate.append(list(car))

    for child in list(range(len(children))):
        for n in list(range(len(children[child]))):
            children[child][n] = tuple(children[child][n])

    return children               


        
def iterativedeepsearch(initialboardstate):
    """
Controls the depth of depth limited search
    """
    depth = 0;
    
    while ( dls(initialboardstate, depth) == None):
           depth = depth + 1
    return dls(initialboardstate, depth)

def getheuristicval(boardstate):
    """
    Gets the heuristic value for the given boardstate. The value is spaces needed to move
    the ice cream truck plus cars in the way
    """
    cararray = initializeboard(boardstate)
    stepstotake = 5 - boardstate[0][3]

    startindex = boardstate[0][3] - 1
    carsinway = 0
    while startindex != 6:
        if cararray[2][startindex] == 1:
            carsinway = carsinway + 1
        startindex = startindex + 1
    return (carsinway - 2) + stepstotake
        
        
        
    

def Astar(initialboardstate):
    rootnode = node(getheuristicval(initialboardstate), initialboardstate) #Rootnode set to initialboardstate


    openset = [] #Currently evaluating nodes
    closedset = []#Nodes already evaluated

    heapq.heapify(openset)

    
    heapq.heappush(openset, rootnode)
    #Keeps heuristic value in node, determines where to move from children heuristic value
    
    while len(openset) != 0:
        current = heapq.heappop(openset)      #Current = the node with the lowest heuristic value
        if current.boardstate[0][3] == 5:     #Base Case current is equal to goal
            return current.boardstate
        
        heapq.heappush(closedset, current)   #nodes has been evaluated
        
        children = generatemoves(current.boardstate, initializeboard(current.boardstate))
        for child in children:
            child = node(getheuristicval(child), child)  #Push all the children onto the q to be evaluated
            if not(child in openset):
                heapq.heappush(openset, child) #Discovered a new node
           
            heapq.heappush(openset, child)
            
    return False
        
        
