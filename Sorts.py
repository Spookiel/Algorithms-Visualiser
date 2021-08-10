from abc import ABC, abstractmethod
import random
from termcolor import colored  # Allows coloured text in terminal
from typing import List, Tuple
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import  os

class Sort(ABC):
    SMALL_SORT = 8
    MED_SORT = 15
    LARGE_SORT = 25
    EXTREME_SORT = 150
    SORT_SIZES = [SMALL_SORT, MED_SORT, LARGE_SORT, EXTREME_SORT]
    NUM_SIZES = 5

    SLOW_ANIM = 1
    MED_ANIM = 0.2
    FAST_ANIM = 0.05
    INSTA_ANIM = 0
    ANIM_SPEEDS = [SLOW_ANIM, MED_ANIM, FAST_ANIM, INSTA_ANIM]
    MATPLOT_INTERVALS = [250, 100, 10, 1]

    def __init__(self):
        self._steps: List[Tuple[str, List[int]]] = []
        self._totalComparisons = 0
        self._frames: List[List[int]] = []

    @abstractmethod
    def sort_array(self, arr: List[int]):
        raise NotImplementedError

    @abstractmethod
    def process_sort(self, size: int = 1, delay: int = 2) -> None:
        raise NotImplementedError

    def update_fig(self, arr: List[int], bars, comps):

        for bar, val in zip(bars, arr):

            bar.set_height(val)

            bar.set_color(self.col_look[val-1])


        self.its += 1
        self.__text.set_text("# of operations: {}".format(self.its))
        self.__text2.set_text(f"Time elapsed: {round(time.time()-self._anim_start,3)}")
        # Add code to increment #iterations and draw them
        # Add code to change the colour of all bars which need to be highlighted

    def show_animation(self, save=False) -> None:
        """
        Generates a matplotlib animation for the given set of frames

        :param frames:
        :return None:
        """
        cmap = plt.get_cmap("winter")
        assert len(self.frames) > 0

        fig, ax = plt.subplots()

        plt.yticks([])
        self.its = 0
        frames_gen = (f for f in self.frames)

        arr = next(frames_gen)

        rescale = lambda y: 1-((y - np.min(y)) / (np.max(y) - np.min(y)))

        self.col_look = cmap(rescale(sorted(arr)))

        bars = ax.bar(range(len(arr)), arr, align="edge", color=self.col_look, alpha=0.88, width=1.0)

        ax.set_xlim(0, len(arr))
        ax.set_ylim(0, len(arr)*1.15)

        self.__text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontfamily="serif")
        self.__text2 = ax.text(0.02, 0.90, "", transform=ax.transAxes, fontfamily="serif")
        # Calculate interval based on number of frames

        interval: int = 10   # Delay between frames in ms
        if len(self.frames) < 20:
            interval = Sort.MATPLOT_INTERVALS[0]
        elif len(self.frames) < 100:
            interval = Sort.MATPLOT_INTERVALS[1]
        elif len(self.frames) < 200:
            interval = Sort.MATPLOT_INTERVALS[2]
        elif len(self.frames) > 200:
            interval = Sort.MATPLOT_INTERVALS[3]

        self._anim_start = time.time()

        anim = animation.FuncAnimation(fig, func=self.update_fig, fargs=(bars, 0), frames=frames_gen,
                                       interval=interval, repeat=False, save_count=len(self.frames))

        if save:
            fpath = os.path.join(os.getcwd(), "animations", "test.gif")
            print(f"Saving to file location {fpath}")
            gifwriter = animation.PillowWriter(fps=60)

            anim.save(fpath, writer=gifwriter)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def generate_array(upto: int) -> List[int]:
        nums = [i + 1 for i in range(upto)]

        random.shuffle(nums)

        return nums

    @property
    def frames(self):
        return self._frames

# Re-write merge sort as in place sorting


class MergeSort(Sort):

    def __init__(self):

        super().__init__()

    def process_sort(self, size: int = 1, delay: int = 2) -> None:

        self._steps: List[Tuple[str, List[int]]] = []  # Resets after each sort
        self._totalComparisons: int = 0
        self._frames = []
        to_sort: List[int] = Sort.generate_array(Sort.SORT_SIZES[size])

        self.sort_array(to_sort)

    def sort_array(self, arr: List[int], level: int = 1) -> List[int]:

        mid = len(arr) // 2

        left_arr = arr[:mid]
        right_arr = arr[mid:]


        if len(left_arr) > 2:
            left_arr = self.sort_array(left_arr, level + 1)

        else:

            if len(left_arr) == 2:
                self._totalComparisons += 1

                if left_arr[0] > left_arr[1]:
                    left_arr = left_arr[::-1]

        if len(right_arr) > 2:
            right_arr = self.sort_array(right_arr, level + 1)
        else:
            if len(right_arr) == 2:
                self._totalComparisons += 1
                if right_arr[0] > right_arr[1]:
                    right_arr = right_arr[::-1]

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

        return merged



class BubbleSort(Sort):

    def __init__(self):
        super().__init__()

        self._steps: List[str] = []
        self._iterations = 0

    def process_sort(self, size: int = 1, speed: int = 1) -> None:
        self._iterations = 0

        to_sort = Sort.generate_array(Sort.SORT_SIZES[size])

        self._frames = []

        self.sort_array(to_sort)


    def sort_array(self, arr: List[int]) -> None:

        swapped = True

        while swapped:
            swapped = False
            for ind in range(len(arr) - self._iterations - 1):

                self._totalComparisons += 1
                if arr[ind] > arr[ind + 1]:
                    arr[ind], arr[ind + 1] = arr[ind + 1], arr[ind]
                    swapped = True

                    self._frames.append(arr[:])  # Add frame to animation if element is swapped

            self._iterations += 1



class RadixSort(Sort):
    def __init__(self):
        super().__init__()

    def process_sort(self, size: int = 1, speed: int = 1):
        raise NotImplementedError

    def sort_array(self, arr: List[int]):
        raise NotImplementedError



class QuickSort(Sort):
    def __init__(self):
        super().__init__()

    def process_sort(self, size: int = 1, speed: int = 1, display_text_steps: bool = True) -> None:
        self._iterations = 0

        to_sort = Sort.generate_array(Sort.SORT_SIZES[size])
        self._frames = []
        self.sort_array(to_sort)


    def sort_array(self, arr: List[int]):

        self._quick_sort(arr, 0, len(arr) - 1)

    def _quick_sort(self, arr: List[int], lo: int, hi: int, level: int = 1):

        if lo < hi:

            part = self._partition(arr, lo, hi)


            self._quick_sort(arr, lo, part - 1, level + 1)
            self._quick_sort(arr, part + 1, hi, level + 1)


    def _partition(self, arr: List[int], lo: int, hi: int) -> int:
        """
        Partitions array for quick sort, using the Lomutu partition system (stable)

        :param arr:
        :param lo:
        :param hi:
        :return:
        """
        piv: int = arr[hi]

        ind: int = int(lo)

        for j in range(ind, hi):
            if arr[j] < piv:
                arr[ind], arr[j] = arr[j], arr[ind]
                ind += 1
                self._frames.append(arr[:])

        arr[ind], arr[hi] = arr[hi], arr[ind]
        self._frames.append(arr[:])
        return ind



class CountingSort(Sort):
    def __init__(self):
        super().__init__()

    def process_sort(self, size: int = 1, speed: int = 1) -> List[Tuple[str, List[int]]]:
        raise NotImplementedError

    def sort_array(self, arr: List[int]):
        raise NotImplementedError


