# TreeMaker

I have developed this small application program for another project. It's raw and I made it for fun. But maybe you'll need it.
Maybe it will be better in the future.

**makeTree.py** creates a tree. Commands:
```
add node    create new node according to the node name and the parent name
remove nod  remove the node according to the node name
show        print the tree
save        save the tree to the file
```
And you can add several node with one parent with command `add 'parent': 'chile1', 'chile2'`.

makingTree.py example:
```
Create new tree? (y/n)
y
A root name: root
add root: a, b, c
add a: a1, a2
add c: qe, eq
add qe: qe1, qe2
print
|__ root
        |-- a
                |-- a1
                |__ a2
        |-- b
        |__ c
                |-- qe
                        |-- qe1
                        |__ qe2
                |__ eq
remove node qe
print
|__ root
        |-- a
                |-- a1
                |__ a2
        |-- b
        |__ c
                |__ eq
```

Alse there is a _python parser_ and _C# parser_. 
Python parser makes a dictionary form a _.tr_ format file (see examples).
C# one works only with a Tree class.
