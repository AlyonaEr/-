from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.keys():
            print(cls.all_results.get(i))

    def test_tournament_1(self):
        tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        res_1 = Tournament.start(tournament_1)
        self.all_results[1] = res_1
        self.assertTrue(list(res_1.values())[-1] == 'Ник')

    def test_tournament_2(self):
        tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        res_2 = Tournament.start(tournament_2)
        self.all_results[2] = res_2
        self.assertTrue(list(res_2.values())[-1] == 'Ник')

    def test_tournament_3(self):
        tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        res_3 = Tournament.start(tournament_3)
        self.all_results[3] = res_3
        self.assertTrue(list(res_3.values())[-1] == 'Ник')


if __name__ == "__main__":
    unittest.main()
