from typing import List
import random


class Sorter:
    SMALL_SORT = 8
    MED_SORT = 15
    LARGE_SORT = 25
    SORT_SIZES = [SMALL_SORT,MED_SORT,LARGE_SORT]
    NUMBER_SORTS = 3
    NUM_SIZES = 3


    def __init__(self) -> None:

        self.MENU_LOOKUP = ["", self.display_type_menu, self.display_size_menu]


    def getValidChoice(self, upper: int, menuChoice: int = 0, lower: int = 1) -> int:


        while True:
            self.MENU_LOOKUP[menuChoice]()
            str_choice: str = input(f"Enter choice({lower}-{upper}): ")

            try:
                int_choice: int = int(str_choice)

                if lower <= int_choice <= upper:
                    return int_choice

                print("Please input a number which is in range")
            except:
                print("Invalid input, please enter an integer")


    def generate_array(self, upto: int ) -> List[int]:
        nums = [i+1 for i in range(upto)]

        random.shuffle(nums)

        return nums

    def display_type_menu(self):
        print("-"*20, "Sorting choice menu","-"*20)
        print("1) For Merge sort")
        print("2) For Bubble sort")
        print("3) For Quick sort")

        #print(f"Enter choice (1-{Sorter.NUMBER_SORTS})")

    def display_size_menu(self):
        print("-"*20, "Size menu", "-"*20)
        print("1) For Small array (8 elements)")
        print("2) For Medium array (15 elements)")
        print("3) For Large array (25 elements")

    def process_sorting_choice(self) -> None:

        typeSort = self.getValidChoice(Sorter.NUMBER_SORTS, 1) # With menu 1 - Types menu

        # 1 for merge, 2 -> bubble, 3 -> quick

        chosenSize = self.getValidChoice(3, 2) # Upper limit of 3 with menu 2 - Size menu

        # 1 -> small, 2 -> medium, 3 -> large

        to_sort: List[int] = self.generate_array(Sorter.SORT_SIZES[chosenSize-1])


        if typeSort==1:
            # Merge sort
            self.mergeSort(to_sort)
        elif typeSort==2:
            # Bubble sort
            self.bubbleSort(to_sort)
        elif typeSort==3:
            # Quick sort
            self.quickSort(to_sort)


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


    def bubbleSort(self, arr:List[int] ) -> None:
        raise NotImplementedError

    def quickSort(self, arr:List[int] ) -> None:
        raise NotImplementedError