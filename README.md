**JumpCloud Take-home Interview Assignment**
---

**API to add actions to a data structure and keep track of average time to complete each action**

**Notes**
  - Written in python 3.6

**How to Use**
--
  - To create an '*Actions*' object simply call the constructor, no parameters needed.
    - `acts = Actions()`
  - '*Actions*' objects have 2 public functions, **addAction(jsonString)** and **getStats()**
    - **addAction** takes in a JSON string and adds an action and time to a running list of actions and average times. If the action already exists in the list then the time just added gets factored into the new average time.
        - The JSON string must be of the form `{"action":"name of action", "time":number}`
        - You can call **addAction** by doing the following.
        ```
        str = '{"action":"jump", "time":100}'
        acts.addAction(str)
        ```
    - **getStats** is used to return a serialized JSON array of the running list of all actions and their average times.
      - The following line of code: `str = acts.getStats()`. Will set 'str' to the string `{"action":"jump", "avg":100}` based off the action that was just added to the acts variable in the example above.
      - If we add another action to the list, **getStats** will return all actions:
        ```
        acts.addAction({"action":"run", "time":50})
        str = acts.getStats()
        print(str)
        ```
        output:
        ```
        [ {"action":"jump", "avg":100}, {"action":"run", "avg":50} ]
        ```
  - To use the library include `from utils.Action import *` at the top of your file.
  - main.py:
    - has a *Tester* class which uses the python unittest library to run some unit tests on the **getStats()** function.
    - has several examples of how to use both functions and prints out their results.
    - includes a couple examples where the user tries to input an invalid JSON string.
