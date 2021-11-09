from abc import ABC, abstractmethod
import random
from termcolor import colored  # Allows coloured text in terminal
from typing import List, Tuple
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import log10
import  os
import sys
import utils
sys.setrecursionlimit(10000)
plt.rcParams['animation.ffmpeg_path'] = "C:/Users/lukem/FFmpeg/bin"

class Sort(ABC):
    SMALL_SORT = 8
    MED_SORT = 25
    LARGE_SORT = 50
    EXTREME_SORT = 150
    SORT_SIZES = [SMALL_SORT, MED_SORT, LARGE_SORT, EXTREME_SORT]
    NUM_SIZES = 5

    SLOW_ANIM = 1
    MED_ANIM = 0.2
    FAST_ANIM = 0.05
    INSTA_ANIM = 0
    ANIM_SPEEDS = [SLOW_ANIM, MED_ANIM, FAST_ANIM, INSTA_ANIM]
    MATPLOT_INTERVALS = [2000, 250, 30, 1]

    HIGH_FREQ_BARS = 7

    def __init__(self):
        self._steps: List[Tuple[str, List[int]]] = []
        self._totalComparisons = 0
        self._frames: List[List[int]] = []
        self._fast_frames: List[Tuple[int, int]] = []
        self._frameHighlights: List[List[Tuple[int, int]]] = [] # Stores bar index, colour of specific bars to highlight for each frame
        self.col_look = None # Stores the colour map lookup which is initialised for each new animation
        self.__timer_text = None # Initialised within show_animation()
        self.__iterations_text = None # Initialised within show_animation()






    @abstractmethod
    def sort_array(self, arr: List[int]):
        raise NotImplementedError
    
    @abstractmethod
    def process_sort(self, size: int = 1, gen_type: int = 0, upto: int = -1) -> None:
        raise NotImplementedError

    def update_fig(self, arr: List[int], bars, comps):

        for bar, val in zip(bars, arr):

            bar.set_height(val)
            #print(self.col_look[ind])

            if val != 0:
                #print(val, self.val_ind_look[val])
                bar.set_color(self.col_look[self.val_ind_look[val]])
                #bar.set_color(self.col_look[val-1])


        self.its += 1
        self.__iterations_text.set_text("# of operations: {}".format(self.its))
        self.__timer_text.set_text(f"Time elapsed: {round(time.time()-self._anim_start,3)}")
        # Add code to increment #iterations and draw them
        # Add code to change the colour of all bars which need to be highlighted


    def update_fig_fast(self, arr, bars, comp):


        for ind, val in arr:
            bars[ind].set_height(val)

            if val != 0:
                # print(val, self.val_ind_look[val])
                bars[ind].set_color(self.col_look[self.val_ind_look[val]])
                # bar.set_color(self.col_look[val-1])

        self.its += 1
        self.__iterations_text.set_text("# of operations: {}".format(self.its))
        self.__timer_text.set_text(f"Time elapsed: {round(time.time()-self._anim_start,3)}")
        # Add code to increment #iterations and draw them
        # Add code to change the colour of all bars which need to be highlighted




    @staticmethod
    def rescale(arr: List[int]):
        """
        Returns list of floats for use with matplotlib colour maps

        :param arr:
        :return:
        """
        return 1-((arr - np.min(arr)) / (np.max(arr) - np.min(arr)))

    def show_animation(self, save=False, fast_anim = False) -> None:
        """
        Generates a matplotlib animation for the given set of frames

        :param frames:
        :return None:
        """
        cmap = plt.get_cmap("winter")

        if not fast_anim:
            loc_frames = self.frames
        else:
            loc_frames = self._fast_frames

        assert len(loc_frames) > 0

        fig, ax = plt.subplots()

        plt.yticks([])
        plt.xticks([])
        self.its = 0
        frames_gen = (f for ind,f in enumerate(loc_frames) if ind%1==0)

        if fast_anim:
            arr = self.frames[0]
        else:
            arr = next(frames_gen)
        bars = ax.bar(range(len(arr)), arr, align="edge", color=self.col_look, alpha=0.88, width=1.0)





        self.col_look = cmap(Sort.rescale(sorted(arr)))
        self.val_ind_look = {}

        so = sorted(arr)
        for ind, val in enumerate(so):
            self.val_ind_look[val] = ind


        for bar, val in zip(bars, arr):
            if val != 0:
                bar.set_color(self.col_look[self.val_ind_look[val]])


        ax.set_xlim(0, len(arr))
        ax.set_ylim(0, max(arr)*1.15)

        self.__iterations_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontfamily="serif")
        self.__timer_text = ax.text(0.02, 0.90, "", transform=ax.transAxes, fontfamily="serif")
        # Calculate interval based on number of frames

        interval: int = 10   # Delay between frames in ms
        if len(loc_frames) < 20:
            interval = Sort.MATPLOT_INTERVALS[0]
        elif len(loc_frames) < 50:
            interval = Sort.MATPLOT_INTERVALS[1]
        elif len(loc_frames) < 200:
            interval = Sort.MATPLOT_INTERVALS[2]
        elif len(loc_frames) > 200:
            interval = Sort.MATPLOT_INTERVALS[3]

        self._anim_start = time.time()

        update_func = self.update_fig if not fast_anim else self.update_fig_fast

        anim = animation.FuncAnimation(fig, func=update_func, fargs=(bars, 0), frames = frames_gen,
                                   interval=interval, repeat=False, save_count=len(loc_frames))

        if save:
            utils.save_anim(anim, 0)

        plt.tight_layout()
        plt.show()



    @staticmethod
    def generate_uni_array(size: int, upto: int) -> List[int]:
        nums = [i+1 for i in range(size)]

        random.shuffle(nums)

        return nums

    @staticmethod
    def generate_rand_array(size: int, upto: int) -> List[int]:

        nums = [random.randint(1, upto) for _ in range(size)]

        return nums

    @staticmethod
    def generate_high_freq_array(upto: int) -> List[int]:


        choices = [(upto*x)//Sort.HIGH_FREQ_BARS for x in range(1, Sort.HIGH_FREQ_BARS+1)]

        nums = [random.choice(choices) for _ in range(upto)]


        return nums
    
    @staticmethod
    def generate(size: int, upto: int = -1, gen_type: int = 0):
        
        if upto==-1:
            upto = int(size)
        
        
        if gen_type==0:

            return Sort.generate_uni_array(size,upto)
        elif gen_type==1:

            return Sort.generate_rand_array(size,upto)
        elif gen_type==2:

            return Sort.generate_high_freq_array(upto)

    @property
    def frames(self):
        return self._frames

# Re-write merge sort as in place sorting


class MergeSort(Sort):

    def __init__(self):

        super().__init__()

    def process_sort(self, size: int = 1, gen_type: int = 0, upto: int = -1) -> None:

        self._steps: List[Tuple[str, List[int]]] = []  # Resets after each sort
        self._totalComparisons: int = 0
        self._frames = []
        if upto == -1:
            upto = Sort.SORT_SIZES[size]

        to_sort: List[int] = Sort.generate(Sort.SORT_SIZES[size], upto, gen_type)

        self.sort_array(to_sort,0, len(to_sort)-1)

    def sort_array(self, arr: List[int], l: int , r: int):

        if r == -5:
            r = len(arr)

        if l < r:
            mid = l + (r - l) // 2

            self.sort_array(arr, l, mid)
            self.sort_array(arr, mid+1, r)
            self.merge_array(arr, l, mid, r)
            self._frames.append(arr[:])

    def merge_array(self, arr: List[int], start, mid, end):

        right_start = mid+1

        if arr[mid] <= arr[right_start]:
            return

        while start <= mid and right_start <= end:

            if arr[start] <= arr[right_start]:
                start += 1
            else:
                val = arr[right_start]
                ind = int(right_start)

                while ind != start:
                    arr[ind] = arr[ind-1]
                    ind -= 1
                arr[start] = val
                self._frames.append(arr[:])

                start += 1
                mid += 1
                right_start += 1



class BubbleSort(Sort):

    def __init__(self):
        super().__init__()

        self._steps: List[str] = []
        self._iterations = 0

    def process_sort(self, size: int = 1, gen_type: int = 0, upto: int = -1) -> None:
        self._iterations = 0

        if upto == -1:
            upto = Sort.SORT_SIZES[size]

        to_sort = Sort.generate(Sort.SORT_SIZES[size], upto, gen_type)

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




class QuickSort(Sort):
    def __init__(self):
        super().__init__()

    def process_sort(self, size: int = 1, gen_type: int = 0, upto: int = -1) -> None:
        self._iterations = 0


        if upto == -1:
            upto = Sort.SORT_SIZES[size]
        to_sort = Sort.generate(Sort.SORT_SIZES[size], upto, gen_type)
        #print(to_sort)
        self._frames = [to_sort[:]]
        self._fast_frames = []
        #print(to_sort, size, gen_type, upto)
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
                self._fast_frames.append([(int(ind), int(arr[j])), (int(j), int(arr[ind]))])
                arr[ind], arr[j] = arr[j], arr[ind]
                #self._fast_frames.append([(int(ind), int(arr[j])), (int(j), int(arr[ind]))])
                ind += 1

                self._frames.append(arr.copy())
        self._fast_frames.append([(int(ind), int(arr[hi])), (int(hi), int(arr[ind]))])
        arr[ind], arr[hi] = arr[hi], arr[ind]
        #self._fast_frames.append([(int(ind), int(arr[hi])), (int(hi), int(arr[ind]))])
        self._frames.append(arr.copy())
        return ind



class RadixSort(Sort):
    def __init__(self):
        super().__init__()

    def process_sort(self, size: int = 1, gen_type: int = 0, upto: int = -1):

        if upto == -1:
            upto = Sort.SORT_SIZES[size]

        to_sort = Sort.generate(Sort.SORT_SIZES[size], upto, gen_type)
        print(to_sort)
        self._frames = []
        self.sort_array(to_sort)

    def sort_array(self, arr: List[int]):

        large = max(arr)
        exp = 1


        self._frames.append(arr)
        while exp <= large:
            arr = self.count_sort(arr, exp)
            #print(arr, "AFTER")

            self._frames.append(arr[:])
            exp *= 10


    def count_sort(self, arr, exp):

        N = len(arr)



        output = [0 for _ in range(N)]
        count = [0 for _ in range(10)]


        # Count occurences

        for val in arr:
            dig = (val/exp)
            count[int(dig%10)] += 1

        # Prefix sum bit

        for i in range(1,len(count)):
            count[i] += count[i-1]

        count = [0]+count[:-1]



        for j in range(0, len(arr)):
            ke = int(arr[j]/exp)
            output[count[ke%10]] = arr[j]
            self._frames.append(output[:])
            count[ke%10] += 1


        return output



if __name__ == "__main__":

    #print(animation.writers.list())
    q = QuickSort()
    q.process_sort(size=3)
    q.show_animation(fast_anim=True)
    #q.show_animation(fast_anim=False)