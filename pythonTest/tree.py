import queue

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def dfs_re1(root):
    if not root:
        return 
    else:
        print(root.val)
        dfs_re1(root.left)
        dfs_re1(root.right)
        
def dfs_re2(root):
    if not root:
        return 
    else:
        
        dfs_re2(root.left)
        print(root.val)
        dfs_re2(root.right)
        
        
def dfs_re3(root):
    if not root:
        return 
    else:
        
        dfs_re3(root.left)
        dfs_re3(root.right)
        print(root.val)
def bfs(root):
    node_queue=queue.Queue()
    node_queue.put(root)
    while not node_queue.empty():
        curr_node=node_queue.get()
        if curr_node:
            print(curr_node.val)
            node_queue.put(curr_node.left)
            node_queue.put(curr_node.right)

def dfs_stack1(root):
    stackList=[root]   
    left_visited=set()
    right_visited=set()

    while stackList:    
        root=stackList[-1]
        if root is None:
            stackList.pop()
            #root=stackList[-1]
            '''
            root=stackList[-1]
            stackList.append(root.right)
            root=root.right
            '''
        else:           
            if root not in right_visited and root not in left_visited:                
                print(root.val)
                stackList.append(root.left)
                left_visited.add(root)
                #root=root.left
            
            elif root not in right_visited and root in left_visited:
                stackList.append(root.right)
                right_visited.add(root)
                #root=root.right
            
            
            elif root in right_visited and root in left_visited:
                stackList.pop()
                #if 
                #root=stackList[-1]
            
            
            else:
                raise ValueError
                
                
def dfs_stack2(root):
    stackList=[root]   
    left_visited=set()
    right_visited=set()

    while stackList:    
        root=stackList[-1]
        if root is None:
            stackList.pop()
            #root=stackList[-1]
            '''
            root=stackList[-1]
            stackList.append(root.right)
            root=root.right
            '''
        else:           
            if root not in right_visited and root not in left_visited:                
                
                stackList.append(root.left)
                left_visited.add(root)
                #root=root.left
            
            elif root not in right_visited and root in left_visited:
                print(root.val)
                stackList.append(root.right)
                right_visited.add(root)
                #root=root.right
            
            
            elif root in right_visited and root in left_visited:
                stackList.pop()
                #if 
                #root=stackList[-1]
            
            
            else:
                raise ValueError
    
        



def main():
    '''
    Construct Tree
            A
           / \
          B   C
         /   / \
        D   E   F
    '''
    
    A=Node('A')
    B=Node('B')
    C=Node('C')
    D=Node('D')
    E=Node('E')
    F=Node('F')
    A.left=B
    A.right=C
    B.left=D
    C.left=E
    C.right=F
    print('DFS-------')
    dfs_re1(A)
    print('BFS-------')
    bfs(A)

    
    
main()
