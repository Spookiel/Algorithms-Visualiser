from abc import ABC, abstractmethod
from Simulator import Simulator
from Renderer import Renderer

from typing import List
import random

class UI(ABC):


    def __init__(self):
        self._simulator = Simulator()


    @property
    def simulator(self):
        return self._simulator


    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError


class GUI(UI):

    def __init__(self) -> None:
        super().__init__()
        self._renderer = Renderer()

    def run(self) -> None:
        raise NotImplementedError

    @property
    def renderer(self):
        return self._renderer


class Terminal(UI):
    MENULEN = 4
    SMALL_SORT = 8
    MED_SORT = 15
    LARGE_SORT = 25
    def __init__(self) -> None:
        super().__init__()


    def run(self) -> None:
        while True:
            self.display_menu()
            str_choice: str = input(f"Enter choice (1-{Terminal.MENULEN}): ")
            try:
                int_choice: int = int(str_choice)
            except ValueError:
                print("Invalid input for choice, please try again")
                continue #Back to start of loop

            if int_choice < 1 or int_choice > self.MENULEN:
                print("Choice is out of range, please try again")
                continue

            #Valid choice so process here

            if int_choice==1:
                self.process_sorting_choice()
            elif int_choice==2:
                pass
            elif int_choice==3:
                pass
            elif int_choice==4:
                pass


    def generate_array(self, upto:int ) -> List[int]:
        nums = [i+1 for i in range(upto)]

        random.shuffle(nums)

        return nums

    def process_sorting_choice(self) -> None:

        to_sort = self.generate_array(Terminal.MED_SORT)

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








    def display_menu(self):
        print("Menu:")
        print("1. View sorting algorithm options")
        print("2. View grid searching algorithm options")
        print("3. View maze generation and searching options")
        print("4. Quit")
        print("-"*50)

