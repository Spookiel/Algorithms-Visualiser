from abc import ABC,abstractmethod
import random
from termcolor import colored # Allows coloured text in terminal
from typing import List, Tuple
import time

class Sort(ABC):
    SMALL_SORT = 8
    MED_SORT = 15
    LARGE_SORT = 25
    EXTREME_SORT = 100
    SORT_SIZES = [SMALL_SORT,MED_SORT,LARGE_SORT, EXTREME_SORT]
    NUM_SIZES = 5

    SLOW_ANIM = 1
    MED_ANIM = 0.2
    FAST_ANIM = 0.05
    INSTA_ANIM = 0
    ANIM_SPEEDS = [SLOW_ANIM, MED_ANIM, FAST_ANIM, INSTA_ANIM]

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
    def process_sort(self, size: int = 1, delay: int = 2) -> None:
        raise NotImplementedError

    @abstractmethod
    def output_steps(self):
        raise NotImplementedError

class MergeSort(Sort):


    def __init__(self):

        super().__init__()

    def process_sort(self, size: int = 1, delay: int = 2) -> None:


        self._steps: List[Tuple[str, List[int]]] = []     # Resets after each sort
        self._totalComparisons: int = 0

        to_sort: List[int] = Sort.generate_array(Sort.SORT_SIZES[size])

        self.sort_array(to_sort)
        self.output_steps(delay)
        print(f"[Sorted array with {self._totalComparisons} comparisons!]")


    def sort_array(self, arr:List[int], level:int=1) -> List[int]:

        mid = len(arr)//2

        left_arr = arr[:mid]
        right_arr = arr[mid:]


        step_descrip : str = f"{colored('sorting', 'yellow')} main array at level {level}"
        arr_store: List[int] = arr[:] # [:] to copy the array to prevent mutable type issues

        self._steps.append((step_descrip, arr_store))



        step_descrip: str = f"{colored('sorting', 'red')} left array at level {level}"
        arr_store: List[int] = left_arr[:]

        self._steps.append((step_descrip, arr_store))


        if len(left_arr) > 2:
            left_arr = self.sort_array(left_arr, level+1)

        else:

            if len(left_arr) == 2:
                self._totalComparisons += 1

                if left_arr[0] > left_arr[1]:
                    left_arr = left_arr[::-1]

        step_descrip: str = f"Left array {colored('sorted', 'green')} at level {level}"
        arr_store: List[int] = left_arr[:]

        self._steps.append((step_descrip, arr_store))


        step_descrip: str = f"{colored('sorting', 'red')} right array at level {level}"
        arr_store: List[int] = right_arr[:]

        self._steps.append((step_descrip, arr_store))

        if len(right_arr) > 2:
            right_arr = self.sort_array(right_arr, level+1)
        else:
            if len(right_arr)==2:
                self._totalComparisons += 1
                if right_arr[0] > right_arr[1]:
                    right_arr = right_arr[::-1]

        step_descrip: str = f"Right array {colored('sorted', 'green')} at level {level}"
        arr_store: List[int] = right_arr[:]

        self._steps.append((step_descrip, arr_store))



        # Knowing that the two lists are sorted, we can run through the two arrays using separate pointers

        merged = []
        while left_arr and right_arr:
            if left_arr[0] <= right_arr[0]:
                merged.append(left_arr.pop(0))
            else:
                merged.append(right_arr.pop(0))
            self._totalComparisons += 1

        merged.extend(left_arr)
        merged.extend(right_arr)

        step_descrip: str = f"{colored('Merged', 'green')} array at level {level}"
        arr_store: List[int] = merged[:]

        self._steps.append((step_descrip, arr_store))

        # print(f"{colored('Merged', 'green')} array at level {level}", merged)
        return merged


    def output_steps(self, delay: int = 2) -> None:

        for descrip, arr in self._steps:
            
            time.sleep(Sort.ANIM_SPEEDS[delay])
            print(descrip, arr)

