"""
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
"""

"""
This program shows how the Gradient Descent algorithm works.

Reference: https://en.wikipedia.org/wiki/Gradient_descent

The target function f(x) = x ^ 4 - 3 * x ^ 3 + 2

Find the x that gives the 'local' miminal of f(x)

The derivative of f(x) is f'(x) = 4 * x ^ 3 - 9 * x ^ 2

"""

def f_derivative(x):
    return 4 * x ** 3 - 9 * x ** 2


def gradient_descent():
    """
       iteratively move towards the reverse direction of gradient(derivative)
        which reaches the local minimal at the fastest pace.
    """
    x_old = 0
    x_new = 6     # the algorithm starts at 6
    # the step size moving towards the minimal
    # The choice of gemma is critical to the algorithm,
    #  a wrong gemma could not converge the function.
    # A overly small gemma would take longer time to converge.
    gemma = 0.01

    precision = 0.00001
    iteration = 0

    while abs(x_new - x_old) > precision:
        iteration += 1
        x_old = x_new
        x_new = x_old - gemma * f_derivative(x_old)

    print("Local minimal occurs at {} after {} iterations with gemma {}".format(
          x_new, iteration, gemma))


if __name__ == "__main__":
     print("Calculate the minimal of f(x) = x^4 - 3*x^3 + 2, "
           "through gradient descent algorithm")
     gradient_descent()


