import pytest

from pole import *
from disk import Disk

class TestPole:
    class TestStacking:
        def test_stack_empty(self):
            p = Pole(0)
            d = Disk(3)

            p.push(d)

            assert p[-1] == d
            assert len(p) == 1

        def test_stack_with_members(self):
            p = Pole(0)

            for i in [4, 3, 2]:
                p.push(Disk(i))

            d = Disk(1)
            p.push(d)

            assert len(p) == 4
            assert p[-1] == d

        def test_pop(self):
            p = Pole(0)

            for i in [4, 3, 2]:
                p.push(Disk(i))

            d = Disk(1)
            p.push(d)

            assert p.pop() == d
            assert len(p) == 3

    class TestRules:
        def test_empty(self):
            p = Pole(0)
            d = Disk(5)

            p.push(d)

            assert len(p) == 1

        def test_smaller_on_bigger(self):
            p = Pole(0)
            d = Disk(5)
            e = Disk(4)

            p.push(d)
            p.push(e)

            assert len(p) == 2

        def test_bigger_on_smaller(self):
            p = Pole(0)

            d = Disk(5)
            e = Disk(4)

            with pytest.raises(StackingError):
                p.push(e)
                p.push(d)
