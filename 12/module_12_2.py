import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.all_results = []

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        for res in self.all_results:
            print(res)

    def test_result1(self):
        tur = Tournament(90, self.runner1, self.runner3)
        all_results = tur.start()
        self.all_results.append(all_results)
        self.assertTrue(max(all_results), self.runner3)

    def test_result2(self):
        tur = Tournament(90, self.runner2, self.runner3)
        all_results = tur.start()
        self.all_results.append(all_results)
        self.assertTrue(max(all_results), self.runner2)

    def test_result3(self):
        tur = Tournament(90, self.runner3, self.runner2, self.runner1)
        all_results = tur.start()
        self.all_results.append(all_results)
        self.assertTrue(max(all_results), self.runner3)

    def test_finishers(self):
        tur = Tournament(90, self.runner1, self.runner3)
        finishers = tur.start()
        for f in finishers.values():
            self.assertIsInstance(f, str)

    def test_distance_speed(self):
        tur = Tournament(90, self.runner3, self.runner2, self.runner1)
        for p in tur.participants:
            self.assertGreaterEqual(tur.full_distance,p.speed)

if __name__ == '__main__':
    unittest.main()
