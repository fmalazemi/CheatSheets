class Node(object):
	def __init__(self, val, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right
	def __str__(self):
		return str(self.val)
	def __repr__(self):
		return str(self.val)
		
class Tree(object):
	def __init__(self, root = None):
		self.root = root		
	def setRoot(self, root):
		self.root = root
	def add(self, val):
		if not self.root:
			self.setRoot(node)
			return 
		if val in self:
			print(val, "already exists in the Tree.")
			return 
		parent = None
		cur = self.root	
		while cur:
			parent = cur 
			cur = cur.left if val > cur.val else cur.right
		if parent.val > val:
			parent.left = Node(val)
		else:
			parent.right = node

	def __contains__(self, val):
		return self.contains(val)
	def contains(self, val):
		if not self.root:
			return False 
		while cur:
			if cur.val == node.val:
				return True 
			cur = cur.left if val > cur.val else cur.right
		return False 
	def remove(val):
		pass
	def inorder(self):
		stack = [self.root]
		cur = self.root
		inOrder = []
		while stack:
			if not cur: 
				stack.append(cur)
				cur = cur.left 
			elif stack:
				cur = stack.pop() 
				inOrder.append(cur.val)
				cur = cur.right
			else:
				break
		return inOrder  
				
			
	
		
					
		
		
		
		
