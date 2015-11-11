__author__ = 'Jabari Dash'


def reset_array(arr):
    return [5, 1, 4, 3, 2]

def insertion_sort(arr):
    print("This is a test")
    print("This is a 2nd test")

def print_mom(arr):
    print("Hi mom! its me")

def bubble_sort(arr):
    swapped = True
    i = 0
    count = 0
    swaps = 0

    print("\nBubble Sort:")

    while i < len(arr) - 1 and swapped is True:
        swapped = False

        for j in range(len(arr) - i - 1):

            count += 1
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
                swaps += 1
    print(arr)
    print("Comparisons: ", count)
    print("Swaps: ", swaps)


def insertion_sort(arr):
    i = 1
    j = 0
    count = 0
    swaps = 0

    print("\nInsertion Sort:")

    while i <= len(arr) - 1:
        j = i
        count += 1

        while j > 0 and arr[j] < arr[j-1]:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1
            swaps += 1

        i += 1
    print(arr)
    print("Comparisons: ", count)
    print("Swaps: ", swaps)


def selection_sort(arr):
    print("\nSelection Sort:")

    i = 0
    count = 0
    swaps = 0

    while i < len(arr)-1:
        min_num = i
        j = i+1

        count += 1
        while j < len(arr):

            if arr[j] < arr[min_num]:
                min_num = j

            j += 1

        count += 1
        if min_num != i:
            temp = arr[i]
            arr[i] = arr[min_num]
            arr[min_num] = temp
            swaps += 1
        i += 1
    print(arr)
    print("Comparisons: ", count)
    print("Swaps: ", swaps)


num_list = [5, 1, 4, 3, 2]

print("Unsorted:")
print(num_list)

bubble_sort(num_list)

num_list = reset_array(num_list)
insertion_sort(num_list)

num_list = reset_array(num_list)
selection_sort(num_list)
