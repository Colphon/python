import unittest
from television import *

class MyTestCase(unittest.TestCase):

    def test_init(self):
        test1 = Television('m', 8, "3", True)

        self.assertEqual(test1.__str__(self),'Power = m, Channel = True, Volume = 3')

    def test_power(self):
        test2 = Television()
        test2.power()
        self.assertEqual(test1.__str__(self), 'Power = True, Channel = 0, Volume = 0')
        test2.power()
        self.assertEqual(test1.__str__(self), 'Power = False, Channel = 0, Volume = 0')
    def test_mute(self):
        test3 = Television()
        test3.power()
        test3.volume_up()
        test3.mute()
        self.assertEqual(test3.__str__(self), 'Power = True, Channel = 0, Volume = 0')
        test3.mute()
        self.assertEqual(test3.__str__(self), 'Power = True, Channel = 0, Volume = 1')
        test3.power()
        test3.mute()
        self.assertEqual(test1.__str__(self), 'Power = False, Channel = 0, Volume = 1')
        test3.mute()
        self.assertEqual(test1.__str__(self), 'Power = False, Channel = 0, Volume = 1')


    def test_channel_up(self):
        with self.assertRaises(ValueError):
            triangle('s', 'y')
            triangle('s', 5)
            triangle(4, 'y')
            triangle(4, '*')
            triangle('^', 's')

        with self.assertRaises(TypeError):
            triangle(-1, -2)
            triangle(-1, 2)
            triangle(1, -2)
            triangle(0, 0)
            triangle(0, 1)
            triangle(3, 0)
            triangle(0, -2)
            triangle(-1, 0)

        self.assertAlmostEqual(triangle(2, 3), 3.0, delta=0.001)
        self.assertAlmostEqual(triangle(3.4, 2.1), 3.57, delta=0.001)
        self.assertAlmostEqual(triangle(3.4, 2), 3.4, delta=0.001)
        self.assertAlmostEqual(triangle(2, 3.4), 3.4, delta=0.001)
    def test_channel_down(self):
        pass
    def test_volume_up(self):
        pass
    def test_volume_down(self):
        pass


if __name__ == '__main__':
    unittest.main()