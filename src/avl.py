#!/usr/bin/env python3

import sys
import bst
import logging

log = logging.getLogger(__name__)

class AVL(bst.BST):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def add(self, v):


        if self.is_empty():
            self.__init__(value=v)
            return self
        if self.get_value==v:
            return self
        if v < self.get_value():
            self.cons(self.get_lc().add(v), self.get_rc())
            self.balance()
            return self
        if v > self.get_value():
            self.cons(self.get_lc(), self.get_rc().add(v))
            self.balance()
            return self
        

    
        '''
        Example which shows how to override and call parent methods.  You
        may remove this function and overide something else if you'd like.
        '''
        log.debug("calling bst.BST.add() explicitly from child")
        # TODO: apply balance() correctly for add/delete
        return super().add(v)

    def balance(self):
        '''
        AVL-balances around the node rooted at `self`.  In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''


        if ((self.get_lc().height()-self.get_rc().height())==2):
            self.balance()
        elif((self.get_lc().height()-self.get_rc().height())==-2):
            self.balance()


        log.info("TODO@src/avl.py: implement balance()")
        self.slr().srr().dlr().drr() # TODO: apply these methods correctly
        return self

    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        log.info("TODO@src/avl.py: implement slr()")
        return self

    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        log.info("TODO@src/avl.py: implement srr()")
        return self

    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        log.info("TODO@src/avl.py: implement drl()")
        return self

    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        log.info("TODO@src/avl.py: implement drr()")
        return self
    

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
        


if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
