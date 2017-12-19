import unittest
import os

from sak.commands.toggle import _get_name, toggle


class ToggleTest(unittest.TestCase):

    def test_get_name(self):

        self.assertEqual("first", _get_name(".first"))
        self.assertEqual(".first", _get_name("first"))

    def test_rename(self):
        self._create_file("gradle-project")
        toggle("gradle-project")

        self.assertEqual(True, os.path.exists(".gradle-project"))
        self.assertEqual(False, os.path.exists("gradle-project"))

    def test_rename_hidden(self):
        self._create_file(".gradle-project")
        toggle(".gradle-project")

        self.assertEqual(True, os.path.exists("gradle-project"))
        self.assertEqual(False, os.path.exists(".gradle-project"))

    def test_existing_file(self):
        self._create_file("gradle-project")
        self._create_file(".gradle-project")
        toggle("gradle-project")

        self.assertEqual(True, os.path.exists("gradle-project"))
        self.assertEqual(True, os.path.exists(".gradle-project"))

    def test_non_existing_file(self):
        toggle("gradle-project")

        self.assertEqual(False, os.path.exists("gradle-project"))
        self.assertEqual(False, os.path.exists(".gradle-project"))

    def tearDown(self):
        self._del_file("gradle-project")
        self._del_file(".gradle-project")

    @staticmethod
    def _del_file(name):
        try:
            os.unlink(name)
        except OSError:
            pass

    @staticmethod
    def _create_file(name):
        with open(name, "w+") as fp:
            fp.write("content")