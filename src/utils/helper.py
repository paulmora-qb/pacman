"""Helper functions"""

from typing import Tuple

from matplotlib import colors


def create_color_rgb(color_name: str) -> Tuple[int]:
    """This function creates the rgb color code tuple from the name of the color.
    This is low effort given the matplotlib function, though I could not find a quick
    package that gives the color in range from 0 to 255 instead of 0 to 1

    Args:
        color_name (str): Name of the color

    Returns:
        Tuple[int]: Tuple with the rgb color code
    """
    return tuple((int(x * 255) for x in colors.to_rgb(color_name)))
    