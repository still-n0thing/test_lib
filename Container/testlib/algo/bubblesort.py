"""
https://en.wikipedia.org/wiki/Bubble_sort
Worst-case performance: O(N^2)
If you call bubble_sort(arr,True), you can see the process of the sort
Default is simulation = False
"""
from typing import List

def bubble_sort(arr : List , simulation : bool = False) -> None:
    """Sorts A List using bubble sort algorithm

    Parameters:
    arr(List) : Unsorted List 

    Returns:
    None : Function returns nothing

    """

    def swap(i : int, j : int) -> None:
        """Swaps two element of List 

        Parameters:
        i(int) : index of first element
        j(int) : index of second element

        Returns:
        None : Function returns nothing

        """
        arr[i], arr[j] = arr[j], arr[i]

    n : int = len(arr)
    swapped : bool = True
    
    iteration : int = 0
    if simulation:
        print("iteration",iteration,":",*arr)
    x : int = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                if simulation:
                    iteration = iteration + 1
                    print("iteration",iteration,":",*arr)
                    
    return arr
