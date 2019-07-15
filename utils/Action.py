# This is the data structure that keeps track of average time and names for specific actions
class Action:
    def __init__(self, action, time):
        self.action = action
        self.time = time
        self.totalTime = time
        self.numActions = 1

    def getAction(self):
        return self.action

    def getTime(self):
        return self.time

    def getAvgTime(self):
        return self.totalTime / self.numActions

    def updateAction (self, time):
        self.numActions = self.numActions + 1
        self.totalTime = self.totalTime + time
