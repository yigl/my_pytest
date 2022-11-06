# test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount

'''
 Utilizing fixtures helps us de-duplicate our code. If you notice a case where a piece of code 
 is used repeatedly in a number of tests, that might be a good candidate to use as a fixture.
 run pytest : python3 -m pytest test_wallet.py --fixtures
--fixtures will see all the available fixtures (docstring as the description)
'''

@pytest.fixture
def empty_wallet():
    ''' Returns a Wallet instance with a zero balance '''
    return Wallet()

@pytest.fixture
def wallet():
    # Returns a Wallet instance with a balance of 20
    return Wallet(20)

# use pytest fixture
def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

# use pytest fixture
def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

# use pytest fixture
def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)