"""
UCS420: Cognitive Computing
Assignment-5 - NumPy-Introduction-1

Name       : Aarush Sareen
Roll Number: 1024160027
"""

import numpy as np

YOUR_NAME = "Aarush_Sareen"
ROLL_NUMBER = "1024160027"

print(f"Name: Aarush Sareen | Roll Number: {ROLL_NUMBER}\n")

print("="*70)
print("Q1. Basic 1D Array Operations")
print("="*70)

arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)

# a. Addition of 2 to all elements
add_2 = arr + 2
print("\n(a) Array + 2:", add_2)

# b. Multiply 3 with all elements
mul_3 = arr * 3
print("\n(b) Array * 3:", mul_3)

# c. Divide every element by 2
div_2 = arr / 2
print("\n(c) Array / 2:", div_2)


print("="*70)
print("Q2. Reverse Array & Most Frequent Value")
print("="*70)

# a. Reverse array
arr2 = np.array([1, 2, 3, 6, 4, 5])
reversed_arr = arr2[::-1]
print("(a) Original array:", arr2)
print("    Reversed array :", reversed_arr)

# b. Most frequent value(s) and their indices
def most_frequent(a):
    values, counts = np.unique(a, return_counts=True)
    max_count = counts.max()
    modes = values[counts == max_count]
    # find all indices in 'a' where value equals any of the modes
    indices = {int(m): np.where(a == m)[0] for m in modes}
    return modes, indices

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

modes_x, indices_x = most_frequent(x)
print("\n(b-i) x =", x)
print("      Most frequent value(s):", modes_x)
print("      Indices of most frequent value(s):", indices_x)

modes_y, indices_y = most_frequent(y)
print("\n(b-ii) y =", y)
print("       Most frequent value(s):", modes_y)
print("       Indices of most frequent value(s):", indices_y)


print("="*70)
print("Q3. 2D Array Indexing")
print("="*70)

arr3 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("2D array:\n", arr3)

# a. 1st row, 2nd column
val_a = arr3[0, 1]
print("\n(a) 1st row, 2nd column element:", val_a)

# b. 3rd row, 1st column
val_b = arr3[2, 0]
print("\n(b) 3rd row, 1st column element:", val_b)


print("="*70)
print("Q4. 1D Array with linspace()")
print("="*70)

# Array named <<Your Name>> with 25 evenly spaced numbers from 10 to 100
globals()[YOUR_NAME] = np.linspace(10, 100, 25)
my_array = globals()[YOUR_NAME]
print(f"Array '{YOUR_NAME}' (25 evenly spaced numbers from 10 to 100):")
print(my_array)

print("\nDimensions (ndim):", my_array.ndim)
print("Shape:", my_array.shape)
print("Total elements (size):", my_array.size)
print("Data type (dtype):", my_array.dtype)
print("Total bytes consumed (nbytes):", my_array.nbytes)

# Transpose using reshape()
transposed_reshape = my_array.reshape(25, 1)
print("\nTranspose using reshape((25,1)) - shape:", transposed_reshape.shape)

# Can we do the same with .T attribute?
transposed_T = my_array.T
print("\nUsing .T attribute - shape:", transposed_T.shape)
print("""
Explanation: For a 1-D array, the .T attribute has NO effect - it returns
the same 1-D array unchanged (shape stays (25,)), because a true transpose
only makes sense when there are at least 2 dimensions (rows and columns)
to swap. reshape((25,1)) DOES work here because it explicitly converts the
1-D array into a 2-D column vector of shape (25,1). So reshape() can achieve
what looks like a "transpose" for a 1-D array, but the .T attribute alone
cannot, unless the array is first reshaped into 2-D.
""")


print("="*70)
print(f"Q5. 2D Array - ucs420_{YOUR_NAME}")
print("="*70)

values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 20, 35]
globals()[f"ucs420_{YOUR_NAME}"] = np.array(values).reshape(3, 4)
ucs420_arr = globals()[f"ucs420_{YOUR_NAME}"]
print(f"ucs420_{YOUR_NAME} (3 rows x 4 columns):\n", ucs420_arr)

print("\nMean  :", ucs420_arr.mean())
print("Median:", np.median(ucs420_arr))
print("Max   :", ucs420_arr.max())
print("Min   :", ucs420_arr.min())
print("Unique elements:", np.unique(ucs420_arr))

# Reshape to 4 rows x 3 columns
globals()[f"reshaped_ucs420_{YOUR_NAME}"] = ucs420_arr.reshape(4, 3)
reshaped_arr = globals()[f"reshaped_ucs420_{YOUR_NAME}"]
print(f"\nreshaped_ucs420_{YOUR_NAME} (4 rows x 3 columns):\n", reshaped_arr)

# Resize to 2 rows x 3 columns (this drops elements since 2*3=6 < 12)
globals()[f"resized_ucs420_{YOUR_NAME}"] = np.resize(ucs420_arr, (2, 3))
resized_arr = globals()[f"resized_ucs420_{YOUR_NAME}"]
print(f"\nresized_ucs420_{YOUR_NAME} (2 rows x 3 columns) using np.resize():\n", resized_arr)
print("""
Note: np.resize((2,3)) on a 12-element array only keeps the first 6 elements
(it truncates rather than raising an error) because the target shape (2x3=6)
has fewer total elements than the original (3x4=12).
""")
