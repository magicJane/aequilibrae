from unittest import TestCase
import tempfile
import os
from aequilibrae.project import Project

temp_proj_name = os.path.join(tempfile.gettempdir(), "test_file.sqlite")


class TestProject(TestCase):
    def tearDown(self) -> None:
        if os.path.isfile(temp_proj_name):
            os.unlink(temp_proj_name)

    def test_creation(self):
        test_file = temp_proj_name
        self.assertRaises(FileNotFoundError, Project, test_file)

        p = Project(test_file, True)
        p.conn.close()
