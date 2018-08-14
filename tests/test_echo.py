import unittest
import subprocess


class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        pass

    def test_lower(self):
        pass

    def test_title(self):
        pass


if __name__ == "__main__":
    unittest.main()
