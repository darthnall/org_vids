#!/usr/bin/env python
from org_vids import sort
import os

try:
<<<<<<< HEAD
    os.mkdir("./org_vids/output")
    os.mkdir("./org_vids/input")
=======
    os.mkdir("./org_vids/output/")
    os.mkdir("./org_vids/input/")
>>>>>>> fc393c272fcac221443a22a336a502d2b0d93792
except FileExistsError:
    pass

if __name__ == "__main__":
    sort()
