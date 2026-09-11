"""
UCS420: Cognitive Computing
Assignment 6 - NumPy-II

Name       : Aarush Sareen
Roll Number: 1024160027
"""

import numpy as np

print(f"Name: Aarush Sareen | Roll Number: 1024160027\n")

print("="*70)
print("Q1. Sensor Readings")
print("="*70)

temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])
print("Original temperatures:", temperature)

# a. Add 2 degree C to every reading using vectorization
corrected = temperature + 2
print("\n(a) Corrected temperatures (+2°C):", corrected)

# b. Convert Celsius to Fahrenheit: F = 9/5 * C + 32
fahrenheit = (9/5) * temperature + 32
print("\n(b) Temperatures in Fahrenheit:", fahrenheit)

# c. Readings greater than 32 using Boolean indexing
above_32 = temperature[temperature > 32]
print("\n(c) Readings greater than 32°C:", above_32)

# d. Count how many readings exceed 32
count_above_32 = np.sum(temperature > 32)
print("\n(d) Count of readings exceeding 32°C:", count_above_32)

# e. Explanation (printed as a string)
explanation_q1e = """
(e) Vectorization applies an operation to an entire NumPy array at once using
    low-level, pre-compiled C loops instead of Python's interpreted for-loop.
    This removes the overhead of the Python interpreter (type checking,
    bytecode dispatch) on every single element, so operations run much faster
    and the code is shorter and more readable.

    Boolean indexing lets us filter data by creating a Boolean mask
    (temperature > 32) in one vectorized comparison, then use that mask to
    select elements directly, again avoiding an explicit loop with if-checks.
    Together, vectorization and Boolean indexing make NumPy operations both
    faster (C-level, SIMD-friendly execution) and more memory/CPU efficient
    than manually iterating through every value in pure Python.
"""
print(explanation_q1e)


print("="*70)
print("Q2. Daily Steps Matrix")
print("="*70)

steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])
print("Steps matrix:\n", steps)

# a. Total steps recorded
total_steps = steps.sum()
print("\n(a) Total steps recorded:", total_steps)

# b. Mean number of steps
mean_steps = steps.mean()
print("\n(b) Mean number of steps:", mean_steps)

# c. Max and min values
max_steps = steps.max()
min_steps = steps.min()
print("\n(c) Maximum steps:", max_steps, "| Minimum steps:", min_steps)

# d. Total steps for each day (axis=0 -> sum down the rows, per column/day)
total_per_day = steps.sum(axis=0)
print("\n(d) Total steps per day (axis=0):", total_per_day)

# e. Total steps for each user (axis=1 -> sum across columns, per row/user)
total_per_user = steps.sum(axis=1)
print("\n(e) Total steps per user (axis=1):", total_per_user)

# f. Position (user, day) of maximum steps using argmax()
flat_index = steps.argmax()
user_idx, day_idx = np.unravel_index(flat_index, steps.shape)
print(f"\n(f) Maximum steps position -> User {user_idx + 1}, Day {day_idx + 1} "
      f"(value = {steps[user_idx, day_idx]})")


print("="*70)
print("Q3. Array Slicing, Views, Copies and Reshaping")
print("="*70)

# a. Create original array
original = np.array([1, 2, 3, 4, 5, 6])
print("(a) original:", original)

# b. Slice from index 1 to 4 -> subset
subset = original[1:5]
print("\n(b) subset (original[1:5]):", subset)

# c. Modify first element of subset -> 999, show both
subset[0] = 999
print("\n(c) After subset[0] = 999")
print("    original:", original)
print("    subset  :", subset)
print("    -> subset is a VIEW of original, so changing subset also changes original.")

# reset original for the next part (fresh array as per question flow)
original = np.array([1, 2, 3, 4, 5, 6])

# d. Slice using .copy(), modify first element -> 500
subset_copy = original[1:5].copy()
subset_copy[0] = 500
print("\n(d) Using .copy(): subset_copy = original[1:5].copy(); subset_copy[0] = 500")
print("    original    :", original)
print("    subset_copy :", subset_copy)
print("    -> .copy() creates an independent array, so 'original' remains unchanged.")

