In this assignment you will have to implement algorithm 9C from the book: Construct a suffix tree for a string

The assignment is available in Gradescope as: https://www.gradescope.com/courses/358896/assignments/1822229 (Links to an external site.) .  For additional details, you can also see problem BA9C on Rosalind: http://rosalind.info/problems/ba9C/ (Links to an external site.) .

For this assignment your code should expect one file named "input" which contains a string of DNA letters, on one or more lines, and that ends with the special character $.

Your program must create a file called "output" which contains, on separate lines, each of the strings labeling the edges of the suffix tree constructed from the string provided in the input. 

Since neither the book nor Rosalind provide a good outline of the algorithm you can use to solve this problem, here's a brief outline in pseudocode:

>Construct a class that represents a suffix tree
>One possible solution creates a class for a node, which contains the following information:
> - label of edge leading into node from parent (can be either a string or coordinates within the string provided in the input)
> - dictionary of children indexed by the first character on the edges leading into each child.

Start by creating the root - an empty node
Process the string suffix by suffix, starting from root
For each suffix s
   set current node to be the root
   if current node has a child starting with the first character in s
       check character by character if suffix matches the label of edge
       if child reached before suffix is exhausted
           continue with child as current node, and s as remaining portion of suffix
       if mismatch found inside the edge
           create new node N that splits the edge at location of mismatch
           adjust link from parent and link to child accordingly
           create new leaf node as child of N, and label corresponding edge with remainder of suffix
           break;
     # Note, due to the $ character, it is not possible for suffix to end
     # in the middle of an edge
    if current node does not have child starting with first character in s
       create new leaf node as child of current node
       label the edge towards the leaf with s.
Also see 
https://youtu.be/JKi08gy56ZY
