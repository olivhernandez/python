import unittest
from television import Television

class TestTelevision(unittest.TestCase):
    def test_init(self):
        television = Television()
        self.assertFalse(television.get_status())
        self.assertFalse(television.get_muted())
        self.assertEqual(television.get_volume(), television.MIN_VOLUME)
        self.assertEqual(television.get_channel(), 0)


    def test_power(self):
        television = Television()
        self.assertFalse(television.get_status())
        television.power()
        self.assertTrue(television.get_status())
        television.power()
        self.assertFalse(television.get_status())


    def test_mute(self):
        television = Television()
        television.power()
        television.volume_up()

        self.assertTrue(television.get_status())
        self.assertEqual(television.get_volume(), 1)

        television.mute()
        self.assertTrue(television.get_status())

        television.mute()
        self.assertFalse(television.get_muted())
        self.assertEqual(television.get_volume(), 1)

        television.power()
        television.mute()

        self.assertFalse(television.get_muted())
        self.assertFalse(television.get_status())


    def test_channel_up(self):
        television = Television()

        television.channel_up()
        self.assertFalse(television.get_status())
        self.assertEqual(television.get_channel(), 0)

        television.power()
        television.channel_up()
        self.assertTrue(television.get_status())
        self.assertEqual(television.get_channel(), 1)

        television.channel_up()
        television.channel_up()
        television.channel_up()
        self.assertEqual(television.get_channel(), 0)

    def test_channel_down(self):
        television = Television()
        television.channel_down()
        self.assertFalse(television.get_status())
        self.assertEqual(television.get_channel(), 0)

        television.power()
        television.channel_down()
        self.assertTrue(television.get_status())
        self.assertEqual(television.get_channel(), 3)

        television.channel_down()
        self.assertEqual(television.get_channel(), 2)

    def test_volume_up(self):
        television = Television()
        television.volume_up()
        self.assertEqual(television.get_volume(), 0)

        television.power()
        television.volume_up()
        self.assertTrue(television.get_status())
        self.assertEqual(television.get_volume(), 1)

        television.mute()
        television.volume_up()
        self.assertFalse(television.get_muted())
        self.assertEqual(television.get_volume(), 2)

        television.volume_up()
        self.assertEqual(television.get_volume(), 2)

    def test_volume_down(self):
        television = Television()
        television.volume_down()
        self.assertFalse(television.get_status())
        self.assertEqual(television.get_volume(), 0)

        television.power()
        television.volume_up()
        television.volume_up()
        television.volume_down()
        self.assertTrue(television.get_status())
        self.assertEqual(television.get_volume(), 1)

        television.mute()
        television.volume_down()
        self.assertFalse(television.get_muted())
        self.assertEqual(television.get_volume(), 0)

        television.volume_down()
        self.assertEqual(television.get_volume(), 0)

if __name__ == '__main__':
    unittest.main()