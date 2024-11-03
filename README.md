Mutation Testing Demo
=====================

[![Build Status](https://travis-ci.org/johnnyleitrim/python-mutation-testing-demo.svg?branch=master)](https://travis-ci.org/johnnyleitrim/python-mutation-testing-demo)
[![Coverage Status](https://coveralls.io/repos/github/johnnyleitrim/python-mutation-testing-demo/badge.svg?branch=master)](https://coveralls.io/github/johnnyleitrim/python-mutation-testing-demo?branch=master)

A quick description of mutation testing and examples using [MutPy](https://github.com/mutpy/mutpy)

What is Mutation Testing?
=========================
Mutation testing can be used to evaluate the effectiveness of unit tests.

The idea is to mutate the source code by introducing faults and to check whether the existing unit tests are capable of detecting the faults (by failing).

Mutation testing frameworks generally work as follows:
* Your project is built and the unit tests are run to ensure your project is currently stable.
* It will then automatically apply a mutation operator (eg: remove a line of code, replace an addition with a subtraction, invert a boolean condition) on a single method of your code and re-run all unit tests to check if at least one of the test cases fails.
* If some tests fail, this means they were able to reveal the broken code.
* If no tests fail, this is a sign that there are gaps in your tests.
* It will repeat the mutation/testing process multiple times for different types of mutation operators.

Why do we need Mutation Testing?
================================
**Isn't code coverage/branch coverage enough? No.**

To demonstrate, do the following:
* Run `scripts/runCodeCoverage.sh` on the project.
* This will open the code coverage report (`htmlcov/index.html`).  All branch coverage is 100%.
* Open the `tests/test_simplenumber_ispositive.py` unit test.  You will see that it only has tests for positive and negative numbers, but there is no test for 0 (that test is currently commented out).
* This means that if the condition in `SimpleNumber.is_positive()` method is accidentially changed from `>=` to `>`, there is no test that would catch that.

Traditional test coverage (i.e line, statement, branch etc) measures only which code is executed by your tests. It does not check that your tests are actually able to detect faults in the executed code. **It is therefore only able to identify code that is definitely not tested**.

Examples
========
This project contains a few examples of unit tests that have 100% branch coverage.  However, running mutation testing on them will show that there are gaps in the tests.  Each unit test has commented out sections that are the "missing" tests to make the mutation tests pass.

