

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    if len(elements)== 1:
        return
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = end
    pivot = elements[pivot_index]
    p_index = start

    for i in range(start, end):
        if  elements[i] <= pivot:
            swap(i,p_index, elements)
            p_index += 1
    swap(p_index, end, elements)
    return p_index

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)