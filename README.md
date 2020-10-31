# Sample mean 

Now that we know how to generate normal random variables this let's see if we can do all the usual operations that we have learned on this type of random variable.  As a case in point see if you can adjust the code in the box on the left so that a graph showing how the sample mean changes as you adjust the number of random variables it is computed from changes.

To complete this code you will need to:

1. Write a function called `normal` that takes in two parameters `mu` (the expectation of the random variable) and `sigma2` (the variance of the normal random variable).  This function should return a normal random variable with expectation `mu` and variance `sigma2`.
2. Set the first element of the list called `indices` equal to 1, the second element of the list called `indices` to 2 and so on.
3. Set the first element of the list called `average` equal to a sample mean calculated by generating 1 normal random variable with expectation `expectation` and variance `variance`, the second element of the list `average` equal to a sample mean calculated by generating 2 normal random variables with expectation `expectation` and variance `variance`, set the third element of the list called `average` equal to a sample mean calculated by generating 3 normal random variables with  expectation `expectation` and variance `variance` and so on until you have computed an average by generating 200 normal random variables with expectation `expectation` and variance `variance`.
