class Node(object):
	def __init__(self, val, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right
	def __str__(self):
		return str(self.val)
	def __repr__(self):
		return str(self.val)
		
class BSTree(object):
	def __init__(self):
		self.root = None		
	def setRoot(self, root):
		self.root = root
	def add(self, val):
		if not self.root:
			self.setRoot(Node(val))
			return 
		if val in self:
			return 
		parent = None
		cur = self.root	
		while cur:
			parent = cur  
			cur = cur.left if val < cur.val else cur.right
		if val < parent.val:
			parent.left = Node(val)
		else:
			parent.right = Node(val)	
	def __contains__(self, val):
		return self.contains(val)
	def contains(self, val):
		if not self.root:
			return False 
		cur = self.root
		while cur:
			if cur.val == val: 
				return True
			cur = cur.left if val < cur.val else cur.right
		return False 
	def remove(val):
		pass

	def inOrder(self):
		stack = []
		cur = self.root
		inOrder = []
		while True:
			if cur:
				stack.append(cur)
				cur = cur.left 
			elif stack:
				cur = stack.pop()  
				inOrder.append(cur.val)
				cur = cur.right
			else:
				break
		return inOrder
	def postOrder(self):
			stack = []
			cur = self.root
			inOrder = []
			while True:
				if cur:
					stack.append(cur)
					cur = cur.left 
				elif stack:
					cur = stack.pop()  
					inOrder.append(cur.val)
					cur = cur.right
				else:
					break
			return inOrder



		
