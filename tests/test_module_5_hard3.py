import time
import unittest

from Chapter_5.module_5_hard import UrTube, User, Video


class TestUrTube(unittest.TestCase):

    def setUp(self):
        self.urtube = UrTube()

    def test_registration(self):
        self.urtube.register("test_user", "test_password", 20)
        self.assertEqual(len(self.urtube.users), 1)
        self.assertEqual(self.urtube.current_user.nickname, "test_user")
        self.assertEqual(self.urtube.current_user.age, 20)

    def test_log_in_with_valid_credential(self):
        self.urtube.register("test_user", "test_password", 20)
        self.urtube.log_out()
        self.urtube.log_in("test_user", "test_password")
        self.assertEqual(self.urtube.current_user.nickname, "test_user")

    # def test_log_in_with_invalid_credential(self):
    #     output = self.urtube.log_in("test_user", "test_password")
    #     self.assertIsNone(self.urtube.current_user)
    #     self.assertEqual(output, "Invalid nickname or password")

    def test_log_out(self):
        self.urtube.register("test_user", "test_password", 20)
        self.urtube.log_out()
        self.assertIsNone(self.urtube.current_user)

    def test_add_video(self):
        video = Video('test_video', 20, False)
        self.urtube.add(video)
        self.assertEqual(len(self.urtube.videos), 1)

    def test_get_videos(self):
        video = Video('test_video', 20, False)
        self.urtube.add(video)
        videos = self.urtube.get_videos("video")
        expected_videos = ['test_video']
        self.assertListEqual(videos, expected_videos)

    # def test_watch_video_without_login(self):
    #     video = Video('test_video', 20, False)
    #     self.urtube.add(video)
    #     output = self.urtube.watch_video('test_video')
    #     self.assertEqual(output, 'Please log in to watch videos')

    def test_watch_video_with_login(self):
        video = Video('test_video', 20, False)
        self.urtube.register("test_user", "test_password", 20)
        self.urtube.add(video)
        self.urtube.watch_video('test_video')
        self.assertEqual(video.time_now, 0)


if __name__ == '__main__':
    unittest.main()
