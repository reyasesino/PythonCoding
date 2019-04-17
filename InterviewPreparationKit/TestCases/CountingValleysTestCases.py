import unittest
from InterviewPreparationKit.WarmUpChallenges import CountingValleys


class CountingValleysTest(unittest.TestCase):
    def test_main(self):
        counting = CountingValleys()
        self.assertRaises(Exception,counting.main(5,"UUUDDDDUUUU"))

if __name__ == '__main__':
    unittest.main()