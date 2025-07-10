# 🛒 BGU Mart - SPL work 4

A supermarket chain management system built with Python and SQLite.

## Overview

BGU Mart manages branches, employees, suppliers, products, and inventory activities (sales and supplies).  
It supports database initialization, activity processing, and reporting.

## Files

- `initiate.py` — Initializes `bgumart.db` from a configuration file.
- `action.py` — Processes sales and supply actions from a file.
- `printdb.py` — Prints tables and detailed reports.

## Usage

python3 initiate.py config.txt
python3 action.py actions.txt
python3 printdb.py

## Database

Tables: Employees, Suppliers, Products, Branches, Activities.

File: bgumart.db.

## Notes

Requires Python 3.9+.

Uses SQLite3.

All modules run from the command line as standalone scripts.

