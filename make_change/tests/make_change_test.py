import sys, os
sys.path.insert(0, os.getcwd())
from make_change import give_change, init_change
from change_helpers import generateExpectedDollarsCents

coins   = [25, 10, 5, 1]
dollars = [100, 50, 20, 10, 5, 1]

def test_give_change():
    cents = 93
    change_1 = give_change(cents, coins)
    assert change_1 == {25: 3, 10:1, 5: 1, 1: 3}

    bucks = 135
    change_2 = give_change(bucks, dollars)
    assert change_2 == {100: 1, 50: 0 , 20: 1, 10: 1, 5: 1, 1: 0 }


def test_init_change():
    assert init_change(coins)   == {25: 0, 10:0, 5: 0, 1: 0}
    assert init_change(dollars) == {100: 0, 50:0, 20: 0, 10:0, 5: 0, 1: 0}




def test_compute_change_for_dollars():
    bucks = 10.42

    expected_dollars = {10: 1}
    expected_cents   = {10: 4, 1: 1}

    assert compute_change_for_dollars(10) == generateExpectedDollarsCents(expected_dollars, expected_cents)


