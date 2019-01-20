class TicTacToe3X3GamePlay:

    # initialize essential elements of a gameplay: current state, current player, etc
    def __init__(self):

        # current state stores how 'X's and 'O's are placed on the board
        self.currentState = self.GetInitializedState()

        # current player refers to which player ('X' or 'O') take the next move
        self.currentPlayer = 'X'

        self.winner = None

    # get initialized state
    def GetInitializedState (self):
        return '---------'

    # given current state, return a list of possible next states
    def PossibleNextStates (self, currentState):

        player = None
        XCount = currentState.count('X')
        OCount = currentState.count('O')

        if (XCount == OCount):
            player = 'X'
        else:
            player = 'O'

        # this list stores all possible next states
        possibleNextStates = []

        # locate all position with '-'
        for i in range(len(self.currentState)):
            if self.currentState [i] == '-':
                possibleNextStates.append (currentState[:i] + player + currentState[i+1:])

        return possibleNextStates

    def FindOutTheWinner (self, currentState):
        # 3 in a row, 3 in a column, 2 diagonals
        winningCombintation = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        # for each winning combination, check if the same player places their mark onto them
        for aCombination in winningCombintation:
            subState = [currentState[aCombination[i]] for i in range(3)]
            # if player 'X' wins
            if subState.count('X') == 3:
                return 'X'
            # if player 'O' wins
            elif subState.count('O') == 3:
                return 'O'
        # if no one wins
        return '-'

    def IsFullGame(self, currentState):
        if currentState.count('-') == 0:
            return True
        else:
            return False

    def RewardOfGame (self, winner):
        if winner == 'X':
            return 1.0
        elif winner == 'O':
            return -1.0
        else:
            return 0.0

class TicTacToe4X4GamePlay:

    # initialize essential elements of a gameplay: current state, current player, etc
    def __init__(self):

        # current state stores how 'X's and 'O's are placed on the board
        self.currentState = self.GetInitializedState()

        # current player refers to which player ('X' or 'O') take the next move
        self.currentPlayer = 'X'

        self.winner = None

    # get initialized state
    def GetInitializedState(self):
        return '----------------'

    # given current state, return a list of possible next states
    def PossibleNextStates (self, currentState):

        player = None
        XCount = currentState.count('X')
        OCount = currentState.count('O')

        if (XCount == OCount):
            player = 'X'
        else:
            player = 'O'

        # this list stores all possible next states
        possibleNextStates = []

        # locate all position with '-'
        for i in range(len(self.currentState)):
            if self.currentState [i] == '-':
                possibleNextStates.append (currentState[:i] + player + currentState[i+1:])

        return possibleNextStates

    def FindOutTheWinner (self, currentState):
        # 4 in a row, 4 in a column, 2 diagonals
        winningCombintation = [(0,1,2,3), (4,5,6,7), (8,9,10,11), (12,13,14,15), (0,4,8,12), (1,5,9,13), (2,6,10,14), (3,7,11,15), (0,5,10,15), (3,6,9,12), \
                               (0,1,4,5), (1,2,5,6), (2,3,6,7), (4,5,8,9), (5,6,9,10), (6,7,10,11), (8,9,12,13), (9,10,13,14), (10,11,14,15)]
        # for each winning combination, check if the same player places their mark onto them
        for aCombination in winningCombintation:
            subState = [currentState[aCombination[i]] for i in range(4)]
            # if player 'X' wins
            if subState.count('X') == 4:
                return 'X'
            # if player 'O' wins
            elif subState.count('O') == 4:
                return 'O'
        # if no one wins
        return '-'

    def IsFullGame(self, currentState):
        if currentState.count('-') == 0:
            return True
        else:
            return False

    def RewardOfGame (self, winner):
        if winner == 'X':
            return 1.0
        elif winner == 'O':
            return -1.0
        else:
            return 0.0