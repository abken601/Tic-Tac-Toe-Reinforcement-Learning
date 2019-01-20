# Tic-Tac-Toe-Reinforcement-Learning

This project tackles Tic-Tac-Toe game using reinforcement learning method. Tic Tac Toe players on a 3x3 board and is well-known a "must-draw" game with an educated strategy. We demonstrate how this strategy can be trained with reinforcement learning method. The number of state of this game can be roughly estimated by 3^9 = 19,683 states, a very good number for a normal desktop computer can afford to. We use three temporal difference methods to train our strategy, because the model is known and therefore a value-table suffices to this problem. One can try to use Sarsa or Q-learning methods, literally they converge to the same optimal strategy.

We train our model for 30,000 iterations, in every 2,000 iterations we use the 'trained' model to play 1,000 games and collect some stats, the result is as follows.

Round 2000 X wins: 51.2 %, O wins 34.1 %, Draw is  14.7 %

Round 4000 X wins: 34.3 %, O wins 16.5 %, Draw is  49.2 %

Round 6000 X wins: 10.4 %, O wins 3.3 %, Draw is  86.3 %

Round 8000 X wins: 5.0 %, O wins 1.0 %, Draw is  94.0 %

Round 10000 X wins: 1.4 %, O wins 1.2 %, Draw is  97.4 %

Round 12000 X wins: 1.3 %, O wins 0.0 %, Draw is  98.7 %

Round 14000 X wins: 0.5 %, O wins 0.2 %, Draw is  99.3 %

Round 16000 X wins: 0.7 %, O wins 0.0 %, Draw is  99.3 %

Round 18000 X wins: 0.0 %, O wins 0.0 %, Draw is  100.0 %

Round 20000 X wins: 0.3 %, O wins 0.0 %, Draw is  99.7 %

Round 22000 X wins: 0.6 %, O wins 0.0 %, Draw is  99.4 %

Round 24000 X wins: 0.0 %, O wins 0.0 %, Draw is  100.0 %

Round 26000 X wins: 0.0 %, O wins 0.0 %, Draw is  100.0 %

Round 28000 X wins: 0.0 %, O wins 0.0 %, Draw is  100.0 %

Round 30000 X wins: 0.0 %, O wins 0.0 %, Draw is  100.0 %

Our trained strategy is an optimal one. Convergence occurs roughly at round 20,000. You may try the same by running main.py from the repository.

We extend our method to a 4x4 board, the winning combinations are defined as: 4 four-in-a-rows, 4 four-in-a-columns, two diagonals, 9 2x2 squares. The number of state of this variation is much larger, roughly equal to 3^16 = 43,046,721 states. Luckily it is still affordable to a normal desktop but requires more computational time for an optimal strategy to be trained. 

We train our model for 30,000 iterations, and in every 2,000 iterations we use the 'trained' model to play 1,000 games and collect some stats, in order to compare the 3x3 result.

Round 2000 X wins: 40.3 %, O wins 32.3 %, Draw is  27.4 %

Round 4000 X wins: 43.1 %, O wins 31.9 %, Draw is  25.0 %

Round 6000 X wins: 37.7 %, O wins 35.2 %, Draw is  27.1 %

Round 8000 X wins: 43.6 %, O wins 32.0 %, Draw is  24.4 %

Round 10000 X wins: 40.4 %, O wins 30.4 %, Draw is  29.2 %

Round 12000 X wins: 38.9 %, O wins 33.1 %, Draw is  28.0 %

Round 14000 X wins: 44.1 %, O wins 30.4 %, Draw is  25.5 %

Round 16000 X wins: 41.6 %, O wins 32.1 %, Draw is  26.3 %

Round 18000 X wins: 42.0 %, O wins 31.2 %, Draw is  26.8 %

Round 20000 X wins: 42.7 %, O wins 31.5 %, Draw is  25.8 %

Round 22000 X wins: 44.4 %, O wins 31.1 %, Draw is  24.5 %

Round 24000 X wins: 42.6 %, O wins 32.3 %, Draw is  25.1 %

Round 26000 X wins: 44.7 %, O wins 30.2 %, Draw is  25.1 %

Round 28000 X wins: 41.3 %, O wins 29.9 %, Draw is  28.8 %

Round 30000 X wins: 42.5 %, O wins 31.5 %, Draw is  26.0 %

For the result, there is no hint of how an optimal strategy performs. We do not see the convergence tendency neither. If you set the training iteration to over one million, you will see the optimal strategy gives you a "Draw" result with 100%. 
