from typing import List, Tuple
import random
from termcolor import colored # Allows coloured text in terminal
import time
class Sorter:
    SMALL_SORT = 8
    MED_SORT = 15
    LARGE_SORT = 25
    EXTREME_SORT = 100
    SORT_SIZES = [SMALL_SORT,MED_SORT,LARGE_SORT, EXTREME_SORT]
    NUM_SIZES = 5


    NUMBER_SORTS = 4
    SLOW_ANIM = 1.5
    MED_ANIM = 0.5
    FAST_ANIM = 0.2
    INSTA_ANIM = 0



    def __init__(self) -> None:

        self.MENU_LOOKUP = ["", self.display_type_menu, self.display_size_menu]
        self._totalComparisons: int = 0
        self._outputStepsL: bool = True
        # Contains steps in the form (string, state of array)
        self._mergeSortSteps: List[Tuple[str, List[int]]] = []

        # Instant, fast, med, slow, user
        self._animationSpeeds: List[int] = [Sorter.INSTA_ANIM, Sorter.FAST_ANIM, Sorter.MED_ANIM, Sorter.SLOW_ANIM]



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


    def new_sorting_menu(self):
        print("-" * 20, "Sorting choice menu", "-" * 20)
        print("Enter arguments space separated")
        print("-"*40)
        print("First argument: Type of sort (Case insensitive)")
        print("b: Bubble Sort", "m: Merge Sort")
        print("q: Quick Sort", "r: Radix Sort")
        print("-"*40)
        print("Second argument: Array size (Case insensitive)")
        print("Leave blank for Small sort with fast animation")
        print(f"s: Small ({Sorter.SMALL_SORT} nums)", f"m: Medium ({Sorter.MED_SORT} nums)")
        print(f"l: Large ({Sorter.LARGE_SORT} nums)", f"e: Extreme ({Sorter.EXTREME_SORT} nums)")
        print("-"*40)
        print("Third argument: Animation speed (Case insensitive)")
        print("Leave blank for Fast Animation speed")
        print(f"i: Instant (0 second delay)", f"f: Fast ({Sorter.FAST_ANIM} second delay)")
        print(f"m: Medium ({Sorter.MED_SORT} second delay)", f"s: Slow ({Sorter.SLOW_ANIM} second delay)")
        print("-"*40)

    def display_type_menu(self):
        print("-"*20, "Sorting choice menu","-"*20)
        print("1) For Merge sort")
        print("2) For Bubble sort")
        print("3) For Quick sort")
        print("4) For Radix sort")
        print("5) Back to main menu")
        print("-"*40)



    def display_size_menu(self):
        print("-"*20, "Size menu", "-"*20)
        print("1) For Small array (8 elements)")
        print("2) For Medium array (15 elements)")
        print("3) For Large array (25 elements")
        print("4) For Extreme (100 elements) - (Individual steps not shown, just comparisons made) ")
        print("5) For load own input numbers from text file")
        print("6) Back to previous menu")
        print("-"*40)

    def process_sorting_choice(self) -> None:

        while True:

            # Plus one for back option
            typeSort: int = self.getValidChoice(Sorter.NUMBER_SORTS+1, 1) # With menu 1 - Types menu

            # 1 for merge, 2 -> bubble, 3 -> quick, 4 -> Radix, 5 -> Back

            if typeSort==5:
                # Back to main menu immediately
                return

            # Plus one for back option
            chosenSize: int = self.getValidChoice(Sorter.NUM_SIZES+1, 2) # Upper limit of 3 with menu 2 - Size menu

            # 1 -> small, 2 -> medium, 3 -> large, 4-> extreme, 5 -> Own input, 6-> Back


            if chosenSize == 6:
                # Back to top of loop
                continue

            to_sort: List[int] = self.generate_array(Sorter.SORT_SIZES[chosenSize-1])


            if typeSort==1:
                # Merge sort

                self._totalComparisons = 0
                self.mergeSort(to_sort)

                self.outputMergeSortSteps()
                print(f"Completed with {colored(str(self._totalComparisons), 'green')} comparisons!")


            elif typeSort==2:
                # Bubble sort
                self._totalComparisons = 0
                self.bubbleSort(to_sort)

                print(f"Completed with {colored(str(self._totalComparisons), 'green')} comparisons!")
            elif typeSort==3:
                # Quick sort
                self._totalComparisons = 0
                self.quickSort(to_sort)

                print(f"Completed with {colored(str(self._totalComparisons), 'green')} comparisons!")

            elif typeSort==4:
                # Comparisons not applicable for Radix sort
                # No need to reset totalComparisons

                self.radixSort(to_sort)
            elif typeSort==5:
                #Back to main menu
                return


            break


    def mergeSort(self, arr:List[int], level:int=1) -> List[int]:

        mid = len(arr)//2

        leftArr = arr[:mid]
        rightArr = arr[mid:]


        step_descrip : str = f"{colored('sorting', 'yellow')} main array at level {level}"
        arr_store: List[int] = arr[:] # [:] to copy the array to prevent mutable type issues

        self._mergeSortSteps.append((step_descrip, arr_store))

        #print(f"{colored('sorting', 'yellow')} main array at level {level}", arr)


        step_descrip: str = f"{colored('sorting', 'red')} left array at level {level}"
        arr_store: List[int] = leftArr[:]

        self._mergeSortSteps.append((step_descrip, arr_store))



        if len(leftArr) > 2:
            leftArr = self.mergeSort(leftArr, level+1)
        else:
            if len(leftArr)==2:
                self._totalComparisons += 1
                if leftArr[0] > leftArr[1]:
                    leftArr = leftArr[::-1]

        step_descrip: str = f"Left array {colored('sorted', 'green')} at level {level}"
        arr_store: List[int] = leftArr[:]

        self._mergeSortSteps.append((step_descrip, arr_store))


        step_descrip: str = f"{colored('sorting', 'red')} right array at level {level}"
        arr_store: List[int] = rightArr[:]

        self._mergeSortSteps.append((step_descrip, arr_store))

        if len(rightArr) > 2:
            rightArr = self.mergeSort(rightArr, level+1)
        else:
            if len(rightArr)==2:
                self._totalComparisons += 1
                if rightArr[0] > rightArr[1]:
                    rightArr = rightArr[::-1]

        step_descrip: str = f"Right array {colored('sorted', 'green')} at level {level}"
        arr_store: List[int] = rightArr[:]

        self._mergeSortSteps.append((step_descrip, arr_store))

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

        self._mergeSortSteps.append((step_descrip, arr_store))

        # print(f"{colored('Merged', 'green')} array at level {level}", merged)
        return merged


    def bubbleSort(self, arr:List[int] ) -> None:
        raise NotImplementedError

    def quickSort(self, arr:List[int] ) -> None:
        raise NotImplementedError

    def radixSort(self, arr: List[int]) -> None:
        raise NotImplementedError




    def outputMergeSortSteps(self, anim_speed: int =1) -> None:

        for step in self._mergeSortSteps:
            time.sleep(self._animationSpeeds[anim_speed])
            print(step[0], step[1])












