import pytest
from app_test.logic import is_eligible_for_load

def test_is_eligible_income():
    assert is_eligible_for_load(60000, 700, True) == True
    
def test_is_eligible_credit_score():
    assert is_eligible_for_load(60000, 650, True) == False
    
def test_is_eligible_employment():
    assert is_eligible_for_load(60000, 700, False) == False
    
def test_is_eligible_all_conditions():
    assert is_eligible_for_load(40000, 650, False) == False