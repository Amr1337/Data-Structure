
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list)-1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) //2
        mid_number = numbers_list[mid_index]
        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index +1
        else:
            right_index = mid_index -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index)//2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index
    if mid_number <= number_to_find:
        left_index = mid_index +1
    else:
        right_index = mid_index -1
    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

def find_all_occur(numbers_list, number_to_find):
    index = binary_search(numbers_list, number_to_find)
    indices = [index]
    i = index-1
    while i >=0:
        if numbers_list[i] ==number_to_find:
            indices.append(i)
        else:
            break
        i = i -1
    i = index +1
    while i <len(numbers_list):
        if numbers_list[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i +1
    return sorted(indices)



if __name__ == "__main__":
    numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list)-1)
    print(f"The number's index {index} using")

    #index = linear_search(numbers_list, number_to_find)
    indices = find_all_occur(numbers_list, number_to_find)
    print(f"the indices are {indices}")
