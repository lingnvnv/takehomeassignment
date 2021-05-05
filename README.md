# Databased Take at home assignment

[![Build Status](https://travis-ci.com/lingnvnv/takehomeassignment.svg?branch=main)](https://travis-ci.com/github/lingnvnv/takehomeassignment/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/lingnvnv/takehomeassignment/blob/main/LICENSE)


## Overview
This is Databased take home problems for software engineer position. Every problems is developed by Test-driven development (TDD) and test files are included in the repository.

## Problem 1 - Least Factorial
### 1.1 Problem Description
Given an integer n, find the minimal k such that k=m! (where m! =1*2*... *m)for some integer m;k ≥ n. In other words, find the smallest factorial which is not less than n

### 1.2 Constraints
1 ≤ n ≤ 120

### 1.3 Test Cases
1. For n = 17, the output should be leastFactorial(n) = 24. 
2. For n = 5, the output should be leastFactorial(n) = 6.
3. For n = 106, the output should be leastFactorial(n) = 120.
4. For n = 0 or n = 121, the output should be Value Error

## Problem 2 - Recycling Lipstick
### 2.1 Problem Description
You own a lipstick business. When a lipstick container is empty, there is actually some leftover lipstick at the bottom that cannot be used because it is not accessible. Being an environmentally friendly business owner, you would like to recycle the leftover lipstick to make more. As a business, you know you need ‘numberOfLeftoversNeeded‘ to make a new lipstick. You have ‘numberOfLipsticks‘ in your possession. What’s the total number of lipsticks you can sell assuming that each of your customers return their leftovers?

For numberOfLipsticks = 5 and numberOfLeftoversNeeded = 2 the output should be getTotalNumberOfLipsticks(numberOfLipsticks, numberOfLeftovesNeeded) = 9

Here is how you get 9 lipsticks: Sell 5 lipsticks, get 5 leftovers; Create 2 more lipsticks using 4 leftovers (1 leftover remains); Sell 2 lipsticks, end up with 3 leftovers; Create 1 lipstick using 2 leftovers (1 leftover remains); Sell 1 lipstick, end up with 2 leftovers; Create 1 lipstick using 2 leftovers (no leftovers remain); Sell 1 lipstick

Thus you sell 5 + 2 + 1 + 1 = 9 lipsticks!

### 2.2 Test Cases
1. numberOfLipsticks = 5 numberOfLeftoversNeeded = 2 expected output =9
2. numberOfLipsticks = 15 numberOfLeftoversNeeded = 5 expected output = 18
3. numberOfLipsticks = 2 numberOfLeftoversNeeded = 3 expected output =2
4. numberOfLipsticks = 0.5 numberOfLeftoversNeeded = 2, the output should be Value Error


## Problem 3 - Students and Treats
### 3.1 Problem Description
A school teacher wants to hand out treats to his students. The teacher decides the best way to divide the treats is to have the students sit in a circle of sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the student in drawn chair, one treat will be handed to each student sequentially going around the circle until all treats have been distributed.
The teacher wants to have the students involved in sharing treats. He decides that whoever gets the very last treat, will be the student who makes the treats for the next game. Determine the chair number occupied by the student who will receive the last treat.
For example, there are 4 students and 6 treats. The students arrange them- selves in seats numbered 1 to 4. Let’s suppose 2 is drawn from the hat. Students receive treats at positions 2,3,4,1,2,3. The student who gets the last treat is in chair number 3.

### 3.2 Constraints
Notice the constraints for this problem. These are very large numbers, although it is highly unlikely there exists a class with that many students and treats, we still will be testing with large inputs.
1. 1≤n≤10^9 
2. 1≤m≤10^9 
3. 1≤s≤n

### 3.3 Test Cases
1. student_treats(5,2,1) = 2 
2. student_treats(5,2,2) = 3 
3. student_treats(7,19,2) = 6 
4. student_treats(3,7,3) = 3
5. student_treats(-1,-2,0.2), raise TypeError ("Input must be positive integer" )
6. student_treats(5, 3, 6), raise ValueError ( "hair number is out of range")

## Development setup

Our software is based in python 3.7.3 platform. Please make sure your python is above 3.5 because it contains some comments which require python new feature above 3.5. All the packages are stated in `requirements.txt`. Users can build their own virtual environment by using shell command:
```sh
pip install -r requirements.txt
```

## How to use
1. Choose "clone with https" in your repository to your local computer.
2. Open your `Git Bash` and input `git clone` adding with the URL.
3. Create virtual environment by command `python -m venv <venv name>`.
4. Install the required code environment in the `requitements.txt` with the following command: `pip install -r requirements.txt`.
5. Ensure the existence of the python files named `least_factorial.py`, `recycling_lipstick.py` and `student_treats.py`to run the core functions. 
6. The python files starting with `test_` are to test the corresponding functions in other python files. Run the command `pytest -v` in your bash window. It will automatically test all the test functions. If all pass, we are expected to see the following output.
```
================================================== test session starts ==================================================
platform darwin -- Python 3.7.3, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/lingzhong/Downloads/databased/takehomeassignment
plugins: pep8-1.0.6
collected 13 items                                                                                                      

test_least_factorial.py ....                                                                                      [ 30%]
test_recycling_lipstick.py ....                                                                                   [ 61%]
test_student_treats.py .....                                                                                      [100%]

================================================== 13 passed in 0.07s ===================================================
```
    * You can also change the testing arguments and expected results in the `test_xxx.py` and re-run the pytest command.
7. If you want to create the sphinx documentation, you should run following commands to generate HTML documentation. 
    ```
    cd docs
    sphinx-build -M html . _build
    ```
    * This will create `docs/_build/html` with the default webpage being `index.html`. Or the result of webpage that we ran is in the same path in the repository.





