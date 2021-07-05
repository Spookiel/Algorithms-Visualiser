from typing import List, Tuple
import random
from termcolor import colored # Allows coloured text in terminal
import sys
import time
from Sorts import Sort, MergeSort



class Sorter:
    NUMBER_SORTS = 4
    SLOW_ANIM = 1.5
    MED_ANIM = 0.5
    FAST_ANIM = 0.1
    INSTA_ANIM = 0

    POSSIBLE_ARGS = ["bqrm", "smle", "smfi"]



    def __init__(self) -> None:

        self._totalComparisons: int = 0
        self._outputStepsL: bool = True
        # Contains steps in the form (string, state of array)

        self._mergeSort = MergeSort()


        # Instant, fast, med, slow, user
        self._animationSpeeds: List[int] = [Sorter.SLOW_ANIM, Sorter.MED_ANIM, Sorter.FAST_ANIM, Sorter.INSTA_ANIM]


    def display_sorting_menu(self):
        print("-" * 20, "Sorting choice menu", "-" * 20)
        print("Enter arguments space separated")
        print("-"*40)
        print("First argument: Type of sort (Case insensitive)")
        print("b: Bubble Sort", "m: Merge Sort")
        print("q: Quick Sort", "r: Radix Sort")
        print("back: To return to main menu")
        print("-"*40)
        print("Second argument: Array size (Case insensitive)")
        print("Leave blank for Small sort with fast animation")
        print(f"s: Small ({Sort.SMALL_SORT} nums)", f"m: Medium ({Sort.MED_SORT} nums)")
        print(f"l: Large ({Sort.LARGE_SORT} nums)", f"e: Extreme ({Sort.EXTREME_SORT} nums)")
        print("-"*40)
        print("Third argument: Animation speed (Case insensitive)")
        print("Leave blank for Fast Animation speed")
        print(f"i: Instant (0 second delay)", f"f: Fast ({Sorter.FAST_ANIM} second delay)")
        print(f"m: Medium ({Sorter.MED_ANIM} second delay)", f"s: Slow ({Sorter.SLOW_ANIM} second delay)")
        print("-"*40)


    def process_sorting_choice(self) -> None:

        while True:

            self.display_sorting_menu()

            try:
                args: List[str] = input("Enter arguments (space separated): ").split()
                if args[0].lower() == "back":
                    return
            except:
                print("Unknown error with input")
                try:
                    ans = input("would you like to return to main menu? (yY)")
                    if ans in "yY":
                        return
                except:
                    print("Error with input, returning to main menu")
                    return
                continue
            if self._test_sorting_args(args):

                conv_args: List = self._convert_args(args)



                if conv_args[0]=="m":

                    steps = self._mergeSort.process_sort(Sort.SORT_SIZES[conv_args[1]])
                    print(conv_args)
                    self.outputSortSteps(steps, conv_args[2])



                elif conv_args[0]=="q":
                    pass
                    #Quick sort
                elif conv_args[0]=="b":
                    #Bubble sort
                    pass
                elif conv_args[0]=="r":
                    #Radix sort
                    pass
                # Valid arguments,
            else:

                print("Invalid arguments, returning to main menu")
                return







    def bubbleSort(self, arr:List[int] ) -> None:
        raise NotImplementedError

    def quickSort(self, arr:List[int] ) -> None:
        raise NotImplementedError

    def radixSort(self, arr: List[int]) -> None:
        raise NotImplementedError




    def outputSortSteps(self, steps: List[Tuple[str, List[int]]], anim_speed: int =1) -> None:

        for step in steps:
            time.sleep(self._animationSpeeds[anim_speed])
            print(step[0], step[1])



    def _test_sorting_args(self, args: List[str]) -> bool:
        if len(args) > len(Sorter.POSSIBLE_ARGS):
            return False

        for i in range(len(args)):
            if args[i].lower() not in Sorter.POSSIBLE_ARGS[i]:
                #print(args[i], "not valid argument for position", i)
                return False
        return True


    def _convert_args(self, args: List[str]) -> List:

        size_lookup = {"s":0, "m":1, "l":2, "e":3} # Matches letter input to index in class attribute Sort.SORT_SIZES
        anim_lookup = {"s":0, "m":1, "f":2, "i":3} # Matches letter input to index in class attribute Sorter._animationSpeeds
        # Convert args to lower case to make it easier to process


        converted: List = [arg.lower() for arg in args]
        if len(converted)==1:
            converted.extend([1,2]) # Defaults for missing args
        elif len(converted)==2:
            converted[1] = size_lookup[converted[1]]
            converted.append(2)
        else:
            converted[1] = size_lookup[converted[1]]
            converted[2] = anim_lookup[converted[2]]

        return converted











