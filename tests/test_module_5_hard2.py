import unittest

from Chapter_5.module_5_hard import Video


class TestVideo(unittest.TestCase):

    def setUp(self):
        self.video = Video(title="Awesome Video", duration=120)

    def test_initialization(self):
        self.assertEqual(self.video.title, "Awesome Video")
        self.assertEqual(self.video.duration, 120)
        self.assertEqual(self.video.adult_mode, False)
        self.assertEqual(self.video.time_now, 0)

    def test_editing(self):
        self.video.title = "Edited Video"
        self.video.duration = 300
        self.video.adult_mode = True
        self.video.time_now = 30
        self.assertEqual(self.video.title, "Edited Video")
        self.assertEqual(self.video.duration, 300)
        self.assertEqual(self.video.adult_mode, True)
        self.assertEqual(self.video.time_now, 30)


if __name__ == "__main__":
    unittest.main()
