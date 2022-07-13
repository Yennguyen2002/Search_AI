from re import S
import numpy as np
from queue import PriorityQueue
import math


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

def reconstruct_path(visited, start, end):
    total_path = [end]
    while end in visited.keys():
        if (start == end):
            break

        end = visited[end]
        total_path.append(end)
    return total_path[::-1]

def Astar(matrix, start, end, pos):
    path=[]     # total path
    visited={}  #came from
    visited[start] = start

    heuristic = [[ 0 for i in range(len(matrix[_]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            heuristic[i][j] = math.sqrt((pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2)

    open_set = []
    open_set.append(start)
    
    g_score = [float("inf")] * len(matrix)
    g_score[start] = 0

    f_score = [float("inf")] * len(matrix)
    f_score[start] = heuristic[start][end]

    while open_set:
        cur = -1
        lowest_f_score = float("inf")
        for i in open_set:
            if f_score[i] < lowest_f_score :
                cur = i
                lowest_f_score = f_score[i]
        print("cur: ", cur)        
        open_set.remove(cur)

        if cur == end:
            path = reconstruct_path(visited, start, end)
            break
        
        for i in range(len(matrix[cur])):
            if matrix[cur][i] != 0 and ( i not in visited.keys()):
                if g_score[cur] + matrix[cur][i] < g_score[i]:
                    visited[i] = cur
                    g_score[i] = g_score[cur] + matrix[cur][i]
                    f_score[i] = g_score[i] + heuristic[i][end]
                    print("Updating distance of node ", i, " to ", g_score[i], " and priority to ", f_score[i])
                    
                    if i not in open_set:
                        open_set.append(i)


        print("visited: ", visited)
        print(open_set)

    print(visited)
    print(path)
    return visited, path

