# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# Collections are used to store multiple items in a single variable
# Lists are ordered collections of items
# Lists are mutable meaning you can change their content
#lists are created using square brackets []
list_of_fruits = ["apple", "banana", "cherry", "dates"]
print(list_of_fruits) #[apple, banana, cherry, dates]
print(type(list_of_fruits)) # <class 'list'>
print(list_of_fruits[0]) #apple
print(list_of_fruits[1]) #banana
print(list_of_fruits[-1]) #dates
print(list_of_fruits[1:3]) #[banana, cherry]
#reversing a list
list_of_fruits.reverse()
print(list_of_fruits)
print(list_of_fruits[::-1])

# Appending items to a list
list_of_fruits.append("elderberry") # add items to the end of the list
print(list_of_fruits)

list_of_fruits.append("pear")
list_of_fruits.append("strawberry")
print(list_of_fruits)

list_of_fruits.extend(["fig","grape","mango"])
print(list_of_fruits)
list_of_fruits.reverse()
print(list_of_fruits)

#popping items from a list

popped_item= list_of_fruits.pop()
print(popped_item)
print(list_of_fruits)

list_of_fruits.insert(1, "blueberry")
print(list_of_fruits)

list_of_fruits.remove("banana")
print(list_of_fruits)

list_of_fruits.insert(3, "watermelon")
print(list_of_fruits)

list_of_fruits.sort()
print(list_of_fruits)

list_of_items= list(range(1,1001))
print(list_of_items)

print(len(list_of_items))
popped_number = list_of_items.pop
print(list_of_items)

list_of_items.extend(range(1001, 2001))
print(list_of_items)
# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.