#!/usr/bin/env python
from org_vids import sort
import os

try:
    os.mkdir("./output")
    os.mkdir("./input")
except FileExistsError:
    pass

if __name__ == "__main__":
    sort()
