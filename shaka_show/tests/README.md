# Testing

We are using unittest for unit testing and mocking.

## Running tests

To run your test, type the following:
```
python test_<testname>.py
```

To run all tests from inside folder, type:
```
python -m unittest discover
```

## Making a test

1. Name your test:
```
test_<class or function name>.py
```
2. Make a class named "TestYourClassName"
3. For each test, define a function that starts with test\_.
4. Asserts can be found at [the unittest site](https://docs.python.org/3/library/unittest.html#classes-and-functions)

