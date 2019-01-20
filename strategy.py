import random

class Strategy:

    def ValueTablePossibleNextStateDict (self, possibleNextStates, valueTableDict):
        return dict((state, valueTableDict[state]) for state in possibleNextStates)

    def EpsilonGreedyPolicyFromValueTableDict(self, valueTableSubDict, maxMinValue, epsilon):
        # P = epsilon: exploration, return random next state
        if random.random() < epsilon:
            return random.choice(list(valueTableSubDict.keys()))
        # P = 1-epsilon: exploitation
        else:
            # player X turn, return highest value next state
            if (maxMinValue == 'Max'):
                maxValue = max(valueTableSubDict.values())
                return random.choice([state for state, value in valueTableSubDict.items() if value == maxValue])
            # player O turn, return lowest value next state
            elif (maxMinValue == 'Min'):
                minValue = min(valueTableSubDict.values())
                return random.choice([state for state, value in valueTableSubDict.items() if value == minValue])

    def BestPolicyFromValueTableDict(self, valueTableSubDict, maxMinValue):
        # player X turn, return highest value next state
        if (maxMinValue == 'Max'):
            maxValue = max(valueTableSubDict.values())
            return random.choice([state for state, value in valueTableSubDict.items() if value == maxValue])
        # player O turn, return lowest value next state
        elif (maxMinValue == 'Min'):
            minValue = min(valueTableSubDict.values())
            return random.choice([state for state, value in valueTableSubDict.items() if value == minValue])

    def BestValueFromValueTableDict(self, valueTableSubDict, maxMinValue):
        # player X turn, return highest value next state
        if (maxMinValue == 'Max'):
            return max(valueTableSubDict.values())
        # player O turn, return lowest value next state
        elif (maxMinValue == 'Min'):
            return min(valueTableSubDict.values())