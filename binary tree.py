class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.insert(data)

    def lookup(self, key, parent=None):
		# Lookup node containing datareturns node and node's parent if found or None, None
        if key < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(key, self)
        elif key > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(key, self)
        else:
            return self, parent
        
    def children_count(self):
		#Returns the number of children for a given node		count = 0
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def descendant_count(self):
		#Counts all descendant nodes
        count = 0
        if self.left:
            count += 1 + self.left.descendant_count()
        if self.right:
            count += 1 + self.right.descendant_count()
        return count
    
    def delete(self, data):
		#Delete node containing data
        node, parent = self.lookup(data)
        if node:
            children_count = node.children_count()
            if children_count == 0:   # If node has no children then remove it
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif children_count == 1:
                if node.left:
                    child = node.left
                else:
                    child = node.right
                if parent:
                    if parent.left is node:
                        parent.left = child
                    else:
                        parent.right = child
                del node
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
    

def inorder(tree):
    if tree == None: return ''    
    return inorder(tree.left) + str(tree.data)+ ' ' + inorder(tree.right) 

tree = Tree(10)
tree.insert(6)
tree.insert(20)
tree.insert(4)
tree.insert(25)
tree.insert(15)
print('In Order Traversal')
print(inorder(tree))

tree.delete(6)
tree.delete(20)
print('In Order Traversal')
print(inorder(tree))
