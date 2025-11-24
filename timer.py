import time
import sys
import os
from colors import get_color_by_int, get_color_end

# Emoji Reddit Post
# https://www.reddit.com/r/Python/comments/qy4iym/you_can_insert_emoji_using_nname_of_emoji/

# List that contains valid user input
valid_input: list[str] = ['yes', 'y', '1']

# Display a progress bar within the console
def progress_bar(progress: int, total: int, seconds: int, minutes: int) -> None:
    percent = 100 * (progress / float(total))
    color = get_color_by_int(percent)
    bar = color + '█' * int(percent/2) + get_color_end() + '⣿' * (50 - int(percent/2))
    print(f'\r POMO |{bar}| [{minutes:02}:{seconds:02}] [{percent:.0f}%] \N{Tomato}', end='\r')

# Hides the cursor within the console
def hide_cursor():
    print('\033[?25l', end='')

# Displays the cursor within the console
def show_cursor():
    print('\033[?25h', end='')

# Clearing console
os.system('clear')

# Boolean flag to control the timer
is_continue = True

# Variable to store user input as an integer (minutes)
my_time: int = 60 * int(sys.argv[1])

# Hiding cursor before starting timer
hide_cursor()

# Starting timer
while (is_continue):

    # Variable to store current timer progress
    progress_counter = 0

    # Using range(start, stop, step)
    # Reverse for loop that decrements by one (based on time value provided by the user)
    for x in range(my_time, -1, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        # Alternate way to display the timer
        # print(f'{hours:02}:{minutes:02}:{seconds:02}', end='\r')
        progress_bar(progress_counter, my_time, seconds, minutes)
        # Increment progress counter by 1 (one) second
        progress_counter += 1
        # Set progress bar delay by one (1) second
        time.sleep(1)
    
    print('', end='\n')
    # Displaying cursor for user input
    show_cursor()
    # Prompting user to restart timer
    yes_or_no = input(f'Continue \N{Tomato} ? ')
    # Restarts timer if input is valid
    is_continue = True if yes_or_no in valid_input else False
    # Hiding cursor again
    hide_cursor()
    os.system('clear')

# print('', end='\n')

# Displaying cursor again after timer stops
show_cursor()

