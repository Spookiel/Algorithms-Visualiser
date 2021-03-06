from typing import List, Tuple, Callable
import os
from matplotlib import animation
from matplotlib import pyplot as plt
plt.rcParams['animation.ffmpeg_path'] = "C:/Users/lukem/FFmpeg/bin"


def run_menu(display_menu: Callable) -> Tuple[int, List]: # Return is of form (Back to previous menu, args)

    display_menu()

    try:
        inp: str = input("Enter arguments (space separated): ")
        if len(inp) == 0:
            return 0, []

        args:List = inp.split()
        if args[0].lower()=="back":
            return 1, []

    except:
        print("Unknown error with input, returning to previous menu")
        return 1, []

    return 0, args

def count_lines():
    tlines = 0
    for file in os.listdir():
        if file.endswith(".py"):
            print(f"{file} - {len(open(file).readlines())} lines")
            tlines += len(open(file).readlines())
    print(f"Total lines in the project: {tlines}")
    print("-" * 40)


def usage():
    print("run with t as second argument for terminal mode")
    print("run with g as second argument for GUI mode")
    print("-"*40+"\n")


def save_anim(anim, anim_type:int = 0):
    fpath = os.path.join(os.getcwd(), "animations", str(anim_type))
    ind = 0
    while os.path.exists(os.path.join(fpath, f"anim_{ind}.mp4")):
        ind += 1

    final_fpath = os.path.join(fpath, f"anim_{ind}.mp4")
    print(f"Saving to file location {final_fpath}")
    writer_two = animation.FFMpegWriter(fps=60)

    anim.save(final_fpath, writer=writer_two)



