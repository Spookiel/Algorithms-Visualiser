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


    def process_sort(self, size=1):
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


class BubbleSort(Sort):


    def __init__(self):
        super().__init__()

        self._steps: List[str] = []
        self._iterations = 0


    def process_sort(self, size=1) -> List[str]:
        self._iterations = 0

        to_sort = Sort.generate_array(size)

        self.sort_array(to_sort)



        return self._steps





    def getColoredArray(self, arr: List[int], curPointer: int) -> str:



        arr[curPointer] = colored(arr[curPointer], "yellow")
        arr[curPointer+1] = colored(arr[curPointer+1], "yellow")
        #print(-self._iterations)
        #print(-self._iterations)
        for i in range(-self._iterations, 0, 1):
            #print(i)
            arr[i] = colored(arr[i], "green")



        return " ".join(list(map(str, arr)))

    def sort_array(self, arr: List[int]):

        swapped = True

        while swapped:
            swapped = False
            for ind in range(len(arr)-self._iterations-1):
                lastSwapped = False


                if arr[ind] > arr[ind+1]:
                    arr[ind],arr[ind+1] = arr[ind+1], arr[ind]
                    swapped = True
                    lastSwapped = True


                col_str: str = self.getColoredArray(arr[:], ind)
                if lastSwapped:
                    step = f"[{arr[ind+1]} is greater than {arr[ind]} - moving {arr[ind+1]} up]"+"   "+col_str
                else:
                    step = f"[{arr[ind]} is less than {arr[ind+1]}, No swap]"+"   "+col_str

                self._steps.append(step)
            self._iterations += 1






class RadixSort(Sort):
    def __init__(self):
        super().__init__()

    def process_sort(self):
        pass

    def sort_array(self, arr: List[int]):
        pass

class QuickSort(Sort):
    def __init__(self):
        super().__init__()

    def process_sort(self) -> List[Tuple[str, List[int]]]:
        pass

    def sort_array(self, arr: List[int]):
        pass


tBubble = BubbleSort()
to_sort = Sort.generate_array(10)
tBubble.sort_array(to_sort)
