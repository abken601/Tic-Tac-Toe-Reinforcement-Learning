from gameplay import TicTacToe3X3GamePlay, TicTacToe4X4GamePlay
from strategy import Strategy
from collections import defaultdict

class BotTraining:

    # initialize essential elements of a gameplay: current state, current player, etc
    def __init__(self):
        # dictionary: key = game state e.g. 'XOOOX-XXO'
        # this dict is the Q-table, stores rthe Q value for all combinations of states and actions
        self.valueTableDict = defaultdict(float)

        self.epsilon = 0.05
        self.alpha = 1.0
        self.strategy = Strategy()

    def TrainAndTestTicTacToe3X3GameBot (self, trainingIteration, testingPartition):

        for i in range(trainingIteration):

            if ((i+1)%testingPartition == 0):
                print("Round",(i+1),end=' ')
                self.TestTicTacToe3X3GameBotPerformance()

            # hit = 0, stick = 1
            nextState = None

            # if player wins dealer, reward = 1
            # if player draws dealer, reward = 0
            # if player loses dealer, reward = -1
            # used to update the V function
            winner = '-'
            fullGame = False

            # start a game
            gameplay = TicTacToe3X3GamePlay()

            # game proceeds only if (1) no one has won yet (2) the board is not full
            while (winner == '-' and fullGame == False):

                # get all possible next states
                possibleNextStates = gameplay.PossibleNextStates(gameplay.currentState)
                # get the corresponding value table dictionary for possible next states
                valueTablePossibleNextStateDict = self.strategy.ValueTablePossibleNextStateDict (possibleNextStates, self.valueTableDict)

                # find next state defined by the policy map
                # in training phase, use epsilon greedy policy
                # player 'X' wants to achieve the highest value
                if (gameplay.currentPlayer == 'X'):
                    nextState = self.strategy.EpsilonGreedyPolicyFromValueTableDict(valueTablePossibleNextStateDict, 'Max', self.epsilon)
                # player 'O' wants to achieve the lowest value
                elif (gameplay.currentPlayer == 'O'):
                    nextState = self.strategy.EpsilonGreedyPolicyFromValueTableDict(valueTablePossibleNextStateDict, 'Min', self.epsilon)

                # proceed the game to the next state
                gameplay.currentState = nextState

                # swap player's turn
                gameplay.currentPlayer = 'O' if gameplay.currentPlayer == 'X' else 'X'

                # update which player has won the game
                winner = gameplay.FindOutTheWinner(gameplay.currentState)

                # update if the board is full
                fullGame = gameplay.IsFullGame(gameplay.currentState)

                # get the reward given winner
                reward = gameplay.RewardOfGame(winner)

                # initialize the next state best value
                nextStateBestValue = 0.0

                if (winner == '-' and fullGame == False):
                    # get all possible next states
                    possibleNextStates = gameplay.PossibleNextStates(gameplay.currentState)

                    # get the corresponding value table dictionary for possible next states
                    valueTablePossibleNextStateDict = self.strategy.ValueTablePossibleNextStateDict(possibleNextStates, self.valueTableDict)

                    # get the best value for next state if next player is 'X'
                    if (gameplay.currentPlayer == 'X'):
                        nextStateBestValue = self.strategy.BestValueFromValueTableDict(valueTablePossibleNextStateDict, 'Max')
                    # get the best value for next state if next player is 'O'
                    elif (gameplay.currentPlayer == 'O'):
                        nextStateBestValue = self.strategy.BestValueFromValueTableDict(valueTablePossibleNextStateDict, 'Min')

                # update value table dictionary
                currentStateValue = self.valueTableDict[gameplay.currentState]
                nextStateValue = reward + nextStateBestValue
                self.valueTableDict[gameplay.currentState] = currentStateValue + self.alpha * (nextStateValue - currentStateValue)


    def TestTicTacToe3X3GameBotPerformance(self):

        # 'X', '-', 'O'
        result = [0,0,0]
        for i in range (1000):
            # start a game
            nextState = None

            # if player wins dealer, reward = 1
            # if player draws dealer, reward = 0
            # if player loses dealer, reward = -1
            # used to update the V function

            winner = '-'
            fullGame = False

            gameplay = TicTacToe3X3GamePlay()

            # game proceeds only if (1) no one has won yet (2) the board is not full
            while (winner == '-' and fullGame == False):

                # get all possible next states
                possibleNextStates = gameplay.PossibleNextStates(gameplay.currentState)

                # get the corresponding value table dictionary for possible next states
                valueTablePossibleNextStateDict = self.strategy.ValueTablePossibleNextStateDict(possibleNextStates, self.valueTableDict)

                # find next state defined by the policy map
                # in training phase, use epsilon greedy policy
                # player 'X' wants to achieve the highest value
                if (gameplay.currentPlayer == 'X'):
                    nextState = self.strategy.BestPolicyFromValueTableDict(valueTablePossibleNextStateDict, 'Max')
                # player 'O' wants to achieve the lowest value
                elif (gameplay.currentPlayer == 'O'):
                    nextState = self.strategy.BestPolicyFromValueTableDict(valueTablePossibleNextStateDict, 'Min')

                gameplay.currentState = nextState

                # swap player's turn
                gameplay.currentPlayer = 'O' if gameplay.currentPlayer == 'X' else 'X'

                # update which player has won the game
                winner = gameplay.FindOutTheWinner(gameplay.currentState)

                # update if the board is full
                fullGame = gameplay.IsFullGame(gameplay.currentState)

            if (winner == 'X'):
                result[0] += 1
            elif (winner == '-'):
                result[1] += 1
            elif (winner == 'O'):
                result[2] += 1
        print("X wins:", result[0]/10.0, '%, O wins', result[2]/10.0,'%, Draw is ',result[1]/10.0, '%')

    def TrainAndTestTicTacToe4X4GameBot (self, trainingIteration, testingPartition):

        for i in range(trainingIteration):

            if ((i+1)%testingPartition == 0):
                print("Round",(i+1),end=' ')
                self.TestTicTacToe4X4GameBotPerformance()

            # hit = 0, stick = 1
            nextState = None

            # if player wins dealer, reward = 1
            # if player draws dealer, reward = 0
            # if player loses dealer, reward = -1
            # used to update the V function
            winner = '-'
            fullGame = False

            # start a game
            gameplay = TicTacToe4X4GamePlay()

            # game proceeds only if (1) no one has won yet (2) the board is not full
            while (winner == '-' and fullGame == False):

                # get all possible next states
                possibleNextStates = gameplay.PossibleNextStates(gameplay.currentState)
                # get the corresponding value table dictionary for possible next states
                valueTablePossibleNextStateDict = self.strategy.ValueTablePossibleNextStateDict (possibleNextStates, self.valueTableDict)

                # find next state defined by the policy map
                # in training phase, use epsilon greedy policy
                # player 'X' wants to achieve the highest value
                if (gameplay.currentPlayer == 'X'):
                    nextState = self.strategy.EpsilonGreedyPolicyFromValueTableDict(valueTablePossibleNextStateDict, 'Max', self.epsilon)
                # player 'O' wants to achieve the lowest value
                elif (gameplay.currentPlayer == 'O'):
                    nextState = self.strategy.EpsilonGreedyPolicyFromValueTableDict(valueTablePossibleNextStateDict, 'Min', self.epsilon)

                # proceed the game to the next state
                gameplay.currentState = nextState

                # swap player's turn
                gameplay.currentPlayer = 'O' if gameplay.currentPlayer == 'X' else 'X'

                # update which player has won the game
                winner = gameplay.FindOutTheWinner(gameplay.currentState)

                # update if the board is full
                fullGame = gameplay.IsFullGame(gameplay.currentState)

                # get the reward given winner
                reward = gameplay.RewardOfGame(winner)

                # initialize the next state best value
                nextStateBestValue = 0.0

                if (winner == '-' and fullGame == False):
                    # get all possible next states
                    possibleNextStates = gameplay.PossibleNextStates(gameplay.currentState)

                    # get the corresponding value table dictionary for possible next states
                    valueTablePossibleNextStateDict = self.strategy.ValueTablePossibleNextStateDict(possibleNextStates, self.valueTableDict)

                    # get the best value for next state if next player is 'X'
                    if (gameplay.currentPlayer == 'X'):
                        nextStateBestValue = self.strategy.BestValueFromValueTableDict(valueTablePossibleNextStateDict, 'Max')
                    # get the best value for next state if next player is 'O'
                    elif (gameplay.currentPlayer == 'O'):
                        nextStateBestValue = self.strategy.BestValueFromValueTableDict(valueTablePossibleNextStateDict, 'Min')

                # update value table dictionary
                currentStateValue = self.valueTableDict[gameplay.currentState]
                nextStateValue = reward + nextStateBestValue
                self.valueTableDict[gameplay.currentState] = currentStateValue + self.alpha * (nextStateValue - currentStateValue)


    def TestTicTacToe4X4GameBotPerformance(self):

        # 'X', '-', 'O'
        result = [0,0,0]
        for i in range (1000):
            # start a game
            nextState = None

            # if player wins dealer, reward = 1
            # if player draws dealer, reward = 0
            # if player loses dealer, reward = -1
            # used to update the V function

            winner = '-'
            fullGame = False

            gameplay = TicTacToe4X4GamePlay()

            # game proceeds only if (1) no one has won yet (2) the board is not full
            while (winner == '-' and fullGame == False):

                # get all possible next states
                possibleNextStates = gameplay.PossibleNextStates(gameplay.currentState)

                # get the corresponding value table dictionary for possible next states
                valueTablePossibleNextStateDict = self.strategy.ValueTablePossibleNextStateDict(possibleNextStates, self.valueTableDict)

                # find next state defined by the policy map
                # in training phase, use epsilon greedy policy
                # player 'X' wants to achieve the highest value
                if (gameplay.currentPlayer == 'X'):
                    nextState = self.strategy.BestPolicyFromValueTableDict(valueTablePossibleNextStateDict, 'Max')
                # player 'O' wants to achieve the lowest value
                elif (gameplay.currentPlayer == 'O'):
                    nextState = self.strategy.BestPolicyFromValueTableDict(valueTablePossibleNextStateDict, 'Min')

                gameplay.currentState = nextState

                # swap player's turn
                gameplay.currentPlayer = 'O' if gameplay.currentPlayer == 'X' else 'X'

                # update which player has won the game
                winner = gameplay.FindOutTheWinner(gameplay.currentState)

                # update if the board is full
                fullGame = gameplay.IsFullGame(gameplay.currentState)

            if (winner == 'X'):
                result[0] += 1
            elif (winner == '-'):
                result[1] += 1
            elif (winner == 'O'):
                result[2] += 1
        print("X wins:", result[0]/10.0, '%, O wins', result[2]/10.0,'%, Draw is ',result[1]/10.0, '%')