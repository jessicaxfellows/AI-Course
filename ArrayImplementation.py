class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root, result=[]):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)
    return result

def tree_to_array(root):
    result = []
    inorder_elements = inorder_traversal(root)
    for element in inorder_elements:
        result.append(element)
    return result

# Example Usage
if __name__ == "__main__":
    keys = [5, 3, 7, 2, 4, 6, 8]
    root = None
    for key in keys:
        root = insert(root, key)

    tree_array = tree_to_array(root)
    print("Binary Tree stored in an array:", tree_array)
