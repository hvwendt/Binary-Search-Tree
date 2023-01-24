#Harrison Wendt
#30353351
#Created: 10/31/2022
#Last modified: 10/31/2022
#binary_tree.py


from bnode import bNode

class BST: 

    def __init__(self):
        self._root = None 

    def search(self, key):  
        return self._recSearch(key, self._root)

    def _recSearch(self, key, curNode):
        if curNode == None:
            raise IndexError("Not in tree!")

        if curNode.entry == key:
             return curNode.entry

        if curNode.entry < key:
            return self._recSearch(key, curNode.right)
        if curNode.entry > key: 
            return self._recSearch(key, curNode.left)
        else:
            raise RuntimeError("Not in tree!")

    def add(self, entry): 
        if self._root == None:
            self._root = bNode(entry)
       
        elif self._root.entry < entry:
            if self._root.right == None:
                self._root.right = bNode(entry)
            else:
                self._recAdd(entry, self._root.right)

        elif self._root.entry > entry:
            if self._root.left == None:
                self._root.left = bNode(entry)
            else:     
                self._recAdd(entry, self._root.left)

        else:
            raise RuntimeError("No Duplicates! ")

    def _recAdd(self, entry, curNode):
        if curNode.entry < entry:
            if curNode.right == None:
                curNode.right = bNode(entry)
            else:
                self._recAdd(entry, curNode.right)

        elif curNode.entry > entry:
            if curNode.left == None: 
                curNode.left = bNode(entry)

            else:
                self._recAdd(entry, curNode.left)

        else:
            raise RuntimeError("No Duplicates!")

    def preOrder(self, visit):  
        if self._root != None:
            self._recPreOrder(visit, self._root)

    def _recPreOrder(self, visit, curNode):
        visit(curNode.entry)

        if curNode.left != None:
            self._recPreOrder(visit, curNode.left)

        if curNode.right != None:
            self._recPreOrder(visit, curNode.right)


    def inOrder(self, visit):  
        if self._root != None:
            self._recInOrder(visit, self._root)

    def _recInOrder(self, visit, curNode):
        if curNode.left != None: 
            self._recInOrder(visit, curNode.left)

        visit(curNode.entry)

        if curNode.right != None:
            self._recInOrder(visit, curNode.right)


    def postOrder(self, visit): 
        if self._root != None:
            self._recPostOrder(visit, self._root)

    def _recPostOrder(self, visit, curNode):
        if curNode.left!= None:
            self._recPostOrder(visit, curNode.left)

        if curNode.right!= None:
            self._recPostOrder(visit, curNode.right)

        visit(curNode.entry)