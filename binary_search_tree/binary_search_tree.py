class BinarySearchTree:
    """A class implementing basic binary search tree functionality"""
    # subclasses
    class Node:
        def __init__(self):
            self.value = None
            self.left = None
            self.right = None
            self.parent = None

        @classmethod
        def leaf_node(cls, value):
            node = cls()
            node.right = None
            node.left = None
            node.value = value
            return node

        @classmethod
        def with_children(cls, left, value, right):
            node = cls()
            node.right = right
            node.left = left

            if left is not None:
                left.parent = node

            if right is not None:
                right.parent = node
            node.value = value
            return node

        def successor(self):
            if self.right is not None:
                return self.right.minimum_in_subtree()
            x = self
            y = self.parent
            while (y is not None) and (x == y.right):
                x = y
                y = y.parent
            return y

        def minimum_in_subtree(self):
            if self.left is None:
                return self
            return self.left.minimum_in_subtree()

        def maximum_in_subtree(self):
            if self.right is None:
                return self
            return self.right.maximum_in_subtree()

        def find_in_subtree(self, value):
            if self.value == value:
                return self

            if value < self.value:
                return self.left.find_in_subtree(value) if self.left is not None else None
            else:
                return self.right.find_in_subtree(value) if self.right is not None else None

        def height(self):
            return self.__tree_height__(self)

        def insert(self, node):
            if self.value == node.value:
                return
            if node.value < self.value:
                if self.left is None:
                    self.left = node
                    node.parent = self
                else:
                    self.left.insert(node)
            else:
                if self.right is None:
                    self.right = node
                    node.parent = self
                else:
                    self.right.insert(node)

        def to_sorted_array(self):
            return (self.left.to_sorted_array() if self.left is not None else []) + [self.value] + (
                self.right.to_sorted_array() if self.right is not None else [])

        def is_correct_binary_search_tree(self):
            if (self.left is None) and (self.right is None):
                return True

            if self.left is not None:
                if self.left.value > self.value:
                    return False

            if self.right is not None:
                if self.right.value < self.value:
                    return False

            left_is_correct = self.left.is_correct_binary_search_tree() if self.left is not None else True
            right_is_correct = self.right.is_correct_binary_search_tree() if self.right is not None else True

            return left_is_correct and right_is_correct

        # private methods
        def __tree_height__(self, subtree):
            if subtree is None:
                return 0
            return 1 + max(self.__tree_height__(subtree.left), self.__tree_height__(subtree.right))

    # public methods
    def __init__(self):
        self.root = None

    def insert(self, x):
        node = self.Node()
        node.value = x

        if self.root is None:
            self.root = node
            return

        self.root.insert(node)

    def delete(self, x):
        node = self.root.find_in_subtree(x)

        if node is None:
            return

        # case 1 if x doesn't have any children
        if (node.left is None) and (node.right is None):
            if node.parent is None:
                self.root = None
            elif node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            return

        # case 2 if x has exactly one child (either left or right)
        if (node.left is None) != (node.right is None):
            child = node.left if (node.left is not None) else node.right
            parent = node.parent

            if parent is None:
                self.root = child
                child.parent = None
            elif parent.left == node:
                parent.left = child
                child.parent = parent
            else:
                parent.right = child
                child.parent = parent
            return

        # case 3 if x has two children
        minimum = node.right.minimum_in_subtree()

        # case 3.1 if x has two children and the minimum in the right subtree is a leaf node
        if minimum.right is None:
            minimum.right = node.right
            minimum.left = node.left
            minimum.parent = node.parent

            if node.parent is not None:
                if node == node.parent.left:
                    node.parent.left = minimum
                else:
                    node.parent.right = minimum
            else:
                self.root = minimum
            return

        # case 3.2 if x has two children and the minimum in the right subtree has the right child
        if minimum.right is not None:
            child = minimum.right
            minimum.parent.left = child
            child.parent = minimum.parent

            minimum.right = node.right
            minimum.left = node.left
            minimum.parent = node.parent

            if node.parent is not None:
                if node == node.parent.left:
                    node.parent.left = minimum
                else:
                    node.parent.right = minimum
            else:
                self.root = minimum
            return

    def minimum(self):
        return self.root.minimum_in_subtree().value

    def maximum(self):
        return self.root.maximum_in_subtree().value

    def find(self, x):
        return self.root.find_in_subtree(x) is not None

    def height(self):
        return self.root.height() if self.root is not None else 0

    def to_sorted_array(self):
        return self.root.to_sorted_array()

    def is_correct(self):
        return self.root.is_correct_binary_search_tree()


