import unittest

from grappa import should

from app import index


class AppTest(unittest.TestCase):
    def test_index(self):
        index() | should.be.equal.to({"hi": "there"})
