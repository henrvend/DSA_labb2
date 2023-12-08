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
        super().add(v)
        return self.balance()
    
    def delete(self, v):
        super().delete(v)
        return self.balance()

    def balance_factor(self):
        return self.get_lc().height()-self.get_rc().height()
        

    def balance(self):
        '''
        AVL-balances around the node rooted at `self`.  In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''
        if self.is_empty():
            return self
        
        
        if self.balance_factor() >= 2:
            #print("VTungt")
            if self.get_lc().get_lc().height() >= self.get_lc().get_rc().height():
                #print("VVtungt: srr")
                return self.srr()
            else:
                #print("VHtung: drr")
                return self.drr()

        elif self.balance_factor() <= -2:
            #print("Htungt")  
            if self.get_rc().get_rc().height() >= self.get_rc().get_lc().height():
                #print("HHtungt: slr") 
                self = self.slr()
                return self
            else:
                #print("HVtung: dlr")
                return self.dlr()

        return self

    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        ''' 
        
        y = self.get_rc()
        self.set_rc(y.get_lc())
        y.set_lc(self)
        return y


    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        y = self.get_lc()
        self.set_lc(y.get_rc())
        y.set_rc(self)
        return y

    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''

        new_head = self.get_rc().srr()
        self.set_rc(new_head)
        return self.slr()


    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''

        new_head = self.get_lc().slr()
        self.set_lc(new_head)
        return self.srr()


if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
