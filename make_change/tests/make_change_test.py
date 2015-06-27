import sys, os
sys.path.insert(0, os.getcwd())
from make_change import give_change, init_change

def test_give_change():
    coins = [25, 10, 5, 1]
    dollars = [100, 50, 20, 10, 5, 1]

    cents = 93
    change_1 = give_change(cents, coins)

    assert change_1 == {25: 3, 10:1, 5: 1, 1: 3}

    bucks = 135
    change_2 = give_change(bucks, dollars)
    assert change_2 == {100: 1, 50: 0 , 20: 1, 10: 1, 5: 1, 1: 0 }



