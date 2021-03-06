from btnode import Node
class LinkedBinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None


    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = LinkedBinaryTree(new_node)
        else:
            t = LinkedBinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t


    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = LinkedBinaryTree(new_node)
        else:
            t = LinkedBinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t


    def get_right_child(self):
        return self.right_child


    def get_left_child(self):
        return self.left_child


    def set_root_val(self, obj):
        self.key = obj


    def get_root_val(self):
        return self.key


    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()


    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.key)
        if self.right_child:
            self.right_child.inorder()


    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key)


    # def __str__(self):
    #     """Returns a string representation with the tree rotated
    #     90 degrees counterclockwise."""

    #     def recurse(node, level):
    #         s = ""
    #         if node != None:
    #             s += recurse(node.right, level + 1)
    #             s += "| " * level
    #             s += str(node.data) + "\n"
    #             s += recurse(node.left, level + 1)
    #         return s

    #     return recurse(self.key, 0)
# n = Node(1)
# a = LinkedBinaryTree(n)
# print(a.insert_left(Node(10)))
# print(a.insert_right(Node(11)))
# print(a)
