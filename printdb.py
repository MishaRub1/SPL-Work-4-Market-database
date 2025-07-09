from persistence import *

def print_table(name: str, records: list):
    print(name)
    for record in records:
        print(record)

def main():
    activities = repo._conn.execute("""
        SELECT * FROM activities ORDER BY date ASC
    """).fetchall()
    activities_objs = [Activitie(*row) for row in activities]
    print_table("Activities", activities_objs)

    # Branches
    branches = repo.branches.find_all()
    branches.sort(key=lambda x: x.id)
    print_table("Branches", branches)

    # Employees
    employees = repo.employees.find_all()
    employees.sort(key=lambda x: x.id)
    print_table("Employees", employees)

    # Products
    products = repo.products.find_all()
    products.sort(key=lambda x: x.id)
    print_table("Products", products)

    # Suppliers
    suppliers = repo.suppliers.find_all()
    suppliers.sort(key=lambda x: x.id)
    print_table("Suppliers", suppliers)

    # Employees report
    print("Employees report")
    query = """
        SELECT e.name, e.salary, b.location, 
            IFNULL(SUM(-a.quantity * p.price), 0)
        FROM employees e
        JOIN branches b ON e.branche = b.id
        LEFT JOIN activities a ON e.id = a.activator_id AND a.quantity < 0
        LEFT JOIN products p ON a.product_id = p.id
        GROUP BY e.id
        ORDER BY e.name ASC
    """
    for row in repo._conn.execute(query):
        print(row)

    # Activities report
    print("Activities report")
    query = """
        SELECT a.date, p.description, a.quantity,
               e.name AS seller_name,
               s.name AS supplier_name
        FROM activities a
        JOIN products p ON a.product_id = p.id
        LEFT JOIN employees e ON a.activator_id = e.id AND a.quantity < 0
        LEFT JOIN suppliers s ON a.activator_id = s.id AND a.quantity > 0
        ORDER BY a.date ASC
    """
    rows = repo._conn.execute(query).fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    main()