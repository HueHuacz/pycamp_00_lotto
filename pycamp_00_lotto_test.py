""" Skrypt do testowania """

from pycamp_00_lotto import make_user_list, make_user_set, one_draw
from io import StringIO
import pytest


def test_make_user_list(monkeypatch):
    test_value1 = '1 2 3 4 5 6'
    test_value2 = 'wiosna lato jesien zima'
    test_value3 = '12 34 zima'

    for i in {test_value1, test_value2, test_value3}:
        monkeypatch.setattr('sys.stdin', StringIO(i))
        assert make_user_list() == list(i.split())


def test_make_user_set():
    test_list = ['1', '2', '3', '4', '5', '6']
    test_list_int = [int(i) for i in test_list]

    assert make_user_set(test_list) == set(test_list_int)


def test_make_user_set_v2():
    test_value = ['1', '2', '3', '4', '5', 'zima']
    test_value_v2 = ['1', '2', '3', '4', '5', '6', '7']
    test_value_v3 = ['1', '2', '3', '4', '5', '51']

    for i in [test_value, test_value_v2, test_value_v3]:
        with pytest.raises(SystemExit) as e:
            make_user_set(i)
        assert e.type == SystemExit


def test_one_draw():
    for _ in range(101):
        drawn_numbers = one_draw()
        assert len(drawn_numbers) == 6
        assert min(drawn_numbers) >= 1
        assert max(drawn_numbers) <= 49

# TODO:


def test_play_until_win():
    pass
