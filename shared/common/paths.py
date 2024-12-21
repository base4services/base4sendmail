import os
import pathlib


# Root directory of the project
def root():
    return pathlib.Path(__file__).parent.parent.parent

