#
# Code written by Jingwen Feng 02/28/2024. All rights reserved.
#
from a_star import AStar
from ucs import UCS



def get_user_input(attempt=1, max_attempts=3):
    if attempt > max_attempts:
        print("Maximum attempts exceeded. Using the default stack.")
        return [10, 9, 8, 7, 6, 5, 4, 1, 3, 2]

    user_input = input("Enter the pancake stack numbers separated by spaces (e.g., '10 9 8 7 6 5 4 1 3 2'): ")
    try:
        initial_stack = [int(x) for x in user_input.split()]
        if len(initial_stack) > 1:
            return initial_stack
        else:
            print("Invalid input. A valid sequence with at least two numbers is required.")
            return get_user_input(attempt + 1)
    except ValueError:
        print("Invalid input. Please enter a valid sequence of integers.")
        return get_user_input(attempt + 1)

if __name__ == "__main__":
    choice = input("Do you want to input your own pancake stack? YES/NO: ").strip().lower()
    if choice == 'yes':
        initial_stack = get_user_input()
    elif choice == 'no':
        initial_stack = [10, 9, 8, 7, 6, 5, 4, 1, 3, 2]
    else:
        print("Invalid choice. Using the default stack.")
        initial_stack = [10, 9, 8, 7, 6, 5, 4, 1, 3, 2]

    print("Initial stack: ", initial_stack)

    astar = AStar(initial_stack)
    astar.search()
    print("A Star:")
    print("Solution Set:", astar.solution())
    print("Steps:", astar.steps())
    print("Time:", astar.time())
    print("Space:", astar.space())

    ucs = UCS(initial_stack)
    ucs.search()
    print("UCS:")
    print("Solution Set:", ucs.solution())
    print("Steps:", ucs.steps())
    print("Time:", ucs.time())
    print("Space:", ucs.space())
