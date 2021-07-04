from typing import List
import random


class Sorter:
    SMALL_SORT = 8
    MED_SORT = 15
    LARGE_SORT = 25
    def __init__(self) -> None:
        pass




    def generate_array(self, upto:int ) -> List[int]:
        nums = [i+1 for i in range(upto)]

        random.shuffle(nums)

        return nums

    def process_sorting_choice(self) -> None:

        to_sort = self.generate_array(Sorter.MED_SORT)

        # First merge sort function will be out of place
        # Must define the array as an attribute that can be accessed from the class and modified


        # This way the array can be printed inside the merge sort function, which makes the process much clearer

        self.mergeSort(to_sort)
    def mergeSort(self, arr:List[int], level:int=1) -> List[int]:

        mid = len(arr)//2

        leftArr = arr[:mid]
        rightArr = arr[mid:]

        print(f"Sorting main array at level {level}", arr)

        print(f"Sorting left array at level {level}", leftArr)
        if len(leftArr) > 2:
            leftArr = self.mergeSort(leftArr, level+1)
        else:
            if len(leftArr)==2:
                if leftArr[0] > leftArr[1]:
                    leftArr = leftArr[::-1]
        print(f"Left array sorted at level {level}", leftArr)

        print(f"Sorting right array at level {level}", rightArr)
        if len(rightArr) > 2:
            rightArr = self.mergeSort(rightArr, level+1)
        else:
            if len(rightArr)==2:
                if rightArr[0] > rightArr[1]:
                    rightArr = rightArr[::-1]

        print(f"Right array sorted at level {level}", rightArr)


        # Knowing that the two lists are sorted, we can run through the two arrays using separate pointers

        merged = []
        while leftArr and rightArr:
            if leftArr[0] <= rightArr[0]:
                merged.append(leftArr.pop(0))
            else:
                merged.append(rightArr.pop(0))

        merged.extend(leftArr)
        merged.extend(rightArr)

        print(f"Merged array at level {level}", merged)
        return merged
