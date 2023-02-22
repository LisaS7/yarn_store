DROP TABLE IF EXISTS colours;
DROP TABLE IF EXISTS yarns;
DROP TABLE IF EXISTS manufacturers;


CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    last_payment_date DATE,
    balance_due INT
);

CREATE TABLE yarns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE,
    yarn_weight VARCHAR(255),
    ball_weight_grams INT,
    length_metres INT,
    needle_size_mm DECIMAL,
    fibre_type VARCHAR(255),
    buy_cost INT,
    sell_price INT,
    image VARCHAR(255)
);

CREATE TABLE colours (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    hex_code VARCHAR(8),
    stock_quantity INT,
    yarn_id INT REFERENCES yarns(id) ON DELETE CASCADE
);