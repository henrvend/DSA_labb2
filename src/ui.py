#!/usr/bin/env python3
#Henrik Vendel
#Adam Brattström

import sys
import bst
import avl
import logging

log = logging.getLogger(__name__)

class TerminalUI:
    def __init__(self, mode, echo=False):
        '''
        Select BST mode by passing "bst" as argument; otherwise select AVL mode.
        '''
        if mode == "bst":
            logging.info("running in BST mode")
            self._tree = bst.BST()
        else:
            logging.info("running in AVL mode")
            self._tree = avl.AVL()
        self._echo = echo

    def run(self):
        '''
        Provides a terminal-based UI to perform tree operations.
        '''
        self.display_menu()
        while True:
            opt, err = self.get_choice()
            if err is not None:
                self.display_error(err)
                continue

            if opt == "m":
                self.display_menu()
            elif opt == "t":
                self.display_tree()
            elif opt == "a":
                self.add_value()
            elif opt == "d":
                self.delete_value()
            elif opt == "f":
                self.is_member()
            elif opt == "q":
                break
            else:
                log.error("menu case '{}' is missing, aborting".format(opt))
                return 1

    def display_menu(self):
        '''
        Shows a menu which is encapsulated between a top rule and a bottom rule.
        '''
        print(self.menu_rule("top", self.menu_width()))
        for opt in self.menu_options():
            print("\t{}".format(opt))
        print(self.menu_rule("bot", self.menu_width()))

    def display_error(self, err):
        '''
        Shows an error message.
        '''
        print("error> {}".format(err))

    def display_tree(self):
        '''
        Shows the tree's structure and content.
        '''
        if self._tree.is_empty():
            print("\n  Tree is empty\n")

        self.show_2d()
        print("")
        print("Size:      {}".format(self._tree.size()))
        print("Height:    {}".format(self._tree.height()))
        print("Inorder:   {}".format(self._tree.inorder()))
        print("Preorder:  {}".format(self._tree.preorder()))
        print("Postorder: {}".format(self._tree.postorder()))
        print("BFS star:  {}".format([
            v if v is not None else "*" for v in self._tree.bfs_order_star()
        ]))
        print("")

    def add_value(self):
        '''add_value:
        Prompts the user for an integer which is added to the tree.
        '''
        value, err = self.get_int("Enter value to be added")
        if err is not None:
            self.display_error(err)
            return
        self._tree = self._tree.add(value)

    def delete_value(self):
        '''delete_value:
        Prompts the user for an integer which is removed from the tree.
        '''
        value, err = self.get_int("Enter value to be deleted")
        if err is not None:
            self.display_error(err)
            return
        self._tree = self._tree.delete(value)

    def is_member(self):
        '''is_member:
        Prompts the user for a value that is checked for membership in the tree.
        '''
        value, err = self.get_int("Enter search value")
        if err is not None:
            self.display_error(err)
            return

        print("\n  {} is a {}member\n".format(
            value,
            "" if self._tree.is_member(value) is True else "non-"),
        )

    def menu_rule(self, pos, width):
        '''
        Returns a horizontal line using stars or tildes.
        '''
        return ("*" if pos == "top" else "~") * width

    def menu_width(self):
        '''
        Returns the menu width.
        '''
        return 32

    def menu_options(self):
        '''
        Returns a list of printable menu options.  Blank entries will be interpreted
        as new lines, and single characters before the colon as hotkeys.
        '''
        return [
            "m: menu",
            "t: display tree",
            "",
            "a: add value",
            "d: delete value",
            "f: test membership",
            "",
            "q: quit",
        ]

    def menu_hotkeys(self):
        '''
        Returns a list of symbols that the menu defined as valid hotkeys.
        '''
        opts = self.menu_options()
        return [ o.split(":")[0] for o in opts if len(o.split(":")[0]) == 1 ]

    def get_choice(self):
        '''
        Attempts to read a valid menu option from the user.  Caller should look
        for errors by comparing the second return value against ``not None''.
        '''
        buf = input("menu> ")
        if self._echo:
            print(buf)

        if len(buf) != 1:
            return None, "input must be a a single character"
        if buf[0] not in self.menu_hotkeys():
            return None, "invalid choice"
        return buf[0], None

    def get_int(self, message):
        '''
        Writes a message to stdout and waits for an integer from stdin.
        '''
        buf = input("{}> ".format(message))
        if self._echo:
            print(buf)

        try:
            return int(buf), None
        except ValueError:
            return None, "invalid input (not an integer)"

    def show_2d(self):
        '''
        Shows a pretty 2D tree based on the output of bfs_order_star(). None
        values are are replaced by stars ("*").
        '''

        height = self._tree.height()    
        level = height
        arr = self._tree.bfs_order_star()
        start_value = 0
        count = 1
        longestInt = 0

        '''
        Find which value has most numbers in it 
        '''
        for i in arr:
            if(i==None):
                i=1
            current = str(i)
            if(len(current) > longestInt):
                longestInt = len(current)
        
        '''
        For each level in tree, print spaces and numbers 
        '''
        for i in range(height):
            
            '''
            Print the current level of the tree
            '''
            for j in range(start_value, start_value + count):
                offset = ((2**(level))*longestInt)
                
                print(end=" " * (offset))
                '''
                Set size of the number to take the same amount of space as the longest int in array and center it
                '''
                if arr[j]==None:
                    print('{message: ^{width}}'.format(message="*", width=longestInt), end="" ) 
                else:    
                    print('{message: ^{width}}'.format(message=str(arr[j]), width=longestInt), end="" ) 
                print(end=" " *(offset-longestInt))
                

            level = level -1
            print("\n")
            start_value += count
            count*=2

    
if __name__ == "__main__":
    log.critical("ui contains no main module")
    sys.exit(1)
