from db.run_sql import run_sql
from datetime import datetime as dt

TABLE_NAME = "manufacturers"
FIELDS = "name, last_payment_date, balance_due"

number_of_fields = len(FIELDS.split(","))
placeholders = ", ".join(["%s"] * number_of_fields)

from models.manufacturer import Manufacturer


def select_all():
    manufacturers = []

    sql = f"SELECT * FROM {TABLE_NAME}"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(
            row["name"], row["last_payment_date"], row["balance_due"], row["id"]
        )
        manufacturers.append(manufacturer)
    return manufacturers


def select(id):
    sql = f"SELECT * FROM {TABLE_NAME} WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        manufacturer = Manufacturer(
            result["name"],
            result["last_payment_date"],
            result["balance_due"],
            result["id"],
        )
        return manufacturer


def delete_all():
    sql = f"DELETE FROM {TABLE_NAME}"
    run_sql(sql)


def delete(id):
    sql = f"DELETE FROM {TABLE_NAME} WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def save(manufacturer):
    sql = f"""INSERT INTO {TABLE_NAME} ({FIELDS}) 
            VALUES ({placeholders}) RETURNING *"""
    values = [
        manufacturer.name,
        manufacturer.format_date_for_psql(),
        manufacturer.balance_due,
    ]
    result = run_sql(sql, values)
    manufacturer.id = result[0]["id"]


# def update(task):
#     sql = f"""UPDATE {TABLE_NAME} SET ({FIELDS}) = ({placeholders}) WHERE id = %s"""
#     values = []
#     run_sql(sql, values)
