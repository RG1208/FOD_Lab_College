import numpy as np

#(a)
array = np.random.randint(1, 51, size=(4, 5))
print("Original Array:\n", array)

#(b)
total_sum = np.sum(array)
print("\nSum of all elements:", total_sum)

#(c)
max_value = np.max(array)
print("\nMaximum value:", max_value)

#(d)
mean_value = np.mean(array)
print("\nMean of all elements:", mean_value)

#(e)
row_sums = np.sum(array, axis=1)
print("\nSum of each row:", row_sums)

#(f)
transposed_array = np.transpose(array)
print("\nTransposed Array:\n", transposed_array)

#(g)
bool_mask = array > 25
filtered_elements = array[bool_mask]
print("\nBoolean mask (elements > 25):\n", bool_mask)
print("Elements greater than 25:", filtered_elements)
