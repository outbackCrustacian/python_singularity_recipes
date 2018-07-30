#!/usr/bin/env python
from mpi4py import MPI
import os

def main():
    make_file()

def make_file():
    os.system('Touch file.txt')

if __name__ == "__main__":
    main()
