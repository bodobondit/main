import unittest
import module_12_1 as RunTest
import module_12_2 as Tourtest

testSuit = unittest.TestSuite()
testSuit.addTest(unittest.TestLoader().loadTestsFromTestCase(RunTest.RunnerTest))
testSuit.addTest(unittest.TestLoader().loadTestsFromTestCase(Tourtest.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testSuit)
