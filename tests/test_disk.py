import pytest
from disk import Disk

class TestDisk():
    def test_body_one(self):
        assert Disk.body(1) == [0, 0, 1, 0, 0]

    def test_body_two(self):
        assert Disk.body(2) == [0, 0, 1, 1, 0]

    def test_body_three(self):
        assert Disk.body(3) == [0, 1, 1, 1, 0]

    def test_body_four(self):
        assert Disk.body(4) == [0, 1, 1, 1, 1]

    def test_body_five(self):
        assert Disk.body(5) == [1, 1, 1, 1, 1]
