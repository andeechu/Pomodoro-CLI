# The following list of colors is based on rene-d's ANSI colors list:
# https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007

# Colors
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"

# Returns a Color string based on an integer (percent) value
def get_color_by_int(percent: int) -> str:
    if percent <= 10:
        return BLUE + FAINT
    elif percent <= 20:
        return PURPLE + FAINT
    elif percent <= 30:
        return PURPLE
    elif percent <= 40:
        return LIGHT_PURPLE
    elif percent <= 50:
        return BLUE
    elif percent <= 60:
        return LIGHT_BLUE
    elif percent <= 70:
        return CYAN
    elif percent <= 80:
        return LIGHT_CYAN
    elif percent <= 90:
        return GREEN
    elif percent <= 99:
        return LIGHT_GREEN
    else:
        return LIGHT_GREEN + BOLD

# Returns the Color string for END
def get_color_end() -> str:
    return END

