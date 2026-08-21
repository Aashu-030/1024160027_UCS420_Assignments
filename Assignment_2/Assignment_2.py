#ASSIGNMENT 2 - Q1
roll_no = "1024160027"
# i.
L = [int(digit) * 10 for digit in roll_no]
print(L)
#Original List ---> [10, 0, 20, 40, 10, 60, 0, 0, 20, 70]
#ii.
L.append(66)
print(L)
#Changed List ---> [10, 0, 20, 40, 10, 60, 0, 0, 20, 70, 66]
#Using append we can add something to end of List, hence 66 is added to the end
L.insert(1, 44)
print(L)
#Changed List ---> [10, 44, 0, 20, 40, 10, 60, 0, 0, 20, 70, 66]
#Insert adds something at a specific index in the list, like 44 is added at index 1
#iii.
L.remove(44)
print(L)
#Changed List ---> [10, 0, 20, 40, 10, 60, 0, 0, 20, 70, 66]
L.pop()
print(L)
#Changed List ---> [10, 0, 20, 40, 10, 60, 0, 0, 20, 70]
#iv.
L.sort()
print(L)
#Changed List ---> [0, 0, 0, 10, 10, 20, 20, 40, 60, 70]
L.sort(reverse = True)
print(L)
#Changed List ---> [70, 60, 40, 20, 20, 10, 10, 0, 0, 0]
#v.
#Here using the sorted list only in reverse manner
print("First three elements")
print(L[0:3])      #[70, 60, 40]
print("Last three elements")
print(L[-3:])       #[0, 0, 0]
#vi.
average = sum(L)/ len(L)
new_list = []
print(average)     #23.0
for s in L:
  if (s > average):
    new_list.append(s)
print(new_list)    #[70, 60, 40]


#Assignment 2- Q2
#Using list from Q1.py --> the final changed list
L = [70, 60, 40, 20, 20, 10, 10, 0, 0, 0]
scores = tuple(L[:8])   #(70, 60, 40, 20, 20, 10, 10, 0)
print(scores)
#i. 
highest = max(scores)        #70
highest_index = scores.index(highest)       #at index 0 
lowest = min(scores)       # 0 
lowest_index = scores.count(lowest)     #1
print("Highest Score: ", highest, "Index: ", highest_index)
print("Lowest Score: ", lowest, "Count: ", lowest_index)
#ii. 
reversed_scores = list(reversed(scores))
print(reversed_scores)     #[0, 10, 10, 20, 20, 40, 60, 70]
#iii.
user_score = int(input("Enter your score: "))
if user_score in scores: 
    print("First occurence: ", scores.index(user_score))
else : 
    print("Score not found in the tuple")
#iv. 
#scores[0] = 100
#we got a TypeError :  'tuple' object does not support item assignment 
#As tuple is immutable and list are mutable, so we can't change the value of an element after tuple creation. 
#v. 
first_score, second_score, *remaining_scores = scores
print("First Score: ", first_score)       #70
print("Second Score: ", second_score)      #60 
print("Remaining Scores: ", remaining_scores)       #[40, 20, 20, 10, 10, 0]


#Assignment 2 - Q3
import random 
random.seed(1024160027)
#i. 
numbers = [random.randint(100,900) for _ in range(100)]
print(numbers)
#[498, 623, 819, 119, 812, 730, 862, 521, 492, 147, 792, 711, 745, 179, 662, 855, 755, 886, 873, 200, 316, 570, 134, 350, 578, 488, 277, 792, 761, 707, 410, 689, 511, 472, 157, 130, 686, 534, 446, 198, 625, 323, 478, 895, 290, 686, 484, 485, 177, 541, 875, 542, 155, 499, 200, 722, 716, 128, 338, 875, 633, 556, 510, 206, 854, 424, 320, 577, 272, 260, 404, 200, 386, 344, 831, 433, 107, 330, 434, 154, 761, 468, 206, 435, 745, 416, 741, 244, 550, 560, 813, 342, 364, 549, 790, 543, 328, 220, 286, 404]

