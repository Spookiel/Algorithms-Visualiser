from typing import List
from termcolor import colored # Allows coloured text in terminal
from Sorts import Sort, MergeSort, BubbleSort, QuickSort, RadixSort
import utils


class Sorter:


    POSSIBLE_ARGS = ["bqrm", "smle", "smfi"]
    DEFAULT_SIZE = 1
    DEFAULT_ANIM = 2


    def __init__(self) -> None:

        self._outputSteps: bool = True

        self._mergeSort = MergeSort()
        self._bubbleSort = BubbleSort()
        self._radixSort = RadixSort()
        self._quickSort = QuickSort()




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
        print(f"i: Instant (0 second delay)", f"f: Fast ({Sort.FAST_ANIM} second delay)")
        print(f"m: Medium ({Sort.MED_ANIM} second delay)", f"s: Slow ({Sort.SLOW_ANIM} second delay)")
        print("-"*40)


    def process_sorting_choice(self) -> None:

        while True:

            self.display_sorting_menu()
            back, args = utils.run_menu(self.display_sorting_menu)

            if back:
                return

            if self._test_sorting_args(args):

                conv_args: List = self._convert_args(args)
                assert len(conv_args) == 3

                s_type, size, speed = conv_args

                if s_type == "m":
                    
                    self._mergeSort.process_sort(size, speed)

                elif s_type == "q":
                    # Quick sort
                    self._quickSort.process_sort(size, speed)

                elif s_type == "b":

                    self._bubbleSort.process_sort(size, speed)

                elif s_type == "r":

                    self._radixSort.process_sort(size, speed)
            else:

                print("Invalid arguments, returning to main menu")
                return



    def _test_sorting_args(self, args: List[str]) -> bool:
        if len(args) > len(Sorter.POSSIBLE_ARGS):
            return False

        for i in range(len(args)):
            if args[i].lower() not in Sorter.POSSIBLE_ARGS[i]:
                return False

        return True


    def _convert_args(self, args: List[str]) -> List:

        size_lookup = {"s":0, "m":1, "l":2, "e":3} # Matches letter input to index in class attribute Sort.SORT_SIZES
        anim_lookup = {"s":0, "m":1, "f":2, "i":3} # Matches letter input to index in class attribute Sorter._animationSpeeds
        # Convert args to lower case to make it easier to process

        converted: List = [arg.lower() for arg in args]

        if len(converted) == 1:

            converted.extend([Sorter.DEFAULT_SIZE, Sorter.DEFAULT_ANIM]) # Defaults for missing args
        elif len(converted) == 2:

            converted[1] = size_lookup[converted[1]]
            converted.append(Sorter.DEFAULT_ANIM)
        else:

            converted[1] = size_lookup[converted[1]]
            converted[2] = anim_lookup[converted[2]]

        return converted











