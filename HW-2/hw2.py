# Haron Yunis
# yunhar04@evergreen.edu
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.



###
### Problem 1
###
import hw2_test

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"


y = 0
x = 1

while (x <= hw2_test.n):
    y= y+x
    x= x+1
print (y)


###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

a = 1.0
for x in range (2, 10):
    print a/x
###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"
n = 10
triangular = 0
for i in range (n+1):
    triangular = triangular
print "triangualr number", n, "via loop:", triangular
print "triangular number", n, "via formula:", n*(n+1)/2
###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"
n = 10
x = 1

for i in range(1, n+1):
        x = x * i
print x


###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10

for i in range(numlines, 0, -1):
    x = 1
    for m in range(1, i + 1):
        x = x * m
    print x
###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

numlines = 10
a = 1 

for i in range(1, numlines + 1):
    x = 1
    for b in range(1, i+1):
        x = x * b
        recip = 1.0/x
    a = a + recip
print a
###
### Collaboration
###

# Me and Ahmed Ali work together helped each other on problems we knew
#that the other didnt know.
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
