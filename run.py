#!/usr/bin/env python
from org_vids import sort
import os

try:
    os.mkdir("./org_vids/output/")
    os.mkdir("./org_vids/input/")
except FileExistsError:
    pass

if __name__ == "__main__":
    sort()
