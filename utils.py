from typing import List, Tuple, Callable



def run_menu(display_menu: Callable) -> Tuple[int, List]: # Return is of form (Back to previous menu, args)

    display_menu()

    try:
        args: List[str] = input("Enter arguments (space separated): ").split()
        if args[0].lower()=="back":
            return 1, []

    except:
        print("Unknown error with input, returning to previous menu")
        return 1, []

    return 0, args


