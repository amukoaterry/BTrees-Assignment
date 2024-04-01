class Binary:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None


def inOrderTraversal(node):
   if node is None:
       return
   inOrderTraversal(node.left)
   print(node.data, end=", ")
   inOrderTraversal(node.right)


root = Binary('one')
nodeone = Binary('two')
nodetwo = Binary('three')
nodethree = Binary('four')
nodefour = Binary('')
nodefive = Binary('six')
nodesix = Binary('seven')
nodeseven = Binary('eight')


root.left = nodeone
root.right = nodetwo


nodeone.left = nodethree
nodetwo.right = nodefour


nodetwo.left = nodefive
nodetwo.right = nodesix


nodethree.left = nodeseven


print("inOrderTraversal:")
inOrderTraversal(root)