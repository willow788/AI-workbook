minimax algorithm is one of the adversial earch methods that assumes that both the players are playing optimally and at their best performance
now we will understand the code's function blocks
1. check_winner:
   it takes two attributes board and players, board gives the current states of the tic tac toe grid, and player tells us which player is playing is it the machine or the human
   we have all the possible winning combinations predefined
   if board's combination matches any of the winnning combination then thw winner is declared any other combination is classified as draw

   2. minimax_search
      here 1st we are checking for the terminal cases,
      if x is winner will return 1
      if o is winner will return -1
      otherwise 0
      for draw

   3. is_maximising: here we are defining the maximumn score for the max player, for this example we are considering x as the maximising player,
      we are initialisng a variable as best_Score as - infiinty
      then we run a loop for to reach from 0 to 9 index : as in covering all the grid blocks
      if a grid block is empty we put x in there as it is the maximinsing function ad then we generate the score by alling recursive function and setting is_maximising to false as the next move is a min mov
      th the best score will the max btw current score and best score and it will be returned

      then and else statement executes similarly to generate the score of the min function

   4. finding the best move:
    best move is none initialised
      then we run the loop for all the grid and see which score tgives the best_Score and reset the best scoree to the current score and then chose the move that caused this score as the move

  after this this is a drivers function that can be understood very easily
  
