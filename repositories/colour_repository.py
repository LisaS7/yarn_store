from db.run_sql import run_sql
from repositories import yarn_repository
from models.colour import Colour

from config.config import config

TABLE_NAME = config.db_data["colours"]["table_name"]
FIELDS = config.db_data["colours"]["fields"]

number_of_fields = len(FIELDS.split(","))
placeholders = ", ".join(["%s"] * number_of_fields)


def select_all():
    colours = []

    sql = f"SELECT * FROM {TABLE_NAME} ORDER BY name"
    results = run_sql(sql)

    for row in results:
        yarn = yarn_repository.select(row["yarn_id"])
        colour = Colour(
            row["name"],
            row["hex_code"],
            row["stock_quantity"],
            yarn,
            row["id"],
        )
        colours.append(colour)
    return colours


def select(id):
    sql = f"SELECT * FROM {TABLE_NAME} WHERE id = %s ORDER BY name"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        yarn = yarn_repository.select(result["yarn_id"])
        colour = Colour(
            result["name"],
            result["hex_code"],
            result["stock_quantity"],
            yarn,
            result["id"],
        )
        return colour


def delete_all():
    sql = f"DELETE FROM {TABLE_NAME}"
    run_sql(sql)


def delete(id):
    sql = f"DELETE FROM {TABLE_NAME} WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def save(colour):
    sql = f"""INSERT INTO {TABLE_NAME} ({FIELDS}) 
            VALUES ({placeholders}) RETURNING *"""
    values = [colour.name, colour.hex_code, colour.stock_quantity, colour.yarn.id]
    result = run_sql(sql, values)
    colour.id = result[0]["id"]


def update(colour):
    sql = f"""UPDATE {TABLE_NAME} SET ({FIELDS}) = ({placeholders}) WHERE id = %s"""
    values = [
        colour.name,
        colour.hex_code,
        colour.stock_quantity,
        colour.yarn.id,
        colour.id,
    ]
    run_sql(sql, values)


def select_by_yarn(yarn_id):
    colours = []
    sql = f"SELECT * FROM {TABLE_NAME} WHERE yarn_id = %s ORDER BY name"
    values = [yarn_id]
    results = run_sql(sql, values)

    for row in results:
        yarn = yarn_repository.select(row["yarn_id"])
        colour = Colour(
            row["name"],
            row["hex_code"],
            row["stock_quantity"],
            yarn,
            row["id"],
        )
        colours.append(colour)
    return colours
