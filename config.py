db_name = "yarn_store"

manufacturer_table_name = "manufacturers"
manufacturer_fields = "name, last_payment_date, balance_due"

yarn_table_name = "yarns"
yarn_fields = "name, manufacturer_id, yarn_weight, ball_weight_grams, length_metres, needle_size_mm, fibre_type, buy_cost, sell_price, image"
yarn_weights = ["2ply", "4ply", "DK", "Aran", "Chunky", "Super Chunky"]

colours_table_name = "colours"
colours_fields = "name, hex_code, stock_quantity, yarn_id"
stock_low_threshold = 10
