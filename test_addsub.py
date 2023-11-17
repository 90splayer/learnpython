import addsub
import pytest

def test_add():
    assert addsub.add(4, 5) == 9

def test_sub():  
    assert addsub.sub(4, 5) == -1