# e. arange(1,13) reshaped into 3x4
matrix = np.arange(1, 13).reshape(3, 4)
print("\n(e) 3x4 matrix from np.arange(1,13).reshape(3,4):\n", matrix)

# f. Indexing/slicing
first_row = matrix[0]
last_row = matrix[-1]
second_col = matrix[:, 1]
sub_block = matrix[0:2, 1:3]  # rows 1-2 (index 0,1), columns 2-3 (index 1,2)
print("\n(f) First row       :", first_row)
print("    Last row        :", last_row)
print("    Second column   :", second_col)
print("    Rows 1-2, Cols 2-3:\n", sub_block)

# g. Flatten using flatten() and ravel()
flat_flatten = matrix.flatten()
flat_ravel = matrix.ravel()
print("\n(g) flatten():", flat_flatten)
print("    ravel()  :", flat_ravel)

# h. Modify element from ravel() result, observe original
flat_ravel[0] = -1
print("\n(h) After flat_ravel[0] = -1")
print("    ravel result:", flat_ravel)
print("    original matrix:\n", matrix)
print("    -> ravel() usually returns a VIEW (when possible), so the original "
      "matrix IS affected (matrix[0,0] became -1).")

# reset matrix since it was mutated above
matrix = np.arange(1, 13).reshape(3, 4)
flat_flatten = matrix.flatten()

# i. Modify element from flatten() result, observe original
flat_flatten[0] = -1
print("\n(i) After flat_flatten[0] = -1")
print("    flatten result:", flat_flatten)
print("    original matrix:\n", matrix)
print("    -> flatten() always returns a COPY, so the original matrix is "
      "NOT affected.")

# j. Shape, ndim, size, dtype of the 3x4 matrix
matrix = np.arange(1, 13).reshape(3, 4)
print("\n(j) shape:", matrix.shape, "| ndim:", matrix.ndim,
      "| size:", matrix.size, "| dtype:", matrix.dtype)


print("="*70)
print("Q4. Assistance Score Prediction (Linear Regression via OLS)")
print("="*70)

X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])
y = np.array([40, 65, 30, 85])

# a. Shape and dimensions of X
print("(a) X.shape:", X.shape, "| X.ndim:", X.ndim)

# b. Transpose
X_T = X.T
print("\n(b) X.T:\n", X_T)
print("    -> The transpose flips rows and columns: each ROW of X.T now "
      "represents one FEATURE (sleep, activity, stress) across ALL users, "
      "instead of one row per user. This is needed to compute feature-wise "
      "products like X.T @ X.")

# c. Matrix product X.T @ X
XtX = X_T @ X
print("\n(c) X.T @ X:\n", XtX)

# d. Matrix inverse (of X.T @ X, since X itself is not square)
XtX_inv = np.linalg.inv(XtX)
print("\n(d) inverse of (X.T @ X):\n", XtX_inv)

# e. OLS: beta = (X^T X)^-1 X^T y
beta = XtX_inv @ X_T @ y
print("\n(e) OLS coefficients (beta):", beta)

# f. Explanation of coefficients
explanation_q4f = """
(f) Each coefficient in 'beta' represents the estimated change in the
    predicted assistance score for a one-unit increase in that feature,
    holding the other two features constant:
      - beta[0] -> effect of Sleep hours on the assistance score
      - beta[1] -> effect of Activity level on the assistance score
      - beta[2] -> effect of Stress level on the assistance score
    A positive coefficient means the feature increases the assistance score
    as it increases; a negative coefficient means it decreases the score.
    (Note: since this model has no intercept term, the coefficients describe
    a purely proportional relationship through the origin.)
"""
print(explanation_q4f)

# g. Predict for a new user
new_user = np.array([5, 40, 7])
predicted_score = new_user @ beta
print(f"(g) Predicted assistance score for new_user {new_user}: {predicted_score:.4f}")
