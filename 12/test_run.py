import module_12_4 as mt
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            run1 = mt.Runner('Test1', -2)
            for i in range(10):
                run1.walk()
            self.assertEqual(run1.distance, 50)
            mt.logging.info('"est_walk" выполнен успешно')
        except:
            mt.logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            run2 = mt.Runner(3, 4)
            for i in range(10):
                run2.run()
            self.assertEqual(run2.distance, 100)
            mt.logging.info('"test_run" выполнен успешно')
        except:
            mt.logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        run1 = mt.Runner('Test1')
        run2 = mt.Runner('Test2')
        for i in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance, run2.distance)
