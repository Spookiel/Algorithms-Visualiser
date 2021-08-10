from typing import List
from termcolor import colored # Allows coloured text in terminal
from Sorts import Sort, MergeSort, BubbleSort, QuickSort, RadixSort
import utils


class Sorter:


    POSSIBLE_ARGS = ["bqrm", "smle", "urh"]
    DEFAULT_SIZE = 1
    DEFAULT_SORT_TYPE = 0


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
        print("c: Counting Sort")
        print("back: To return to main menu")
        print("-"*40)
        print("Second argument: Array size (Case insensitive)")
        print("Leave blank for Small sort with fast animation")
        print(f"s: Small ({Sort.SMALL_SORT} nums)", f"m: Medium ({Sort.MED_SORT} nums)")
        print(f"l: Large ({Sort.LARGE_SORT} nums)", f"e: Extreme ({Sort.EXTREME_SORT} nums)")
        print("-"*40)
        print("Third argument: Type of array (Case insensitive)")
        print("Leave blank for uniform array")
        print(f"u: Uniform (Elements 1 -> N)", f"h: High frequency (Contains lots of similar elements)")
        print(f"r: Random (Pseudo-randomly distributed elements)")
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

                s_type, size, gen_type = conv_args

                print(s_type, size, gen_type)

                sort_obj = None
                if s_type == "m":

                    sort_obj = self._mergeSort


                elif s_type == "q":
                    sort_obj = self._quickSort


                elif s_type == "b":
                    sort_obj = self._bubbleSort


                elif s_type == "r":
                    sort_obj = self._radixSort



                sort_obj.process_sort(size, gen_type)
                sort_obj.show_animation()

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
        type_lookup = {"u":0, "r":1, "h":2} # Matches letter input to index in class attribute Sorter._animationSpeeds
        # Convert args to lower case to make it easier to process

        converted: List = [arg.lower() for arg in args]

        if len(converted) == 1:

            converted.extend([Sorter.DEFAULT_SIZE, Sorter.DEFAULT_ANIM]) # Defaults for missing args
        elif len(converted) == 2:

            converted[1] = size_lookup[converted[1]]
            converted.append(Sorter.DEFAULT_SORT_TYPE)
        else:

            converted[1] = size_lookup[converted[1]]
            converted[2] = type_lookup[converted[2]]

        return converted











