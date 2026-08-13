(venv) rajkumar@Rajkumars-MacBook-Air 05_testing_using_pytest % pytest -v simple_div_test.py
================================================= test session starts ==================================================
platform darwin -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- /Users/rajkumar/DataEngineering/02_Python/PythonBasics/PythonAdvanced/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/rajkumar/DataEngineering/02_Python/PythonBasics/PythonAdvanced/05_testing_using_pytest
plugins: anyio-4.14.2
collected 3 items                                                                                                      

simple_div_test.py::test_multiply PASSED                                                                         [ 33%]
simple_div_test.py::test_multiply_3_num FAILED                                                                   [ 66%]
simple_div_test.py::test_division_2_num PASSED                                                                   [100%]

======================================================= FAILURES =======================================================
_________________________________________________ test_multiply_3_num __________________________________________________

    def test_multiply_3_num():
>       assert multiply_3_num(2,3,4) == 24
E       assert 162 == 24
E        +  where 162 = multiply_3_num(2, 3, 4)

simple_div_test.py:20: AssertionError
=============================================== short test summary info ================================================
FAILED simple_div_test.py::test_multiply_3_num - assert 162 == 24
============================================= 1 failed, 2 passed in 0.02s ==============================================
(venv) rajkumar@Rajkumars-MacBook-Air 05_testing_using_pytest % 
