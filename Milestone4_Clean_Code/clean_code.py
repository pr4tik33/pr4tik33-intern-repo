# Function to find common elements between two lists
def find_common_elements(list1, list2):
    common_elements = []
    
    # Check if each element in list1 is also in list2
    for element in list1:
        if element in list2:
            common_elements.append(element)
    
    return common_elements

# Lists to compare
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]


result = find_common_elements(list1, list2)
print(result)

# Improvements:
# Descriptive Function and Variable Name.
# Comments where it is necessary. 