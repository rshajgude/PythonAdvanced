
#Criteria	                Default pattern
#---------------------------------------------
#File names	                test_*.py, *_test.py
#Function names	            test_*
#Class names	            Test* (no __init__)
#Method names inside test classes	test_*


def add(a, b):
    return a+b

def test_add_function():
    assert add(3,4) == 7
    assert add(5, 4) == 9

