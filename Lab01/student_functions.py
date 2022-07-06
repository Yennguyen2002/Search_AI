import numpy as np
from queue import PriorityQueue


def DFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 
   
    n = len(matrix)
    path = []
    visited = {}
    
    visited[start] = start
    def DFS_Search(matrix, start, end):
        if start == end:
            return 
        for i in range (n):
            if (matrix[start][i] == 1 and (i not in visited.keys())):
                visited[i] = start
                DFS_Search(matrix,i,end)

    DFS_Search(matrix,start,end)
    print(visited)

    def findPath(visited,path, start, end):
        t = end
        path.append(t)
        while(1):
            #print(visited[t])
            #print(path)
            path.append(visited[t])
            if visited[t] == start:
                return
            t = visited[t]
            
    
    
    findPath(visited,path, start, end)
    print(path)
    return visited, path[::-1]

def BFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    path=[]
    visited={}
   
    return visited, path


def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:  
    path=[]
    visited={}
    q = PriorityQueue()

    visited[start] = start
    q.put((0, start, [start])) 

    while not q.empty():
        CurNode = q.get()
        print("---------")
        print(CurNode)
        for i in range(len(matrix)):
            if matrix[CurNode[1]][i] != 0:
                print("i: ", i )
                print(CurNode)
                visited[i] = CurNode[1]
                temp_path = []
                temp_path[:] =  CurNode[2]
                temp_path.append(i)

                #print((CurNode[0] + matrix[CurNode[1]][i], i, temp_path))
                q.put((CurNode[0] + matrix[CurNode[1]][i], i, temp_path))
                if temp_path[-1] == end:
                    print(temp_path)
                    print(visited)
                    return visited, temp_path
                
                
    return visited, path


def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    return visited, path

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    return visited, path

