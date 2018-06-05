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

### Sample test cases
Input 1
```
6
1 2 4 3 5 6
```

Input 2
```
6
43 65 1 98 99 101
```
Input 3
```
100
4104 8529 49984 54956 63034 82534 84473 86411 92941 95929 108831 894947 125082 137123 137276 142534 149840 154703 174744 180537 207563 221088 223069 231982 249517 252211 255192 260283 261543 262406 270616 274600 274709 283838 289532 295589 310856 314991 322201 339198 343271 383392 385869 389367 403468 441925 444543 454300 455366 469896 478627 479055 484516 499114 512738 543943 552836 560153 578730 579688 591631 594436 606033 613146 621500 627475 631582 643754 658309 666435 667186 671190 674741 685292 702340 705383 722375 722776 726812 748441 790023 795574 797416 813164 813248 827778 839998 843708 851728 857147 860454 861956 864994 868755 116375 911042 912634 914500 920825 979477
```

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
Input 1
```
  4 4 2
  1 2 3 4
  5 6 7 8
  9 10 11 12
  13 14 15 16
```
Input 2
```
5 4 7
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28
```
