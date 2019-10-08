#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


# Your test case class goes here
class testing_testing(unittest.TestCase):

    # def setUp(self):
    #     self.parser = echo.create_parser()

    def test_help(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertAlmostEquals(len(stdout), len(usage))
        self.assertEquals(stdout, usage)

    def test_upper(self):
        args = ["-u", "hello"]
        # namespace = self.parser.parse_args(args)
        # namespace.upper()
        # self.assertTrue(echo.main(args))
        self.assertEquals(echo.main(args), "HELLO")

    def test_lower(self):
        args = ['-l', 'HELLO']
        # self.assertTrue(echo.islower('hello'))
        self.assertEquals(echo.main(args), 'hello')

    def test_title(self):
        args = ['-t', 'hello world']
        self.assertEqual(echo.main(args), 'Hello World')

    def test_all_args(self):
        args = ['-ult', 'hello']
        self.assertEquals(echo.main(args), "Hello")


if __name__ == '__main__':
    unittest.main()
