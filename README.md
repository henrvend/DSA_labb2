# Lab: tree-based data structures
This document provides a cheat-sheet on how to work with the provided
start-code.

## Use available options
```
$ ./bin/main --help
usage: Terminal-based UI for BST/AVL trees [-h] [--log-level LOG_LEVEL]
                                           [--mode MODE] [--echo]


optional arguments:
  -h, --help            show this help message and exit
  --log-level LOG_LEVEL, -l LOG_LEVEL
                        Minimum verbosity for logging. Available in ascending
                        order: debug, info, warning, error, crirical.
  --mode MODE, -m MODE  Tree mode. Available options: bst, avl.
  --echo, -e            Echo input. Useful if redirecting input from file
```

As shown above, you can specify if the program should use a BST or an AVL tree.
The default is BST, and you can change it by setting the AVL mode:
- Run in BST mode: `./bin/main`
- Run in AVL mode: `./bin/main -m avl`

The echo option is useful if you want to redirect input from a file. It will
cause each input to be printed to stdout.
- Run normally: `./bin/main`
- Run with input from file: `./bin/main -e < some_input.txt`

If you'd like to use python's logging module for debugging purposes, set the
logging level accordingly:
- Show all logging statements: `./bin/main -l debug`
- Show all but debug statements: `.bin/main -l info`
- Only show warning, error, and critical statements: `./bin/main -l warning`

There are examples of both debug and info statements in the start code, e.g.,
`log.debug("calling bst.BST.add() explicitly from child")` and
`log.info("Running in BST mode")`.
#   D S A _ l a b b 2  
 