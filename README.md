# Part 1 of the technical test

## Language used - Python 3
## Question 1 - Factorial
### Notes
1. Classic recursion algorithm.
2. Time to solve - 15-20 mins

### Steps to run
1. Input the number on the command line you want to find the factorial for  
2. Enter!

### Updates
1. Memoized the intermediate values to reduce run time

## Question 2 - Sorting
### Notes
1. The algorithm goes like this:
  a) loop the array, starting from index 1 (2nd element) to index array.length-1(2nd last element)  
  b) if next number is greater than the current number, consider it a 'high'  
  c) if next number is lower than the current number, consider it a 'low'  
  d) The count of highs and lows decides whether to swap or reverse a sub-segment  
  e) if count is 2, swap  
  f) if count is 1, reverse the sub-segment  
  g) Although, if both solutions are valid, prefer swapping  
  h) If nothing works, print "no"  
2. Time to solve - Close to 2 hours  
3. It can be further optimized though.  

### Steps to run
1. Input the number of elements in the array, followed by the elements seperated by space.  
2. Enter!

## Question 3 - Matrix Rotation  
### Notes  
Algorithm:   
1. Rotate each layer of the matrix seperately starting with the outermost layer  
2. Keep solving until we reach the inner most layer  
3. Currently, it is using O(mn) extra space to copy the rotated matrix, should be optimized.  

### Steps to run  
1. Input the matrix dimensions and number of rotations (seperated by space)
2. Input the matrix elements row by row on each line
3. E.g.  
```
  4 4 2
  1 2 3 4
  5 6 7 8
  9 10 11 12
  13 14 15 16
```
