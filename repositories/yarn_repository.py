from db.run_sql import run_sql
from models.yarn import Yarn
from repositories import manufacturer_repository
from config import yarn_table_name as TABLE_NAME, yarn_fields as FIELDS

number_of_fields = len(FIELDS.split(","))
placeholders = ", ".join(["%s"] * number_of_fields)


def select_all():
    yarns = []

    sql = f"SELECT * FROM {TABLE_NAME}"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row["manufacturer_id"])
        yarn = Yarn(
            row["name"],
            manufacturer,
            row["yarn_weight"],
            row["ball_weight_grams"],
            row["length_metres"],
            row["needle_size_mm"],
            row["fibre_type"],
            row["buy_cost"],
            row["sell_price"],
            row["image"],
            row["id"],
        )
        yarns.append(yarn)
    return yarns


def select(id):
    sql = f"SELECT * FROM {TABLE_NAME} WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result:
        manufacturer = manufacturer_repository.select(result["manufacturer_id"])
        yarn = Yarn(
            result["name"],
            manufacturer,
            result["yarn_weight"],
            result["ball_weight_grams"],
            result["length_metres"],
            result["needle_size_mm"],
            result["fibre_type"],
            result["buy_cost"],
            result["sell_price"],
            result["image"],
            result["id"],
        )
        return yarn


def delete_all():
    sql = f"DELETE FROM {TABLE_NAME}"
    run_sql(sql)


def delete(id):
    sql = f"DELETE FROM {TABLE_NAME} WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def save(yarn):
    sql = f"""INSERT INTO {TABLE_NAME} ({FIELDS}) 
            VALUES ({placeholders}) RETURNING *"""
    values = [
        yarn.name,
        yarn.manufacturer.id,
        yarn.yarn_weight,
        yarn.ball_weight_grams,
        yarn.length_metres,
        yarn.needle_size_mm,
        yarn.fibre_type,
        yarn.buy_cost,
        yarn.sell_price,
        yarn.image,
    ]
    result = run_sql(sql, values)
    print(result)
    yarn.id = result[0]["id"]


def update(yarn):
    sql = f"""UPDATE {TABLE_NAME} SET ({FIELDS}) = ({placeholders}) WHERE id = %s"""
    values = [
        yarn.name,
        yarn.manufacturer.id,
        yarn.yarn_weight,
        yarn.ball_weight_grams,
        yarn.length_metres,
        yarn.needle_size_mm,
        yarn.fibre_type,
        yarn.buy_cost,
        yarn.sell_price,
        yarn.image,
        yarn.id,
    ]
    run_sql(sql, values)
