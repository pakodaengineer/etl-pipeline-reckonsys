
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS items;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    age INTEGER NOT NULL
);

CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    item_name TEXT NOT NULL
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    purchase_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    item_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

INSERT INTO customers (customer_id, age) VALUES
(1, 21),
(2, 23),
(3, 35),
(4, 45); 

INSERT INTO items (item_id, item_name) VALUES
(1, 'x'),
(2, 'y'),
(3, 'z');

INSERT INTO orders (order_id, customer_id, purchase_date) VALUES
(1, 1, '2025-01-10'),
(2, 1, '2025-01-15'),
(3, 2, '2025-01-20'),
(4, 3, '2025-01-25'),
(5, 3, '2025-01-28'),
(6, 4, '2025-01-30'); 

INSERT INTO sales (sale_id, order_id, item_id, quantity) VALUES
(1, 1, 1, 5),
(2, 2, 1, 5),
(3, 3, 1, 1),
(4, 3, 2, 1),
(5, 3, 3, 1),
(6, 4, 3, 1),
(7, 5, 3, 1),
(8, 6, 1, 10);
