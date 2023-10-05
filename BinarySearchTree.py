class Node:
    def __init__(self, key):
        self.key = key #value of the node
        self.left = None #ref to the left child node
        self.right = None #ref to the right child node

class BinarySearchTree:
    def __init__(self):
        self.root = None #ref to the root node of the bst

    def insert(self, key):
        if self.root is None: #if the tree is empty
            self.root = Node(key) #create a new node and set it as the root
        else:
            self._insert_recursive(self.root, key) #call the recursive insert function with the root
    
    def _insert_recursive(self, node, key):
        if key < node.key: #if the key is less than the current node's key
            if node.left is None: #if left child is empty
                node.left = Node(key) #create a new node and set it as the left child
            else:
                self._insert_recursive(node.left, key) #recursively insert in the left subtree
        else:
            if node.right is None: #if the right child is empty
                node.right = Node(key) #create a new node and set it as the right child
            else:
                self._insert_recursive(node.right, key) #recursively insert in the right subtree

    def search(self, key):
        return self._search_recursive(self.root, key) #call the recursive search function with the root

    def _search_recursive(self, node, key):
        if node is None or node.key == key: #if the node is None or the key is found
            return node #return the node(found) or None(not found)
        if key < node.key: #if the key is less than the current node's key
            return self._search_recursive(node.left, key) #recursively search in the left subtree
        else:
            return self._search_recursive(node.right, key) #recursively search in the right subtree
#Test the BST
bst = BinarySearchTree() #create a new BST object

#insert nodes
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)

#search for a key
print(bst.search(4).key) #print the key of the found node (4)
print(bst.search(10)) #print none