#!/usr/bin/env python3
#Henrik Vendel
#Adam Brattström


import bt
import sys
import logging

log = logging.getLogger(__name__)

class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        '''
        Returns true if the value `v` is a member of the tree.    
        '''

        if  self.is_empty():
            return False
        elif self.get_value() < v:
            return self.get_rc().is_member(v)
        elif self.get_value() > v:
            return self.get_lc().is_member(v)
        elif self.get_value()==v:
            return True

    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''

        if self.is_empty():
            return 0
        else:
            return ((self.get_lc().size()) + 1 + (self.get_rc().size()))
        
        

    def height(self):
        '''
        Returns the height of the tree.
        '''
        if self.is_empty():
            return 0
        elif self.get_lc().height() > self.get_rc().height():
            return 1 + self.get_lc().height()
        elif self.get_rc().height() >= self.get_lc().height():
            return 1 + self.get_rc().height()


    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.get_value()] + self.get_lc().preorder() + self.get_rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.is_empty():
            return []
        return self.get_lc().inorder() + [self.get_value()] + self.get_rc().inorder()


    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        
        if self.is_empty():
            return []
        return self.get_lc().postorder() + self.get_rc().postorder() + [self.get_value()]


    def find_max(self):
        '''
        Returns highest value of the tree
        '''

        if (self.is_empty()):
            return 0
        
        result = self.get_value()
        left_res = self.get_lc().find_max()
        right_res = self.get_rc().find_max()

        if(left_res > result):
            result = left_res
        if(right_res > result):
            result = right_res

        return result
    
    def find_min(self):
        '''
        Returns lowest value of tree
        '''
        if (self.is_empty()):
            return float('inf')
        
        result = self.get_value()
        left_res = self.get_lc().find_min()
        right_res = self.get_rc().find_min()

        if(left_res < result):
            result = left_res
        if(right_res < result):
            result = right_res

        return result

    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).

        For example, consider the following tree `t`:
                    10
              5           15
           *     *     *     20

        The output of t.bfs_order_star() should be:
        [ 10, 5, 15, None, None, None, 20 ]
        '''
        
        height = self.height()
        my_array = []

        for i in range(1, height+1):
            self.add_level(i, my_array)

        return my_array
    
    def add_level(self, level, arr):
        '''
        Add each level in the tree
        '''
        if(self.is_empty()):
            stars = 2**(level-1)
            for i in range(stars):
                arr.append(None)
        elif(level == 1):
            arr.append(self.get_value())
        elif(level > 1):
            self.get_lc().add_level(level-1, arr)
            self.get_rc().add_level(level-1, arr)
        
    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.get_value():
            return self.cons(self.get_lc().add(v), self.get_rc())
        if v > self.get_value():
            return self.cons(self.get_lc(), self.get_rc().add(v))
        return self

    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        if(self.is_empty()):
            return self
        
        if(self.get_value()==v): 
            self._delete()
        elif(self.get_value()>v):
            self.get_lc().delete(v)
        elif(self.get_value()<v):
            self.get_rc().delete(v)
        return self
    
    def _delete(self):
        '''
        When value is found, remove node and move childs, if there are any, accordingly
        '''
        if(self.get_lc().is_empty() and self.get_rc().is_empty()):
            self.set_value(None)
        elif(self.get_lc().is_empty()):
            self.set_value(self.get_rc().get_value())
            self.set_lc(self.get_rc().get_lc())
            self.set_rc(self.get_rc().get_rc())
        elif(self.get_rc().is_empty()):
            self.set_value(self.get_lc().get_value())
            self.set_rc(self.get_lc().get_rc())
            self.set_lc(self.get_lc().get_lc())
        else:
            self._delete_two()

        return self


    def _delete_two(self):
        
        '''
        If the node that is to be removed has two childs, check size of each and move
        accordingly and set the new nodes value and childs
        '''
        left_height = self.get_lc().height()   
        right_height = self.get_rc().height() 
        if(left_height>=right_height):
            max = self.get_lc().find_max()
            self.set_value(max)
            self.set_lc(self.get_lc().delete(max))
        else:
            min = self.get_rc().find_min()
            self.set_value(min)
            self.set_rc(self.get_rc().delete(min))
        return self


if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
