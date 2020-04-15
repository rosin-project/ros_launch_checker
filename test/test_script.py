import os
import unittest

from ros_launch_checker.__main__ import find_launch_dependencies


class TestScript(unittest.TestCase):
    def setUp(self):
        pass

    @staticmethod
    def get_test_folder(test_folder):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(this_dir, os.curdir, test_folder)

    def test_minimum_failing(self):
        errors = find_launch_dependencies(self.get_test_folder("test_minimum_fail"))
        self.assertNotEqual(errors, [])

    def test_minimum_success(self):
        errors = find_launch_dependencies(self.get_test_folder("test_minimum_success"))
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
