from utils.Actions import *
import unittest


class Tester(unittest.TestCase):
    def testGetStats(self):
        acts = Actions()
        str = '{"action":"jump", "time":100}'
        acts.addAction(str)
        print("TestCase 1\n\n")
        self.assertEqual(acts.getStats(), '[ {"action": "jump", "avg": 100.0} ]')

    def testGetStatsMultiple(self):
        acts2 = Actions()
        str = '{"action":"jump", "time":100}'
        acts2.addAction(str)
        str = '{"action":"run", "time":75}'
        acts2.addAction(str)
        str = '{"action":"jump", "time":200}'
        acts2.addAction(str)
        print("TestCase 2\n\n")
        self.assertEqual(acts2.getStats(), '[ {"action": "jump", "avg": 150.0}, {"action": "run", "avg": 75.0} ]')

    def testBaddAddAction(self):
        acts3 = Actions()
        str = '{"name":"Thomas", "age":175}'
        acts3.addAction(str)
        print("TestCase 3\n\n")
        self.assertRaises(KeyError)


if __name__ == '__main__':
    # ## Testcases for valid inputs
    # acts = Actions()
    # str = '{"action":"jump", "time":100}'
    # acts.addAction(str)
    # result = acts.getStats()
    # print(result)
    # print('1st add action complete\n\n')
    #
    # acts2 = Actions()
    # str = '{"action":"jump", "time":100}'
    # acts2.addAction(str)
    # result = acts2.getStats()
    # print(result)
    # print('11st add action complete\n\n')
    #
    # str = '{"action":"run", "time":75}'
    # acts.addAction(str)
    # result = acts.getStats()
    # print(result)
    # print('2nd add action complete\n\n')
    #
    # str = '{"action":"jump", "time":200}'
    # acts.addAction(str)
    # result = acts.getStats()
    # print(result)
    # print('3rd add action complete\n\n')
    #
    # ## Testcases for invalid inputs
    # str = '{"name":"Thomas", "age":175}'
    # acts.addAction(str)
    # print("Invalid input 1\n")
    #
    # str = '{"action":"run"}'
    # acts.addAction(str)
    # print("Invalid input 2\n")
    #
    # str = '{"time":55}'
    # acts.addAction(str)
    # print("Invalid input 3\n")

    ## Running Unit Tests
    unittest.main()
