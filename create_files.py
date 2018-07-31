#!/usr/bin/env python
from mpi4py import MPI
import os

global jack
jack = """All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jack a dull boy
All work and no play makes Jac"""

def main():
    make_file()

def make_file():
    for r in range(1000):
        comm = MPI.COMM_WORLD
        rank = comm.Get_rank()
        if(r == rank):
            name = "file_%05d.txt" % rank
            os.system(jack + ' > ' + name)


if __name__ == "__main__":
    main()
