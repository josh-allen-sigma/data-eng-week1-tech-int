import pytest
from tech_interview import palindrome_identifier


def test_palindrome_identifier():
    assert palindrome_identifier('aha') == True


def test_palindrome_identifier_complex():
    assert palindrome_identifier('racecar') == True


def test_palindrome_identifier_failed():
    assert palindrome_identifier('abga') == False


def test_palindrome_identifier_failed_complex():
    assert palindrome_identifier('abgba') == True
