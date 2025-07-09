from itertools import product
import re
from persistence import *

import sys

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            product_id = int(splittedline[0])
            quantity = int(splittedline[1])
            activator_id = int(splittedline[2])
            date = splittedline[3]

            product = repo.products.find(id = product_id)
            if product is None:
                continue

            product = product[0]

            if quantity > 0:
                product.quantity = product.quantity + quantity
                repo.products.delete(id = product_id)
                repo.products.insert(Product(product_id, product.description, product.price, product.quantity))

            else:
                if product.quantity < quantity:
                    continue

                product.quantity += quantity
                repo.products.delete(id = product_id)
                repo.products.insert(Product(product_id, product.description, product.price, product.quantity))

            repo.activities.insert(Activitie(product_id, quantity, activator_id, date))
if __name__ == '__main__':
    main(sys.argv)