from db.run_sql import run_sql

TABLE_NAME = "yarns"
FIELDS = "name, manufacturer_id, yarn_weight, ball_weight_grams, length_metres, needle_size_mm, fibre_type, buy_cost, sell_price, image"

number_of_fields = len(FIELDS.split(","))
placeholders = ", ".join(["%s"] * number_of_fields)

from models.yarn import Yarn


# def select_all():
#     tasks = []

#     sql = f"SELECT * FROM {TABLE_NAME}"
#     results = run_sql(sql)

#     for row in results:
#         # create object
#         # append to list
#         pass
#     return tasks


# def select(id):
#     sql = f"SELECT * FROM {TABLE_NAME} WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)

#     if results:
#         result = results[0]
#         # create object
#         # return object


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
    yarn.id = result[0]["id"]


# def update(task):
#     sql = f"""UPDATE {TABLE_NAME} SET ({FIELDS}) = ({placeholders}) WHERE id = %s"""
#     values = []
#     run_sql(sql, values)