class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        curr = self.root
        while True:
            if data < curr.data:
                if curr.left is None:
                    curr.left = new_node
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = new_node
                    break
                curr = curr.right

    def search(self, key):
        curr = self.root
        while curr:
            if curr.data == key:
                return True
            elif key < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def get_successor(self, node):
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr

    def delete(self, key):
        parent = None
        curr = self.root
        while curr:
            if curr.data == key:
                # Found key

                if curr.left is None and curr.right is None:
                    # No child case
                    if curr == self.root:
                        self.root = None
                    elif parent.left == curr:
                        parent.left = None
                    else:
                        parent.right = None

                return True

            parent = curr
            if key < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        return False  # If key not found

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)
# driver code


bst = BST()
# Insert nodes
bst.insert(10)
bst.insert(5)

# Search 
print(bst.search(10))
print(bst.search(2))

# Delete
bst.delete(5)
print(bst.search(5))
