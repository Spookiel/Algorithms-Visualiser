from abc import ABC,abstractmethod
import random
from termcolor import colored # Allows coloured text in terminal
from typing import List, Tuple


class Sort(ABC):
    SMALL_SORT = 8
    MED_SORT = 15
    LARGE_SORT = 25
    EXTREME_SORT = 100
    SORT_SIZES = [SMALL_SORT,MED_SORT,LARGE_SORT, EXTREME_SORT]
    NUM_SIZES = 5

    def __init__(self):

        self._steps: List[Tuple[str, List[int]]] = []
        self._totalComparisons = 0


    @staticmethod
    def generate_array(upto: int) -> List[int]:
        nums = [i+1 for i in range(upto)]

        random.shuffle(nums)

        return nums

    @abstractmethod
    def sort_array(self, arr: List[int]):
        raise NotImplementedError

    @abstractmethod
    def process_sort(self):
        raise NotImplementedError



class MergeSort(Sort):


    def __init__(self):

        super().__init__()


    def process_sort(self, size=1) -> List[Tuple[str, List[int]]]:
        #Only handles the generation of the _steps array, output will be handled by Sorter class

        self._steps: List[Tuple[str, List[int]]] = []     # Resets after each sort
        self._totalComparisons: int = 0

        to_sort: List[int] = Sort.generate_array(size)

        self.sort_array(to_sort)

        return self._steps


    def sort_array(self, arr:List[int], level:int=1) -> List[int]:

        mid = len(arr)//2

        leftArr = arr[:mid]
        rightArr = arr[mid:]


        step_descrip : str = f"{colored('sorting', 'yellow')} main array at level {level}"
        arr_store: List[int] = arr[:] # [:] to copy the array to prevent mutable type issues

        self._steps.append((step_descrip, arr_store))

        #print(f"{colored('sorting', 'yellow')} main array at level {level}", arr)


        step_descrip: str = f"{colored('sorting', 'red')} left array at level {level}"
        arr_store: List[int] = leftArr[:]

        self._steps.append((step_descrip, arr_store))



        if len(leftArr) > 2:
            leftArr = self.sort_array(leftArr, level+1)
        else:
            if len(leftArr)==2:
                self._totalComparisons += 1
                if leftArr[0] > leftArr[1]:
                    leftArr = leftArr[::-1]

        step_descrip: str = f"Left array {colored('sorted', 'green')} at level {level}"
        arr_store: List[int] = leftArr[:]

        self._steps.append((step_descrip, arr_store))


        step_descrip: str = f"{colored('sorting', 'red')} right array at level {level}"
        arr_store: List[int] = rightArr[:]

        self._steps.append((step_descrip, arr_store))

        if len(rightArr) > 2:
            rightArr = self.sort_array(rightArr, level+1)
        else:
            if len(rightArr)==2:
                self._totalComparisons += 1
                if rightArr[0] > rightArr[1]:
                    rightArr = rightArr[::-1]

        step_descrip: str = f"Right array {colored('sorted', 'green')} at level {level}"
        arr_store: List[int] = rightArr[:]

        self._steps.append((step_descrip, arr_store))

        #print(f"Right array {colored('sorted', 'green')} at level {level}", rightArr)


        # Knowing that the two lists are sorted, we can run through the two arrays using separate pointers

        merged = []
        while leftArr and rightArr:
            if leftArr[0] <= rightArr[0]:
                merged.append(leftArr.pop(0))
            else:
                merged.append(rightArr.pop(0))
            self._totalComparisons += 1

        merged.extend(leftArr)
        merged.extend(rightArr)

        step_descrip: str = f"{colored('Merged', 'green')} array at level {level}"
        arr_store: List[int] = merged[:]

        self._steps.append((step_descrip, arr_store))

        # print(f"{colored('Merged', 'green')} array at level {level}", merged)
        return merged