#ii. 
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)
print("Count of odd numbers: ", len(odd_numbers))
#Count of odd numbers:  39

#iii.
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
print("Count of even numbers: ", len(even_numbers))
#Count of even numbers:  61

#iv. 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
prime_numbers = [num for num in numbers if is_prime(num)]
print(prime_numbers)
#[521, 179, 277, 761, 157, 541, 499, 577, 433, 107, 761]
print("Count of prime numbers: ", len(prime_numbers))
#Count of prime numbers:  11

#v. 
frequency = {} 
for num in numbers: 
    frequency[num] = frequency.get(num, 0) + 1
most_frequent = max(frequency, key=frequency.get)
most_frequent_count = frequency[most_frequent]
print("Most frequent number: ", most_frequent, "Count: ", most_frequent_count)
#Most frequent number:  200 Count:  3


#Assignment 2 - Q4

L = [1,0,2,4,1,6,0,0,2,7]
A = {digit*7 for digit in L}
B = {digit*9 for digit in L}
print("Set A: ", A)        #{0, 7, 42, 14, 49, 28}
print("Set B: ", B)        #{0, 36, 9, 18, 54, 63}

#i. 
union = A.union(B)
print("Union of A and B: ", union)
#{0, 36, 7, 9, 42, 14, 49, 18, 54, 28, 63}

#ii. 
intersection = A.intersection(B)
print("Intersection of A and B: ", intersection)
#{0}

#iii.
A_minus_B = A.difference(B)
B_minus_A = B.difference(A)
print("A - B: ", A_minus_B)     #{7, 42, 14, 49, 28}
print("B - A: ", B_minus_A)     #{36, 9, 18, 54, 63}

#symmetric difference () gives all values that are in either set but not in both 
#While difference () gives all values only in one set and not the other

#iv. 
symmetric_diff = A.symmetric_difference(B)
print("Symmetric difference of A and B: ", symmetric_diff)
#{7, 9, 14, 18, 28, 36, 42, 49, 54, 63}

#v. 
print("Is A a subset of B? ", A.issubset(B))       #False
print("Is B a superset of A", B.issuperset(A))     #False

#vi. 
X = int(input("Enter a number to remove from set A: "))
A.discard(X)  
print("Set A after removing", X, ": ", A)

#discard() is safer because it doesn't raise a KeyError when value is not found in the set


#Assignment 2 - Q5
my_dict = {
    "name": "Aarush Sareen",
    "roll_no": "1024160027",
    "branch" : "Computer Science and Engineering",
    "age": 20,
    "city": "Bhopal"
}
print("Original dictionary")
print(my_dict)

# i.
my_dict["location"] = my_dict.pop("city")
print(my_dict)

#ii.
my_dict["cgpa"] = 7.5
print(my_dict)

#iii.
my_dict["age"] += 1
print(my_dict)

#iv.
#Pop returns the value of that key deleted and then deletes it
dict_pop = my_dict.copy()
removed_branch = dict_pop.pop("branch")
print(dict_pop)
print(removed_branch)

#Delete just removes the key-value pair
dict_del = my_dict.copy()
del dict_del["branch"]
print(dict_del)

#v.
for key, value in my_dict.items():
  print(f"{key}--> {value}")

#vi.
if("email" in my_dict) :
  print("Email : " , my_dict["email"])
else :
  print("Email doesn't exist in dictionary")

#vii.
friend_dict = {
    "name": "Amit Vikram Mangal",
    "roll_no": "1024160038",
    "branch": "Computer Science and Engineering",
    "age": 20 ,
    "city": "Pathankot"
}
print(friend_dict)
#When values are common the values from friend_dict win over the ones in my_dict
#As friend_dict is written later in merged_dict
merged_dict = {**my_dict, **friend_dict}
print("Merged dictionary is: ", merged_dict)

#viii.
#Here isinstance check if v is str or not , and if it is str then only add in string_dict
string_dict = {k : v for k , v in my_dict.items() if isinstance(v, str)}
print(string_dict)
