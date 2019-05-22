import unittest
import Tree
from random import shuffle


class TestBSTree(unittest.TestCase):
	def test_inorder(self):
		
		A = [ 
		[0, 0, 0, 0, 0, 0, 0],
		[1, 1, 1, 1, 1, 1, 1],
		[1, 2, 1, 2, 1, 2, 1],
		[1, 1, 1, 2, 2, 2, 2],
		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
		[14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
		[10, 3, 0, 8, 9, 12, 2, 1, 14, 11, 13, 7, 4, 6, 5],
		[8, 11, 12, 0, 2, 6, 14, 3, 13, 1, 7, 5, 9, 10, 4],
		]	
		for L in A:
			T = Tree.BSTree()
			for i in L:
				T.add(i)
			tmp = sorted(list(set(L)))
			self.assertEqual(tmp, T.inOrder(), f"Expected {tmp} result {T.inOrder()}")
if __name__ == '__main__':
	unittest.main()
