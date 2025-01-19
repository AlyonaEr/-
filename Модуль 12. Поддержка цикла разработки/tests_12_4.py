from rt_with_exceptions import Runner
import unittest
import logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner_1 = Runner(self)
            logging.info(f'"test_walk" выполнен успешно')
            for i in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner_2 = Runner(self)
            logging.info(f'"test_run" выполнен успешно')
            for i in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        runner_3 = Runner(self)
        runner_4 = Runner(self)
        for i in range(10):
            runner_3.walk()
            runner_4.run()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")
