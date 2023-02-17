from db.run_sql import run_sql

TABLE_NAME = "??"
FIELDS = "X, X, X"

number_of_fields = len(FIELDS.split(","))
placeholders = ", ".join(["%s"] * number_of_fields)

# import model
# correct number of %s in sql queries to match fields


def select_all():
    tasks = []

    sql = f"SELECT * FROM {TABLE_NAME}"
    results = run_sql(sql)

    for row in results:
        # create object
        # append to list
        pass
    return tasks


def select(id):
    sql = f"SELECT * FROM {TABLE_NAME} WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        # create object
        # return object


def delete_all():
    sql = f"DELETE FROM {TABLE_NAME}"
    run_sql(sql)


def delete(id):
    sql = f"DELETE FROM {TABLE_NAME} WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def save(task):
    sql = f"""INSERT INTO {TABLE_NAME} ({FIELDS}) 
            VALUES ({placeholders}) RETURNING *"""
    values = []
    result = run_sql(sql, values)
    # set id on object ## task.id = result[0]["id"]


def update(task):
    sql = f"""UPDATE {TABLE_NAME} SET ({FIELDS}) = ({placeholders}) WHERE id = %s"""
    values = []
    run_sql(sql, values)
