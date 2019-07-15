import json
import logging
from utils.Action import *

class Actions:
    def __init__(self):
        self.actions = {} # Dictionary of Action objects, action name is key, Action Object is value
        self.results = {} # Dictionary of Action names string as key, avg as value
        self.resultsStr = '' # String to be returned in getStats

    # Function to receive a serialized JSON string of actions and their average times
    def getStats(self):
        self.__createResults()
        return self.resultsStr

    # Function to add a action istance (an action and it's time value) to exisitng data structure of actions
    def addAction(self, jsonStr):
        tempAction = json.loads(jsonStr) #Storing JSON in a python dictionary

        try:
            action = Action(tempAction['action'], tempAction['time'])
        except Exception as ex:
            logging.exception('Caught an error')
            print("Couldn't create Action object")
            print("Added JSON object must have two ONLY keys, 'action' and 'time'")
            return

        # Check if action exists in actions dictionary, if it does update avgTime and numActions, else add to the dictionary
        if(self.__doesExist(tempAction) == True):
            print("updating old action")
            self.actions[action.getAction()].updateAction(action.getTime()) # Updating the current object in the dictionary to have proper numActions and avgTime
        else:
            print("inserting new action")
            self.actions.update({action.getAction() : action})

    # Private Function that checks if the newly added action already exists in our dict of previously accepted actions
    def __doesExist(self, action):
        try:
            if action['action'] in self.actions:
                return True
            else:
                return False
        except Exception as ex:
            print("Error trying to determine existence of action")
            print(ex)

    # Private Function that creates a dict of 'action'(key) and 'avgTime'(key), key value pairs from the actions dict
    def __createResults(self):
        self.resultsStr = '[ ' # Resetting results string
        for k,v in self.actions.items():
            self.results.update({'action' : k})
            self.results.update({'avg' : v.getAvgTime()})
            jsonArr = json.dumps(self.results) # Dump dict to a jsonArr
            self.resultsStr += jsonArr + ", " # Appending each dictionary that gets created to string

        self.resultsStr = self.resultsStr[:-1] # removing whitespace from Storing
        self.resultsStr = self.resultsStr[:-1] # removing ',' from string
        self.resultsStr += ' ]' # closing bracket for JSON notation
