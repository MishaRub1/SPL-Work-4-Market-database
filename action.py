from persistence import *

import sys

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            if splittedline[0] == "C":
                repo.branches.insert(Branche(int(splittedline[1]), splittedline[2], int(splittedline[3])))
            elif splittedline[0] == "S":
                repo.suppliers.insert(Supplier(int(splittedline[1]), splittedline[2], splittedline[3]))
            elif splittedline[0] == "P":
                repo.products.insert(Product(int(splittedline[1]), splittedline[2], float(splittedline[3]), int(splittedline[4])))
            elif splittedline[0] == "E":
                repo.employees.insert(Employee(int(splittedline[1]), splittedline[2], float(splittedline[3]), int(splittedline[4])))
if __name__ == '__main__':
    main(sys.argv)