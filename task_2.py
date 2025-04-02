
import re
from collections import Callable

def generator_numbers(text: str):
    words = text.split()

    for word in words:
        try:
            number = float(word)
            yield number
        except ValueError:
            continue

def sum_profit(text: str, func: Callable) -> float:
        