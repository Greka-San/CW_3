from src.hide_the_account_or_card import hide_the_account_or_card, hides_card_number, hides_account_number


def test_hide_the_account_or_card():
    assert hide_the_account_or_card("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert hide_the_account_or_card("Счет 68319824767376585478") == "Счет **5478"


def test_hides_card_number():
    assert hides_card_number("7000792289606361") == "7000 79** **** 6361"


def test_hides_account_number():
    assert hides_account_number("73654108430135874305") == "**4305"
