# Names: Haron Yunis & Jessica Morton
# Evergreen Logins: morjes14 & yunhar04
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

def areaRectangle(w,h):
    area = w * h
    return area

w = 10
h = 5
myArea = areaRectangle(w,h)

print "Rectangle with width =", w, "height =", h, "has the area of", myArea

print
###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

w = 10
h = 2
myArea1 = areaRectangle(w,h)
print myArea1

w = 10
h = 3
myArea2 = areaRectangle(w,h)
print myArea2

w = 10
h = 4
myArea3 = areaRectangle(w,h)
print myArea3

areaDic = { 1:myArea1,
            2:myArea2,
            3:myArea3}
            
print areaDic

print
###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

for key in areaDic:
    print "Key:", key, "Area:", areaDic[key]

print
###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

for key, value in areaDic.iteritems():
    print "Key:", key, "Area:", value

print
###
### Problem 7
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

def sumNums(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum

myTotal = 0
n = 5
for i in range(n+1):
    myTotal = sumNums(n)
    
print "The Sum of numbers in range %d " %n + "= %d" %myTotal

print
###
### Collaboration
###http://www.pythonforbeginners.com/
# http://stackoverflow.com/questions/12964460/adding-numbers-in-a-range-with-for-loop