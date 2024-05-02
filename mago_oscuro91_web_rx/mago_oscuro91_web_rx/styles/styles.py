from enum import Enum


MAX_WIDTH = "1200px"


class Size(Enum):
    ZERO = "0em ! important"
    DEFAULT = "1em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    BIG = "2em"
    BUTTON = "2.75em"
    BIG_BIG = "3em"
    VERY_BIG = "4em"


max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)

max_width_style_center = dict(
    align_items="center",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)
