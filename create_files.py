#!/usr/bin/env python
from mpi4py import MPI
import os

def main():
    make_file()

def make_file():
    for i in range(1000000):
        comm = MPI.COMM_WORLD
        rank = comm.Get_rank()
        name = "file_%05d.txt" % rank
        os.system('Touch ' + name)

if __name__ == "__main__":
    main()
