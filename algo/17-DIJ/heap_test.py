
import pytest

import heap


def test1():
    h = heap.BinaryMinHeap()
    h.insert("a", 1)
    h.insert("b", 0)
    h.insert("c", 2)
    h["d"] = 3

    assert len(h) == 4
    assert 'a' in h
    assert 'z' not in h
    assert h['a'] == 1

    with pytest.raises(KeyError):
        h["z"]
    with pytest.raises(KeyError):
        h.insert("a", 11)
    with pytest.raises(KeyError):
        h.update("z", 11)

    assert h.find_min_key() == "b"

    h.update("b", 10)
    assert h.find_min_key() == "a"
    h.update("b", 0)
    assert h.find_min_key() == "b"
    h["b"] = 10
    assert h.find_min_key() == "a"
    h["b"] = 0
    assert h.find_min_key() == "b"

    h["z"] = -1
    assert h.find_min_key() == "z"
    del h['z']
    assert h.find_min_key() == "b"

    assert h.extract_min() == ("b", 0)
    assert h.find_min_key() == "a"
    assert h.extract_min() == ("a", 1)
    assert h.find_min_key() == "c"
    assert h.extract_min() == ("c", 2)
    assert h.find_min_key() == "d"
    assert h.extract_min() == ("d", 3)
    assert h.find_min_key() == None
    assert h.extract_min() == None