class BubbleSort(Sort):


    def __init__(self):
        super().__init__()

        self._steps: List[str] = []
        self._iterations = 0


    def process_sort(self, size=1, speed=1) -> None:
        self._iterations = 0

        to_sort = Sort.generate_array(Sort.SORT_SIZES[size])

        self.sort_array(to_sort)

        self.output_steps(speed)





    def getColoredArray(self, arr: List[int], curPointer: int=-1) -> str:

        if curPointer != -1:
            arr[curPointer] = colored(arr[curPointer], "yellow")
            arr[curPointer+1] = colored(arr[curPointer+1], "yellow")

        for i in range(-self._iterations, 0, 1):
            arr[i] = colored(arr[i], "green")

        return " ".join(list(map(str, arr)))

    def sort_array(self, arr: List[int]) -> None:

        swapped = True

        while swapped:
            swapped = False
            for ind in range(len(arr)-self._iterations-1):
                
                last_swapped = False

                self._totalComparisons += 1
                if arr[ind] > arr[ind+1]:
                    
                    arr[ind], arr[ind+1] = arr[ind+1], arr[ind]
                    swapped = True
                    last_swapped = True

                col_str: str = self.getColoredArray(arr[:], ind)
                
                if last_swapped:
                    step = f"[{arr[ind+1]} is greater than {arr[ind]} - moving {arr[ind+1]} up]"+"   "+col_str
                    
                else:
                    step = f"[{arr[ind]} is less than {arr[ind+1]}, No swap]"+"   "+col_str

                self._steps.append(step)
            self._iterations += 1


        # Add final step where the whole array is green
        self._iterations = len(arr)
        col_str: str = self.getColoredArray(arr[:])
        step = f"[Sorted with {self._totalComparisons} comparisons!]"+"   "+col_str
        self._steps.append(step)

    def output_steps(self, delay: int = 2) -> None:
        # Delay is fast speed by default


        for step in self._steps:
            time.sleep(Sort.ANIM_SPEEDS[delay])
            print(step)




class RadixSort(Sort):
    def __init__(self):
        super().__init__()

    def process_sort(self, size: int = 1, speed: int = 1):
        raise NotImplementedError

    def sort_array(self, arr: List[int]):
        raise NotImplementedError

    def output_steps(self):
        raise NotImplementedError

class QuickSort(Sort):
    def __init__(self):
        super().__init__()

    def process_sort(self, size:int = 1, speed: int = 1) -> None:
        self._iterations = 0

        to_sort = Sort.generate_array(Sort.SORT_SIZES[size])

        self.sort_array(to_sort)

        self.output_steps(speed)

    def sort_array(self, arr: List[int]):

        self._quick_sort(arr, 0, len(arr)-1)

    def _quick_sort(self, arr: List[int], lo: int, hi: int, level:int = 1):

        if lo < hi:
            print(arr, arr[lo:hi + 1], lo, hi, "Sorting at level", level)
            part = self._partition(arr, lo, hi)
            print("Partition is", part)

            self._quick_sort(arr, lo, part-1, level+1)
            self._quick_sort(arr, part+1, hi, level+1)
            print(arr, lo, hi, "Finished sorting at level", level)


    def _partition(self, arr: List[int], lo: int, hi: int) -> int:

        piv: int = arr[hi]

        ind: int = int(lo)

        for j in range(ind, hi):
            if arr[j] < piv:
                arr[ind], arr[j] = arr[j], arr[ind]
                ind += 1

        arr[ind], arr[hi] = arr[hi], arr[ind]
        return ind



    def output_steps(self, delay: int = 2):
        raise NotImplementedError

class CountingSort(Sort):
    def __init__(self):
        super().__init__()

    def process_sort(self, size:int = 1, speed: int = 1) -> List[Tuple[str, List[int]]]:
        raise NotImplementedError

    def sort_array(self, arr: List[int]):
        raise NotImplementedError

    def output_steps(self):
        raise NotImplementedError

