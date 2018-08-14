import unittest
import subprocess
from echo import parse_args, make_upper_case, make_lower_case, make_title_case


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
        parser = parse_args(["-u", "taco"])
        parser2 = parse_args(["--upper", "taco"])
        self.assertTrue(parser.upper)
        self.assertTrue(parser2.upper)
        self.assertEquals(make_upper_case("hello"), "HELLO")
        # self.assertEquals("hello", "HELLO")

    def test_lower(self):
        parser = parse_args(["-l", "taco"])
        parser2 = parse_args(["--lower", "taco"])
        self.assertTrue(parser.lower)
        self.assertTrue(parser2.lower)
        self.assertEquals(make_lower_case("Hello"), "hello")
        # self.assertEquals("Hello", "hello")

    def test_title(self):
        parser = parse_args(["-t", "taco"])
        parser2 = parse_args(["--title", "taco"])
        self.assertTrue(parser.title)
        self.assertTrue(parser2.title)
        self.assertEquals(make_title_case("hello"), "Hello")
        # self.assertEquals("hello", "Hello")

    def test_all_opts(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-tul", "heLLo!"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.strip("\n")
        self.assertEquals(stdout, "Hello!")
        process = subprocess.Popen(
            ["python", "./echo.py", "-ul", "heLLo!"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.strip("\n")
        self.assertEquals(stdout.strip("\n"), "hello!")

    def test_no_opt(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "taco"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.strip("\n")
        self.assertEquals(stdout, "taco")


if __name__ == "__main__":
    unittest.main()
