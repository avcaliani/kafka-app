from user_service.database import Database

__db = Database()


def create_table() -> None:
    __db.execute(
        """
        CREATE TABLE IF NOT EXISTS customers (
            customer_id TEXT PRIMARY KEY,
            customer_email TEXT UNIQUE,
            customer_name TEXT,
            customer_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """.strip()
    )


def new_user(customer: dict) -> None:
    query = f"""
        INSERT INTO customers(customer_id, customer_email, customer_name) 
        VALUES(
            '{customer.get("customer_id")}', 
            '{customer.get("customer_email")}', 
            '{customer.get("customer_name")}'
        )
        ON CONFLICT(customer_email) DO NOTHING;
    """.strip()
    __db.execute(query)
    return __db.select(
        f"SELECT * FROM customers WHERE customer_id = \"{customer.get('customer_id')}\" LIMIT 1"
    )
