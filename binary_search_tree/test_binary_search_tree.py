import unittest
import numpy as np
from .binary_search_tree import *


class TestBinarySearchTree(unittest.TestCase):

    def test_minimum(self):
        for i in range(1, 100):
            elements = np.random.random(i) * 100 - 50
            min_element = min(elements)
            tree = BinarySearchTree()
            for element in elements:
                tree.insert(element)

            self.assertEqual(tree.minimum(), min_element)

    def test_maximum(self):
        for i in range(1, 100):
            elements = np.random.random(i) * 100 - 50
            max_element = max(elements)
            tree = BinarySearchTree()
            for element in elements:
                tree.insert(element)

            self.assertEqual(tree.maximum(), max_element)

    def test_tree_structure_basic(self):
        for i in range(1, 100):
            elements = np.random.random(i) * 100 - 50
            tree = BinarySearchTree()
            for element in elements:
                tree.insert(element)

            self.assertEqual(tree.to_sorted_array(), sorted(elements))

    def test_tree_height(self):
        elements_and_heights = [
            ([1, 2, 3, 4, 5, 6], 6),
            ([6, 5, 4, 3, 2, 1], 6),
            ([2, 1, 3], 2),
            ([20, 10, 30, 15, 5], 3),
            ([20, 10, 30, 15, 16], 4),
        ]

        for (elements, height) in elements_and_heights:
            tree = BinarySearchTree()
            for element in elements:
                tree.insert(element)
            self.assertEqual(height, tree.height())

    def test_find(self):
        test_data = [
            ([1, 2, 3, 4, 5, 6], 4, True),
            ([6, 5, 4, 3, 2, 1], 19, False),
            ([2, 1, 3], 54, False),
            ([20, 10, 30, 15, 5], 15, True),
            ([20, 10, 30, 15, 16], 4, False),
        ]

        for (elements, x, answer) in test_data:
            tree = BinarySearchTree()
            for element in elements:
                tree.insert(element)
            self.assertEqual(tree.find(x), answer)

    def test_successor(self):
        test_data = [
            ([1, 2, 3, 4, 5, 6], 4, 5),
            ([6, 5, 4, 3, 2, 1], 1, 2),
            ([2, 1, 3], 3, None),
            ([20, 10, 30, 15, 5], 15, 20),
            ([20, 10, 30, 15, 16], 15, 16),
        ]

        for (elements, x, answer) in test_data:
            tree = BinarySearchTree()
            for element in elements:
                tree.insert(element)

            node = tree.root.find_in_subtree(x)
            successor = node.successor()
            self.assertTrue((successor is None) == (answer is None))
            if successor is not None and answer is not None:
                self.assertTrue(successor.value == answer)

    def test_delete_case1(self):
        # case 1.1
        node15 = BinarySearchTree.Node.leaf_node(15)
        node25 = BinarySearchTree.Node.leaf_node(25)
        node20 = BinarySearchTree.Node.with_children(node15, 20, node25)

        node55 = BinarySearchTree.Node.leaf_node(55)
        node65 = BinarySearchTree.Node.leaf_node(65)
        node60 = BinarySearchTree.Node.with_children(node55, 60, node65)

        node70 = BinarySearchTree.Node.with_children(node60, 70, None)

        root = BinarySearchTree.Node.with_children(node20, 50, node70)

        tree = BinarySearchTree()
        tree.root = root

        tree.delete(15)
        self.assertEqual(False, tree.find(15))

        # case 1.2
        node15 = BinarySearchTree.Node.leaf_node(15)
        node25 = BinarySearchTree.Node.leaf_node(25)
        node20 = BinarySearchTree.Node.with_children(node15, 20, node25)

        node55 = BinarySearchTree.Node.leaf_node(55)
        node65 = BinarySearchTree.Node.leaf_node(65)
        node60 = BinarySearchTree.Node.with_children(node55, 60, node65)

        node70 = BinarySearchTree.Node.with_children(node60, 70, None)

        root = BinarySearchTree.Node.with_children(node20, 50, node70)

        tree = BinarySearchTree()
        tree.root = root

        tree.delete(65)
        self.assertEqual(False, tree.find(65))

    def test_delete_case2(self):
        # case 2.1
        node15 = BinarySearchTree.Node.leaf_node(15)
        node25 = BinarySearchTree.Node.leaf_node(25)
        node20 = BinarySearchTree.Node.with_children(node15, 20, node25)

        node55 = BinarySearchTree.Node.leaf_node(55)
        node65 = BinarySearchTree.Node.leaf_node(65)
        node60 = BinarySearchTree.Node.with_children(node55, 60, node65)

        node70 = BinarySearchTree.Node.with_children(node60, 70, None)

        root = BinarySearchTree.Node.with_children(node20, 50, node70)

        tree = BinarySearchTree()
        tree.root = root

        tree.delete(70)
        self.assertEqual(False, tree.find(70))

    def test_delete_case31(self):
        # case 3.1
        node15 = BinarySearchTree.Node.leaf_node(15)
        node25 = BinarySearchTree.Node.leaf_node(25)
        node20 = BinarySearchTree.Node.with_children(node15, 20, node25)

        node55 = BinarySearchTree.Node.leaf_node(55)
        node65 = BinarySearchTree.Node.leaf_node(65)
        node60 = BinarySearchTree.Node.with_children(node55, 60, node65)

        node70 = BinarySearchTree.Node.with_children(node60, 70, None)

        root = BinarySearchTree.Node.with_children(node20, 50, node70)

        tree = BinarySearchTree()
        tree.root = root

        tree.delete(20)
        self.assertEqual(False, tree.find(20))

    def test_delete_case32(self):
        # case 3.2
        node15 = BinarySearchTree.Node.leaf_node(15)
        node25 = BinarySearchTree.Node.leaf_node(25)
        node20 = BinarySearchTree.Node.with_children(node15, 20, node25)

        node65 = BinarySearchTree.Node.leaf_node(65)
        node60 = BinarySearchTree.Node.with_children(None, 60, node65)

        node70 = BinarySearchTree.Node.with_children(node60, 70, None)

        root = BinarySearchTree.Node.with_children(node20, 50, node70)

        tree = BinarySearchTree()
        tree.root = root

        tree.delete(50)
        self.assertEqual(False, tree.find(50))

    def test_is_correct(self):
        # case 3.2
        node15 = BinarySearchTree.Node.leaf_node(15)
        node25 = BinarySearchTree.Node.leaf_node(25)
        node20 = BinarySearchTree.Node.with_children(node15, 20, node25)

        node65 = BinarySearchTree.Node.leaf_node(65)
        node60 = BinarySearchTree.Node.with_children(None, 60, node65)

        node70 = BinarySearchTree.Node.with_children(node60, 70, None)

        root = BinarySearchTree.Node.with_children(node20, 50, node70)

        tree = BinarySearchTree()
        tree.root = root

        self.assertEqual(True, tree.is_correct())

        node15 = BinarySearchTree.Node.leaf_node(15)
        node25 = BinarySearchTree.Node.leaf_node(25)
        root = BinarySearchTree.Node.with_children(node15, 10, node25)
        tree = BinarySearchTree()
        tree.root = root

        self.assertEqual(False, tree.is_correct())

    # def randomized_test