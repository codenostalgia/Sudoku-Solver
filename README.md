# Sudoku-Solver-using-backtracking-algorithm
Sudoku Solver using backtracking algorithm


Algorithm-
1) for the given board first we have to find the empty cell in the board( empty place is filled by 0 in board ) , so we actually search for 0 in the board using "find_empty" function.
2) When we encounter a zero, we will try to fill that position using a number in 1-9.
3) I used a for loop to insert a number.
4) Suppose we are trying to fill 1 in it, then the next task will be to check that, after filling the number , is it a valid board ? is it satisfying the rules of Sudoku ?
5) To check the validity of board , I defined a "Valid" function, which will check that, the board satisfy the rules or not. if satisfies then returns True or else False.
6) let say, for a empty place, If 1 is satisfying the condition, then we will put it at that empty place.
7) After that, we will look for next empty place and fill it in the same as way as previous one.
8) For moving forward in board i used RECURSION.
9) Suppose if a case arise, where at a empty place, any number from 1-9 is not valid , it means that , we have done some mistake in filling a number at some previous empty place.
10) For that in each recursive case i returned TRUE if board is solved  completely and False if board is not solved.
11) if returned false, we will go to previous empty place and increment it by 1 (by for loop) and again move forward.
This will go on until the board is fully solved.
11) The base condition for the recursion will be to return TRUE when we are  done with all the empty places i.e board fully solved.
